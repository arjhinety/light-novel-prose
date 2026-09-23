#!/usr/bin/env python3
"""voice_metrics.py - measure a chapter against the light-novel-prose voice gates.

Optional helper. Pure Python standard library, no dependencies.

Usage:
    python voice_metrics.py chapter.md [more.md ...]
    python voice_metrics.py chapter.md --json
    python voice_metrics.py chapter.md --introspective   # allows 35% dialogue floor

Gates (see revision/revision-checklist.md):
    dialogue ratio 40-55%            (35-55% with --introspective)
    narrative sentence median <= 10 words
    long narrative sentences (>=25 words) <= 5%
    mixed dialogue paragraphs = 0     (R1: pure dialogue lines)
    dash asides in narration = 0      (R2: dashes only for cut-offs)
    repeated tics (5-grams x3+) = 0
"""
import argparse
import json
import re
import statistics
import sys
from collections import Counter

QUOTE_RE = re.compile(r'"[^"\n]*"|“[^”\n]*”')
DASH_RE = re.compile(r"--|—")
WORD_RE = re.compile(r"[A-Za-z0-9']+")
STOP = set("""a an the and or but so of to in on at for with by from as is was were be been
it its he she they them his her their him i you we me my your our this that these those
not no do did does had has have just then than there here what who when where how why
up down out over into onto off about again very too also all any some one two""".split())


def strip_markup(text):
    """Remove the header block, headings, code fences, and horizontal rules."""
    out, in_code = [], False
    for line in text.splitlines():
        s = line.strip()
        if s.startswith("```"):
            in_code = not in_code
            continue
        if in_code or s.startswith("#") or s.startswith(">") or s in ("---", "***", "* * *"):
            out.append("")
            continue
        out.append(line)
    return "\n".join(out)


def paragraphs(text):
    return [p.strip() for p in re.split(r"\n\s*\n", text) if p.strip()]


def sentences(narr):
    parts = re.split(r"(?<=[.!?])\s+|\n+", narr)
    return [p for p in parts if WORD_RE.search(p)]


def analyze(path, introspective=False):
    raw = open(path, encoding="utf-8", errors="replace").read()
    body = strip_markup(raw)
    paras = paragraphs(body)

    total_words = 0
    dialogue_words = 0
    narr_chunks = []
    mixed = []
    silent = 0
    sections = 0
    dash_total = 0
    dash_asides = 0

    for p in paras:
        words = WORD_RE.findall(p)
        total_words += len(words)
        if re.fullmatch(r"\d{1,3}", p):
            sections += 1
            continue
        quotes = QUOTE_RE.findall(p)
        if quotes:
            dialogue_words += sum(len(WORD_RE.findall(q)) for q in quotes)
            if all(re.fullmatch(r'["“](\.\.\.|…)["”]', q) for q in quotes) and \
                    not WORD_RE.search(QUOTE_RE.sub("", p)):
                silent += 1
            rest = QUOTE_RE.sub(" ", p)
            if len(WORD_RE.findall(rest)) >= 2:
                mixed.append(p[:90].replace("\n", " "))
            narr = rest
        else:
            narr = p
        # Narration dashes: a dash that ends the paragraph (a broken-off thought) is allowed.
        n_dash = len(DASH_RE.findall(narr))
        if n_dash:
            dash_total += n_dash
            trailing = 1 if DASH_RE.search(narr.rstrip(" *_’'")[-2:] or "") else 0
            dash_asides += max(0, n_dash - trailing)
        if WORD_RE.search(narr):
            narr_chunks.append(narr)

    narr_text = "\n".join(narr_chunks)
    lens = [len(WORD_RE.findall(s)) for s in sentences(narr_text)]
    median = statistics.median(lens) if lens else 0
    long_pct = (sum(1 for n in lens if n >= 25) / len(lens)) if lens else 0.0

    toks = [t.lower() for t in WORD_RE.findall(body)]
    grams = Counter(tuple(toks[i:i + 5]) for i in range(len(toks) - 4))
    tics = sorted(
        ((" ".join(g), c) for g, c in grams.items()
         if c >= 3 and sum(1 for w in g if w not in STOP) >= 2),
        key=lambda x: -x[1])

    ratio = dialogue_words / total_words if total_words else 0.0
    floor = 0.35 if introspective else 0.40
    gates = {
        "dialogue_ratio": floor <= ratio <= 0.55,
        "narrative_median": median <= 10,
        "long_sentences": long_pct <= 0.05,
        "mixed_dialogue_paragraphs": len(mixed) == 0,
        "dash_asides": dash_asides == 0,
        "repeated_tics": len(tics) == 0,
    }
    return {
        "file": path,
        "words": total_words,
        "dialogue_ratio": round(ratio, 3),
        "narrative_sentences": len(lens),
        "narrative_median": median,
        "long_sentence_pct": round(long_pct, 3),
        "mixed_dialogue_paragraphs": len(mixed),
        "mixed_examples": mixed[:5],
        "narration_dashes": dash_total,
        "dash_asides": dash_asides,
        "silent_lines": silent,
        "numbered_sections": sections,
        "repeated_tics": tics[:10],
        "gates": gates,
        "pass": all(gates.values()),
    }


def report(r):
    ok = lambda b: "PASS" if b else "FAIL"
    g = r["gates"]
    print(f"== {r['file']}")
    print(f"  words                     {r['words']}")
    print(f"  dialogue ratio            {r['dialogue_ratio']:.0%}   [{ok(g['dialogue_ratio'])}]")
    print(f"  narrative median          {r['narrative_median']} words   [{ok(g['narrative_median'])}]")
    print(f"  long sentences (>=25)     {r['long_sentence_pct']:.1%}   [{ok(g['long_sentences'])}]")
    print(f"  mixed dialogue paragraphs {r['mixed_dialogue_paragraphs']}   [{ok(g['mixed_dialogue_paragraphs'])}]")
    for m in r["mixed_examples"]:
        print(f"      e.g. {m}")
    print(f"  dash asides in narration  {r['dash_asides']} (of {r['narration_dashes']})   [{ok(g['dash_asides'])}]")
    print(f"  repeated 5-gram tics      {len(r['repeated_tics'])}   [{ok(g['repeated_tics'])}]")
    for t, c in r["repeated_tics"][:5]:
        print(f"      x{c}  {t}")
    print(f"  silent \"...\" lines        {r['silent_lines']}")
    print(f"  numbered sections         {r['numbered_sections']}")
    print(f"  OVERALL                   {'PASS' if r['pass'] else 'FAIL'}")


def main():
    ap = argparse.ArgumentParser(description="Measure prose against the light-novel-prose voice gates.")
    ap.add_argument("files", nargs="+")
    ap.add_argument("--json", action="store_true", help="print JSON instead of a report")
    ap.add_argument("--introspective", action="store_true", help="allow a 35%% dialogue floor")
    a = ap.parse_args()
    results = [analyze(f, a.introspective) for f in a.files]
    if a.json:
        print(json.dumps(results if len(results) > 1 else results[0], indent=2))
    else:
        for r in results:
            report(r)
    sys.exit(0 if all(r["pass"] for r in results) else 1)


if __name__ == "__main__":
    main()
