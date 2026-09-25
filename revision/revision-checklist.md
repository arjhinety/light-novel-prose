# Revision Checklist

> **Purpose:** A repeatable, multi-pass edit protocol with a scoring rubric, so every chapter is revised the same disciplined way before it is delivered.
> **Load when:** After finishing any draft (scene, chapter, or rewrite), and whenever a user asks to "polish", "fix", "edit", or "make it less robotic".
> **Related:** [Anti-Robotic Prose](anti-robotic.md), [MTL vs. Natural](mtl-vs-natural.md), [Style Bible](../core/style-bible.md), [Rhythm & Flow](../core/rhythm-and-flow.md), [Hooks & Cliffhangers](../structure/hooks-and-cliffhangers.md), [Honorifics & Address](../dialogue/honorifics-and-address.md), [Before & After](../examples/before-after.md), [Genre Index](../genres/genre-index.md)

---

## 1. Principles

1. **Revise in passes, not all at once.** Each pass has one question. Trying to fix rhythm, names, and structure simultaneously means none of them get fixed.
2. **Structure before sentences.** Don't polish a paragraph you're going to cut.
3. **Measure what can be measured.** Sentence lengths, banned-phrase counts, and dialogue ratio are countable, so count them. Taste is for what can't be counted.
4. **Protect the texture.** Every pass has a "don't over-correct" note. Revising a light novel into generic literary English is a failure too ([MTL vs. Natural §7](mtl-vs-natural.md#7-over-correction-the-opposite-failure)).
5. **Revision is silent.** The user receives the finished prose, not your checklist. Only report revision notes if the user asks.

---

## 2. The measurable voice gates (hard pass/fail)

Taste can be argued with. These cannot. **A draft that fails any gate is not delivered**, whatever its rubric score. They exist because test runs of this library showed strong models passing their own taste checks while drifting far off the voice: a narrative median of 15 words, 27% long sentences, 30% dialogue, 47 dash asides, and 69-100 paragraphs mixing speech with narration, all in "finished" chapters.

| Gate | Pass condition | Why |
|---|---|---|
| **G1 Dialogue share** | 40-55% of the chapter's words are inside quotation marks. Only a chapter the plan explicitly marks "introspective" may go to 35%, **never lower**. | Half the voice is talk. Below 40% the chapter turns into Western narration. |
| **G2 Narrative median** | The median narrative sentence is **≤10 words** (the source sits near 7) | Short beats are the rhythm |
| **G3 Long sentences** | **≤5%** of narrative sentences are 25+ words | One long exhale per scene, not per paragraph |
| **G4 Pure dialogue lines** | **0** paragraphs that mix a quote with narration, and **0** speech tags ([Dialogue Mechanics §2](../dialogue/dialogue-mechanics.md#2-the-pure-dialogue-line-hard-rule)) | The house layout; the user's explicit rule |
| **G5 Dashes** | **0** dash asides in narration. Dashes appear only on cut-off speech or a thought that breaks off ([Anti-Robotic §3.13](anti-robotic.md#313-the-em-dash-cascade)) | Dash asides are the clearest Western-literary tell |
| **G6 Tics** | No sentence construction or 5-word phrase repeated 3+ times (except deliberate leitmotifs, chants, and callbacks), and every [model tic](anti-robotic.md#25-model-specific-tics-found-in-test-runs) under its cap | Repeated constructions become a visible fingerprint |
| **G7 Length** | At or above the requested word count, reached through beats that each pass the [beat test](../structure/chapter-and-section.md#81-reaching-length-the-right-way-r4) (§3 below) | Short chapters break the request; padded ones break the voice |
| **G8 Speaker anchoring** | With 3+ characters present, every line that carries plot, information, or feeling passes the [speaker test](../dialogue/dialogue-mechanics.md#33-the-speaker-test-hard-rule-with-3-characters), and no more than **4** dialogue lines run without a narration paragraph | Pure dialogue lines remove tags; without anchors, group scenes turn into anonymous voices |
| **G9 Contractions** | At least **50%** of the phrases in dialogue that could be contracted are contracted. Only characters designed as formal speak uncontracted ([Character Voices §6](../dialogue/character-voices.md#6-common-failures)) | An uncontracted cast sounds identical and machine-translated |
| **G10 Crutch patterns** | "That's not X. That's Y." pairs ≤0.5 per 1,000 words; stock simile frames ≤1.0 per 1,000 words ([Anti-Robotic §2.5](anti-robotic.md#25-model-specific-tics-found-in-test-runs)); each payoff delivered once ([Chapter & Section §9.1](../structure/chapter-and-section.md#91-spend-each-payoff-once)) | In the v2.1 tests, an independent reviewer singled out both crutches as the clearest signs of AI writing |
| **G11 Content rule** | Every fanservice or sexual beat is either (a) between characters the text establishes as adults, at whatever heat the request named, or (b) written as non-sexual comedy with an underage cast. No sexual rendering of a character under 18, ever ([Ecchi §1](../genres/ecchi-and-fanservice.md#1-the-content-line)) | Adults are unrestricted; this is the library's one hard line |

### 2.1 Measuring with the script (if you can run code)

If your environment can execute Python, run the optional, dependency-free script on the draft:

```
python tools/voice_metrics.py path/to/chapter.md
python tools/voice_metrics.py path/to/chapter.md --json
```

It reports words, dialogue ratio, narrative median, the percentage of sentences at 25+ words, mixed dialogue paragraphs, narration dashes, repeated 5-gram tics, and the dialogue contraction share, each with PASS/FAIL against the gates above. It also reports silent `"..."` lines, numbered sections, and the longest run of consecutive dialogue lines, with a warning above 8. The script can't count speakers, so a warning in a two-person duet is fine, while a warning in a group scene means G8 needs a manual check. See [`tools/voice_metrics.py`](../tools/voice_metrics.py). The script is a measuring tape, not a judge: a draft can pass every gate and still be flat. The rubric (§5) handles that.

### 2.2 Measuring by hand (if you can't)

Estimate from **three random 300-word windows** (one from the first third of the chapter, one from the middle, one from the last third). This takes a few minutes and is accurate enough to catch drift.

1. **G1 Dialogue share.** In each window, count the words inside quotation marks and divide by 300. Average the three. If any single window is under 25% and it isn't a solo scene, look there first.
2. **G2 and G3 Sentences.** In each window, list the word count of every *narrative* sentence (skip quotes). Sort the list and take the middle value: that's the median. Count how many are 25+ words. If more than 1 in 20 is, G3 fails.
3. **G4 Mixed paragraphs.** Don't sample for this one. Scan **every** paragraph that contains a quotation mark. If there's a single word outside the quote marks, it fails. Split it.
4. **G5 Dashes.** Scan every narration paragraph for `--` or `—`. Each one must be a thought breaking off. Anything else gets rewritten.
5. **G6 Tics.** Search the draft for the [§2.5 model tics](anti-robotic.md#25-model-specific-tics-found-in-test-runs) and for your own favorite constructions (*the way*, *something in*, *for once*, *the specific*). Count them.
6. **G7 Length.** Count words, or estimate: lines × average words per line. Then name, in one sentence each, what every section's beats changed. A beat you can't name is padding.
7. **G8 Speaker anchoring.** In every scene with 3+ characters, cover the narration and read only the quotes. Mark each line that matters where you'd have to guess the speaker. Every mark gets an action paragraph.
8. **G9 Contractions.** In one window, count *it is / I am / do not / that is*-type full forms in dialogue against contractions. If the full forms win, rewrite every non-formal character's lines.

Write the numbers down. "It feels about half dialogue" is how the test chapters landed at 30%.

## 3. The length procedure

When a draft is short of its target, **add beats and scenes, never longer sentences.** Test runs showed the failure clearly: one model padded to 6,000 words by inflating sentences (median 15, 27% long), and another stopped at 3,800 words of a 5,000-word request.

1. **Plan the section count from the target before drafting.** At 600-1,200 words per section: 2,500 words is 3-4 sections, 5,000 words is 6-8, and 8,000 words is 9-12.
2. **If you're short after drafting**, add a whole beat, in this order of preference:
   - **A new arrival** who changes the room's energy (another character walks in mid-scene)
   - **A second escalation** of the chapter's situation (the plan goes wrong again, in a new way)
   - **A quiet two-person moment** between the chaos and the payoff (the rooftop, the stairwell, the walk to the station)
   - **A cut-away section** from another character's POV, short and ominous or teasing ([Narration & POV](../core/narration-and-pov.md))
   - **A callback scene** that returns an earlier object or line with a new charge
   - **A chatter burst** where the chapter has been all two-person dialogue
3. **Each added beat must pass the gates on its own.** New material inherits the same dialogue share and sentence profile.
4. **Never pad by:** restating a feeling already shown, adding a second simile to a sentence, extending the analytical spiral past its verdict, describing scenery, or summarizing an exchange instead of playing it.
5. **Re-measure G1-G3** after adding. Padding usually shows up as G1 dropping and G2 rising.

---

## 4. The seven-pass protocol

### Pass 0: Cold read (as a reader)

Read the whole draft once without editing. Answer three questions in one line each:
- What is the **situation**?
- What is the **turn**, the moment the POV's reading changes?
- What is the **hook** that makes the reader click "next"?

If you can't answer any of the three, stop. The problem is structural. Go back to the [chapter plan](../templates/chapter-plan.md) before touching sentences.

### Pass 1: Structure

| Check | Pass condition |
|---|---|
| Numbered sections | One every ~600-1,200 words, each a single scene or single spiral |
| Openings | The chapter opens with a sound, dialogue, time stamp, solitary thought, or cut-away, not weather or backstory |
| Section endings | Every section's last line is a tilt: reveal, arrival, reframe, silence, or verdict ([Hooks](../structure/hooks-and-cliffhangers.md)) |
| Chapter hook | The final line creates a question the next chapter must answer |
| Scene skips | Time jumps inside a section are marked ("After school--", "The next day--") |
| Length | At or above the requested length (default 2,500-4,500 words per chapter), reached through beats per the length procedure (§3), not padding |

**Don't over-correct:** Not every section needs a cliffhanger. A quiet verdict ("Hypocrite.") counts as a tilt.

### Pass 2: Voice and POV

| Check | Pass condition |
|---|---|
| POV anchor | Each section stays inside one head. Cut-aways are marked by a section break. |
| Naming in narration | The POV is called by surname in original stories ([Narration & POV](../core/narration-and-pov.md)); in fan fiction, the source series' convention is followed ([Fan Fiction & Canon](../adaptation/fanfic-and-canon.md)) |
| Free indirect thought | At least three moments per section where narration slides into the POV's own present-tense question |
| Analytical engine | At least one full spiral per chapter: notice, quote back, hypotheses, self-suspicion, verdict ([Inner Monologue](../core/inner-monologue.md)), aimed where the POV's temperament points ([POV Temperaments](../core/pov-temperaments.md)) |
| Leitmotif | The POV's private image (e.g., "the sediment") appears at least once, and not more than three times in a calm chapter |
| Warmth | At least one moment where the cynicism cracks, such as noticing a kindness or feeling guilty |
| Genre dials | Comedy ratio, description density, and POV habits match the genre file |

**Don't over-correct:** Don't add spirals to every paragraph. One strong spiral beats five weak ones.

### Pass 3: Dialogue

| Check | Pass condition |
|---|---|
| Ratio | Gate G1: 40-55% of words (35% floor only for a chapter planned as introspective) |
| Voice test | Reading only the dialogue, each speaker is identifiable |
| Pure lines | Gate G4: every quote alone in its paragraph; zero speech tags, "said" included; actions in their own paragraphs |
| Dodge | At least one question per scene goes unanswered, deflected, or met with `"..."` |
| Stacking | Group scenes include at least one unattributed burst of 4+ lines |
| POV's speech | The POV speaks less than he thinks; his lines are shorter than his monologue |
| Emotional scenes | High-emotion dialogue gets *shorter*, not longer ([Emotional Dialogue](../dialogue/emotional-dialogue.md)) |

### Pass 4: Rhythm

Do this pass **by counting**.

1. Pick three random narration paragraphs. Count words per sentence.
2. Target band (gates G2 and G3): the median is 6-10 words, more than half are under 10, roughly one long exhale of 20-30 words per scene, and no more than 5% of narrative sentences at 25+ words.
3. Flag any run of **four or more sentences within two words of each other in length**. Break the run with a one-liner or merge into a long exhale.
4. Flag any paragraph over six sentences in a non-climax scene. Split it at the turn.
5. Check that each one-line paragraph is *landing* something (a sound, a verdict, a realization, a silence). One-liners that land nothing get merged ([MTL vs. Natural §3.1](mtl-vs-natural.md#31-clause-splitting-choppiness)).
6. Read one page "aloud" in your head. Where you'd stumble, fix it.

**Don't over-correct:** The LN voice is short-sentence-heavy. Don't "fix" it into long literary sentences. The goal is *variation with intent*, not length.

### Pass 5: Anti-robotic sweep

Run the full detection protocol in [Anti-Robotic Prose §6](anti-robotic.md#6-detection-protocol-run-on-every-draft):
- Banned lexicon (zero in narration)
- Structural shapes under threshold
- Therapy-speak
- Explanation deletion test on every post-dialogue narration line
- At least four humanizing moves

### Pass 6: Consistency

| Check | Pass condition |
|---|---|
| Names | Spelled identically everywhere |
| Address forms | Each speaker uses the same honorific for each listener, matching the story bible. Any change is deliberate and noticed in-text ([Honorifics](../dialogue/honorifics-and-address.md)). |
| Visual signatures | Hair, eyes, and signature gestures match the character sheets |
| Timeline | The day, period, and season are consistent (the bell doesn't ring for lunch at 9 a.m.) |
| Setting facts | Club names, class number, and train stops are consistent with the bible |
| Callbacks | Any callback matches what was actually planted |
| Open questions | Questions left open are intentionally open (listed in the chapter plan) |

### Pass 7: Surface polish

| Check | Pass condition |
|---|---|
| `"..."` | Used as a full line of silence, and not more than ~5 times per chapter unless in a monologue-and-silence duet |
| `--` / `—` | Gate G5: only on cut-off speech or a thought that breaks off; one glyph per story; zero dash asides in narration |
| `~` | Only in dialogue, only for characters with a drawl |
| Stutters | Only under fluster, with the first letter repeated: "W-What" |
| `?!` | Dialogue only |
| SFX | Readable, standalone, 1-4 per chapter |
| Typos | None |

See [Punctuation & Typography](../core/punctuation-and-typography.md).

---

## 5. The scoring rubric

Score the draft 0-5 on each axis after Pass 7. **Deliver only when every gate in §2 passes, the total is ≥ 40/50, and no axis is below 3.** A failed gate caps the related axis at 2 (G1 or G4 caps Dialogue, G2 or G3 caps Rhythm, G5 or G6 caps Non-robotic texture).

| # | Axis | 0-1 (failing) | 3 (acceptable) | 5 (excellent) |
|---|---|---|---|---|
| 1 | **Voice** | Generic narrator; could be any book | Recognizably LN; some flat stretches | Unmistakably this POV; every paragraph sounds like him |
| 2 | **Inner monologue** | Absent or abstract ("he felt conflicted") | Present; some concrete analysis | Petty, specific, self-suspicious spirals that make the reader suspect with him |
| 3 | **Rhythm & flow** | Monotone lengths or MTL choppiness | Varied but mechanical | Short beats land, long exhales carry; reads aloud smoothly |
| 4 | **Dialogue** | Q&A exchanges; voices indistinguishable; tags and beats inside quote paragraphs | Distinct voices; pure lines; a few flat exchanges | Speakers recognizable from the words alone; dodges, stammers, banter snap |
| 5 | **Non-robotic texture** | Multiple banned phrases; explained subtext | Clean of tells but a little bland | Clean, and actively human: trivia, pettiness, failed jokes, callbacks |
| 6 | **Characterization** | Archetype labels only | Archetypes with some specificity | Each character has a crack in the image; public vs. private face shows |
| 7 | **Structure** | No sections or tilts; summarized endings | Sections present; some endings flat | Every section tilts; the chapter hook compels |
| 8 | **Japanese texture** | Westernized, or MTL-stiff | Honorifics and some SFX present | Honorifics, silence lines, SFX, and school systems woven in naturally |
| 9 | **Emotional truth** | Melodrama or flatness | Emotions believable | The earnest peak hits harder because of the irony around it |
| 10 | **Genre fit** | Ignores genre conventions | Follows the genre file | Uses the genre's pleasures precisely (gag timing, dread, battle beats...) |

### How to score honestly

- **Quote evidence for every score.** "Voice: 4, because the spiral in section 2 ('Not "what are you doing here"...') is strong, but section 3 slips into neutral summary." A score without a quoted line is a guess.
- **Score the weakest section, not the average.** A chapter is only as good as its flattest stretch.
- **Assume you're too generous.** Models over-score their own drafts. Before recording any 5, find one line in that axis you'd still improve. If you can, it's a 4.

---

## 6. The self-critique loop

```
draft
  └─> Gates G1-G7 (§2) ── any fail ──> fix that gate first, re-measure
  └─> Passes 0-7
        └─> score (10 axes, with quoted evidence)
              ├─ gates pass, total ≥ 40, every axis ≥ 3  ──> deliver
              └─ otherwise
                    └─> choose the TWO lowest axes
                          └─> targeted rewrite of the sections that caused them
                                └─> re-run Passes 4-7 on the changed sections only
                                      └─> re-score (max 3 loops)
```

**Rules for the loop:**
1. **Fix the two lowest axes only.** Rewriting everything reintroduces problems already fixed.
2. **Rewrite whole paragraphs, not words.** Swapping synonyms won't raise the voice score. Re-imagine the beat from inside the POV's head.
3. **Three loops maximum.** If the draft still fails after three, the plan is wrong. Re-plan the chapter (usually the turn is missing or the POV has nothing to analyze).
4. **Keep a "don't touch" list** of the best lines. Revision often destroys the one great line in a paragraph, so protect them.

---

## 7. The two-minute quick audit

When there's no time for the full protocol (a short scene, a chat reply, a quick continuation), do these eight checks:

1. **Last line of each section**: is it a tilt?
2. **Search for** "couldn't help", "a mix of", "breath he didn't know", "something shifted", "hung in the air", "palpable", "testament". Delete all of them.
3. **Dialogue-only skim**: can you tell who's talking?
4. **One spiral present**: notice, question, doubt, verdict?
5. **One silence line** `"..."` where someone is stunned or refusing?
6. **Honorifics**: consistent with earlier text?
7. **Pure lines**: any paragraph with a quote plus other words? Split it.
8. **Dashes**: any `--` or `—` in narration that isn't a thought breaking off? Rewrite it.

---

## 8. Common failure patterns and their targeted fixes

| Symptom | Likely cause | Targeted fix |
|---|---|---|
| "It reads like a summary of a chapter" | Too much narration, not enough scene | Convert reported events into live dialogue stacks with separate action paragraphs; aim for ~50% dialogue |
| "It reads like Western literary fanfic" | Sentence inflation, dash asides, tagged dialogue (gates G2-G5) | See [MTL vs. Natural §7.1](mtl-vs-natural.md#71-the-four-symptoms-of-westernized-drift); split, de-dash, de-tag |
| "It hit the word count but feels padded" | Length reached by inflation | Undo the inflation; add beats per the length procedure (§3) |
| "Canon characters feel off" (fan fiction) | Default-cast traits or invented canon | Rebuild the canon sheet ([Fan Fiction & Canon](../adaptation/fanfic-and-canon.md)); remove anything uncertain |
| "It's choppy" | Clause-splitting without rhythm plan | Merge routine actions into flowing sentences; keep short lines for emphasis only |
| "It sounds like AI" | Tells from [Anti-Robotic](anti-robotic.md) plus abstraction | Lexicon sweep, then add four humanizing moves |
| "The characters sound the same" | Collapsed voices | Re-assign tics from [Character Voices](../dialogue/character-voices.md); read dialogue-only |
| "The protagonist is unlikable" | Cynicism without self-suspicion or warmth | Add self-doubt to spirals; add one moment of guilt or noticed kindness |
| "Nothing happens" | No turn | Find the moment the POV's read changes; if none exists, create a small asymmetry for him to notice |
| "Too melodramatic" | Earnest peak without ironic setup, or ornate peak prose | Simplify the prose at the peak; add ironic texture earlier in the chapter |
| "It's too Western" | Over-correction | Restore surnames, honorifics, SFX lines, silence lines, question chains |
| "The ending falls flat" | Summary ending | Replace the last paragraph with a line of dialogue, a sound, or a one-word verdict |

---

## 9. Final pre-delivery checklist

- [ ] Gates G1-G7 measured and passing (§2): dialogue 40-55%, narrative median ≤10, ≤5% long sentences, 0 mixed paragraphs, 0 dash asides, tics under caps, length met
- [ ] Pass 0: situation, turn, and hook identifiable
- [ ] Pass 1: sections numbered; every section tilts
- [ ] Pass 2: POV anchored; at least one full spiral; leitmotif present
- [ ] Pass 3: dialogue ~half; pure lines only; speakers identifiable; at least one dodge per scene
- [ ] Pass 4: rhythm counted; no monotone runs; long exhales present
- [ ] Pass 5: zero banned phrases in narration; humanizing moves present
- [ ] Pass 6: names, honorifics, and timeline consistent
- [ ] Pass 7: punctuation per house style
- [ ] Rubric ≥ 40/50, no axis < 3, evidence quoted
- [ ] Output is prose only: no preamble, no analysis, bible notes after `---` if any

---

## 10. Worked scoring example

After its first pass, a 3,200-word draft of "Chapter 4: Do You Like Family Restaurants? 1" was scored:

| Axis | Score | Evidence |
|---|---|---|
| Voice | 4 | Strong in §1-2 ("He'd ordered the hamburger because it couldn't be shared."), but §3 drifts into neutral summary |
| Inner monologue | 3 | Only one full spiral (the drink-bar scene). Other analysis is abstract ("He felt used.") |
| Rhythm & flow | 3 | §3 has a run of six 8-10 word sentences and no long exhale |
| Dialogue | 4 | Rin and Amamiya are distinct; Hina's lines are interchangeable with Momo's |
| Non-robotic texture | 3 | "a mix of irritation and amusement" and "hung in the air"; only two humanizing moves |
| Characterization | 4 | Rin's crack (the neat omelet slices) lands; Momo is flat |
| Structure | 4 | §1 and §2 tilt; §3 ends "He felt like he understood a little more." |
| Japanese texture | 4 | Honorifics consistent, drink bar, *Ding-dong*; no silence line |
| Emotional truth | 4 | The hamburger-alone moment works |
| Genre fit | 4 | Rom-com beats land, but the parfait-sharing gag isn't milked |
| **Total** | **37** | Below 40, so revise |

**Two lowest axes:** Inner monologue (3), plus a tie between Rhythm and Non-robotic (3). Inner monologue and Non-robotic were chosen, because both problems live in §3.

**Targeted rewrite of §3:**
- "He felt used." became a spiral. Amamiya's "*today* we've got Kuze" is noticed and quoted back, then comes three hypotheses about the word "today", then self-suspicion ("Or was he just looking for reasons to hate the guy?"), then the verdict: "Alibi. He was an alibi."
- "A mix of irritation and amusement" and "hung in the air" were deleted. A silence line and two humanizing moves were added (the drink bar's melon soda was flat, and he refilled it anyway, out of principle).
- The summary ending became: "Amamiya posted the photo at 9:42 p.m. Kuze's hamburger was in the corner of it."

**Rescore:** Inner monologue 5, Non-robotic 4, Rhythm 4 (the new spiral broke the monotone run), Structure 5. **Total 42.** Deliver.

## 10.5 Plant logistics (coherence check)

Planted clues are this voice's best payoffs: three burnt omelets in the bin, a hidden first batch in the fridge, a guarded "boring" pot. An independent reviewer caught a test chapter whose best plant was physically impossible. The girl had arrived with raw groceries while the POV watched the kitchen all evening, yet three of her failed omelets were already in his bin, still warm.

For every plant, answer three questions before delivering:
1. **When** did the character do it? Name the moment on the chapter's timeline.
2. **Where was the POV** at that moment, and why didn't he see it?
3. **Is it still in the state the text claims** (warm, wet, hidden) when it's found?

If any answer is "it can't have happened", move the plant earlier (she practiced at home and brought the evidence in her bag), or give the POV a reason to be out of the room.

**Keep a ledger of counts.** In the v2.2 tests, every model broke a count: a candy tray went from five to six to one while only one candy was eaten, the lead looked at *all four* of five girls, one burnt egg became twelve, and a group chat of 100 girlfriends messaged as 97. Before delivering, list every counted thing (people in the room, objects in a tray, items bought, minutes elapsed) and walk the chapter once, updating each count at every change. Any count that doesn't add up gets fixed.

## 11. Continuation-specific checks

When continuing someone else's text (or your own from an earlier session), add these to Pass 6:

1. **Voice match.** Compare the sentence-length profile of the last 500 words of the prior text with your first 500. Big shifts are visible seams.
2. **Tic continuity.** Every character tic in the prior text appears at least once, if that character appears.
3. **Open threads.** List the prior text's unanswered questions. Your chapter should touch at least one, even if only to deepen it.
4. **Leitmotif continuity.** Use the author's image ("the mire", "the sediment"), not a new one you prefer.
5. **Formatting continuity.** Match their section numeral style, chapter-title pattern, SFX style, and post format exactly.
6. **No retcons.** If you're unsure of a fact (whose seat is where, which club), keep it vague rather than invent a contradiction.

## 12. Revising user-supplied drafts

When the user asks you to revise *their* prose:
1. **Identify their voice first.** Keep their leitmotifs, jokes, and names. Your job is to make their book better, not to make it yours.
2. **Run Passes 4, 5, and 7 first.** They are the least invasive. Offer structural changes (Passes 1-2) only if asked, or flag them briefly after the prose.
3. **Preserve their best lines** verbatim by adding them to the don't-touch list.
4. **Deliver the revised prose**, then, only if useful, the most important changes in five bullets or fewer.
5. **Match their target.** If they want "more LN-like", push texture (Pass 2, Pass 3). If they want "less robotic", push Pass 5 and the humanizing moves. If they want "smoother", push Pass 4.

## 13. Pass-by-pass time budget

For a 3,500-word chapter, spend attention roughly like this:

| Pass | Share of revision effort | Why |
|---|---|---|
| Gates (§2) | before any pass | Measuring first stops you polishing a draft that has drifted |
| 0-1 Structure | 15% | Cheap to check, expensive to get wrong |
| 2 Voice/POV | 25% | The voice is the product |
| 3 Dialogue | 15% | Half the words |
| 4 Rhythm | 15% | Where "flow" is won or lost |
| 5 Anti-robotic | 20% | Where "human" is won or lost |
| 6-7 Consistency and polish | 10% | Mechanical, but readers notice errors |

## 14. Glossary of terms used in this file

- **Tilt:** a section's final beat that changes how the reader reads what came before (a reveal, arrival, reframe, silence, or verdict). See [Hooks & Cliffhangers](../structure/hooks-and-cliffhangers.md).
- **Spiral:** the analytical monologue sequence of notice, quote back, hypotheses, self-suspicion, verdict. See [Inner Monologue](../core/inner-monologue.md).
- **Long exhale:** a single flowing, clause-rich sentence placed after short beats to carry reflection. See [Rhythm & Flow](../core/rhythm-and-flow.md).
- **Silence line:** `"..."` as its own line of dialogue.
- **Humanizing move:** one of the twelve specific, petty, embodied details listed in [Anti-Robotic Prose §7](anti-robotic.md#7-the-humanizing-moves).
- **Crack in the image:** the contrast that complicates a character's reputation. See [Description & Portraits](../core/description-and-portraits.md).
- **Genre dials:** the voice adjustments each genre file specifies (comedy ratio, description density, POV habits). See [Genre Index](../genres/genre-index.md).

## 15. Budget rule

If you're short on budget, never skip the gates (§2) or Passes 2 and 5. A structurally imperfect chapter in a living voice beats a perfectly structured one that sounds like a machine, and a chapter that fails the gates isn't in the voice at all.
