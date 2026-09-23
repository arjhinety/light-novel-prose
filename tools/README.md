# Tools

> **Purpose:** optional helper scripts that measure a draft against the library's voice gates.
> **Load when:** you can run code and want numbers instead of an estimate during revision.
> **Related:** [Revision Checklist](../revision/revision-checklist.md), [Style Bible](../core/style-bible.md), [Dialogue Mechanics](../dialogue/dialogue-mechanics.md), [Punctuation & Typography](../core/punctuation-and-typography.md)

## 1. This folder is optional

The library works without code: every gate here can also be estimated by hand (see [Revision Checklist](../revision/revision-checklist.md)). If your environment can run a script (a coding agent, a terminal, a notebook), use `voice_metrics.py` to get exact numbers. If it can't, skip this folder.

## 2. `voice_metrics.py`

Pure Python 3 standard library, no installs.

```
python tools/voice_metrics.py path/to/chapter.md
python tools/voice_metrics.py ch1.md ch2.md ch3.md
python tools/voice_metrics.py chapter.md --json
python tools/voice_metrics.py chapter.md --introspective
```

The exit code is `0` when every gate passes and `1` otherwise, so an agent can loop until it passes.

### What it measures

| Metric | Gate | Rule |
|---|---|---|
| Dialogue ratio (words inside quotes / all words) | 40-55% (35-55% with `--introspective`) | Voice profile |
| Narrative sentence median (words) | ≤ 10 | Rhythm |
| Long narrative sentences (≥ 25 words) | ≤ 5% | Rhythm |
| Mixed dialogue paragraphs | 0 | R1, pure dialogue lines |
| Dash asides in narration | 0 | R2, dashes only for cut-offs |
| Repeated 5-gram tics (3+ times, 2+ content words) | 0 | Anti-robotic |
| Silent `"..."` lines, numbered sections | reported, no gate | Texture |

### How it decides

- **Header blocks, headings, code fences, and `---` rules are ignored**, so you can run it on library files with `> **Purpose:**` headers.
- **Dialogue** is anything inside `"..."` or curly quotes on one line.
- **A mixed paragraph** is one that has a quotation plus 2 or more words outside it, such as `"Fine," she said.` or `Rin crossed her arms. "Whatever."`. Fix it by splitting the narration into its own paragraph.
- **A dash aside** is any `--` or `—` in narration except one that ends the paragraph (a broken-off thought, which R2 allows). Dashes inside quotation marks (cut-off speech) are never counted.
- **Narrative sentences** are split on `. ! ?` and line breaks after removing quotations.
- **Tics** are 5-word sequences that repeat 3 or more times and contain at least 2 non-stopwords. An intentional callback (a catchphrase, a chant) will trip it. Check that the repetition is deliberate, and if it is, ignore the flag.

### Known limits

- Quotations that span a line break aren't detected as dialogue. Keep each quote on one line (the house style does this anyway).
- In-world text written in quotation marks (a sign, a text message) counts as dialogue. Format it as a block instead (see [Social Media & Texts](../setting/social-media-and-texts.md)).
- Narration that quotes back a phrase in quotation marks is flagged as mixed. That's by design: R1 says quoted-back phrases go in *italics*.
- It measures form, not quality. A chapter can pass every gate and still be dull. Use it after the reading passes in the revision checklist, not instead of them.

## 3. Suggested agent loop

1. Draft the chapter.
2. Run the script.
3. For each FAIL, apply the fix from the revision checklist: split mixed paragraphs, replace dash asides with periods, break long sentences, and **add dialogue beats rather than cut narration** when the ratio is low.
4. Re-run until PASS, or until the only remaining flags are deliberate (for example a callback tic).
5. Do a final read-aloud pass. The numbers never replace the ear.
