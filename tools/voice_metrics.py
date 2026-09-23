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
    dialogue contraction share >= 50%
    "That's not X. That's Y." pairs <= 0.5 per 1,000 words
    stock simile frames ("with the dignity of a...", "the way a...") <= 1.0 per 1,000 words
Warnings (manual check, not gates):
    longest dialogue run > 8 lines   fine for a two-person duet with distinct voices;
                                     with 3+ speakers, re-anchor at least every 4 lines
"""
import argparse
import json
import re
import statistics
import sys
from collections import Counter

QUOTE_RE = re.compile(r'"[^"\n]*"|“[^”\n]*”')
DASH_RE = re.compile(r"--|—")
CONTR_RE = re.compile(r"\b\w+['’](?:s|re|ll|ve|d|t|m)\b", re.I)
FULL_RE = re.compile(r"\b(?:it is|that is|there is|what is|i am|you are|we are|they are|he is|she is|"
                     r"do not|does not|did not|is not|are not|was not|cannot|can not|will not|"
                     r"would not|could not|should not|i will|you will|i have|i would)\b", re.I)
# "That's not X. That's Y." negation-pair crutch (and "It isn't X. It's Y.")
NXY_RE = re.compile(r"\b(?:that'?s|it'?s|that is|it is|this is)\s+not\b[^.!?\n\"”]{1,60}[.,;!]\s*(?:that'?s|it'?s|that is|it is|this is)\b"
                    r"|\b(?:that|it|this) isn'?t\b[^.!?\n\"”]{1,60}[.,;!]\s*(?:that'?s|it'?s|it is|that is)\b"
                    r"|\bnot \w+(?: \w+){0,3}[.,] (?:just )?\w+(?: \w+){0,3}\.(?=\s*$)", re.I | re.M)
# Stock simile frames: "with the dignity of a...", "the way a pilot looks...", "like a kettle deciding..."
SIM_RE = re.compile(r"\bwith the (?:\w+ )?\w+ of (?:a|an|someone|somebody|a man|a girl)\b"
                    r"|\bthe way (?:a|an|someone|people|you) \w+"
                    r"|\blike (?:a|an) (?:\w+ ){0,2}(?:that|who|being|trying|deciding|asking)\b"
                    r"|\blike (?:a|an) \w+ \w+s (?:a|an|the|his|her|their)\b", re.I)
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
    run = longest_run = 0
    contr = full = 0

    for p in paras:
        words = WORD_RE.findall(p)
        total_words += len(words)
        if re.fullmatch(r"\d{1,3}", p):
            sections += 1
            continue
        quotes = QUOTE_RE.findall(p)
        is_pure = bool(quotes) and not WORD_RE.search(QUOTE_RE.sub("", p))
        run = run + 1 if is_pure else 0
        longest_run = max(longest_run, run)
        for q in quotes:
            contr += len(CONTR_RE.findall(q))
            full += len(FULL_RE.findall(q))
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
    contr_share = contr / (contr + full) if (contr + full) else 1.0
    nxy = len(NXY_RE.findall(body))
    sim = len(SIM_RE.findall(body))
    per_k = 1000 / total_words if total_words else 0
    nxy_rate, sim_rate = nxy * per_k, sim * per_k
    floor = 0.35 if introspective else 0.40
    gates = {
        "dialogue_ratio": floor <= ratio <= 0.55,
        "narrative_median": median <= 10,
        "long_sentences": long_pct <= 0.05,
        "mixed_dialogue_paragraphs": len(mixed) == 0,
        "dash_asides": dash_asides == 0,
        "repeated_tics": len(tics) == 0,
        "contractions": contr_share >= 0.5,
        "negation_pairs": nxy_rate <= 0.5,
        "stock_similes": sim_rate <= 1.0,
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
        "longest_dialogue_run": longest_run,
        "contraction_share": round(contr_share, 3),
        "negation_pairs": nxy,
        "negation_pairs_per_1k": round(nxy_rate, 2),
        "stock_similes": sim,
        "stock_similes_per_1k": round(sim_rate, 2),
        "warnings": ([f"longest dialogue run is {longest_run} lines: if 3+ characters speak in it, re-anchor speakers at least every 4 lines"] if longest_run > 8 else []),
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
    print(f"  longest dialogue run      {r['longest_dialogue_run']} lines   [{'WARN' if r['warnings'] else 'ok'}]")
    print(f"  dialogue contractions     {r['contraction_share']:.0%}   [{ok(g['contractions'])}]")
    print(f"  not-X-that's-Y pairs      {r['negation_pairs']} ({r['negation_pairs_per_1k']}/1k)   [{ok(g['negation_pairs'])}]")
    print(f"  stock simile frames       {r['stock_similes']} ({r['stock_similes_per_1k']}/1k)   [{ok(g['stock_similes'])}]")
    print(f"  silent \"...\" lines        {r['silent_lines']}")
    print(f"  numbered sections         {r['numbered_sections']}")
    for w in r["warnings"]:
        print(f"      warning: {w}")
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
