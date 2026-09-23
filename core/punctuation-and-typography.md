# Punctuation & Typography

> **Purpose:** The house style for light-novel punctuation and page layout (ellipses, dashes, tildes, stutters, unison quotes, section numerals, emphasis, and post formatting), with the reasoning behind each mark so it is used as rhythm, not decoration.
> **Load when:** Formatting any draft, writing dialogue with hesitation or interruption, laying out chapter sections or in-world posts, or cleaning up a draft whose punctuation is either flat-Western or overloaded with marks.
> **Related:** [Style Bible](style-bible.md), [Rhythm & Flow](rhythm-and-flow.md), [Diction & Japanese Terms](diction-and-japanese-terms.md), [Dialogue Mechanics](../dialogue/dialogue-mechanics.md), [Emotional Dialogue](../dialogue/emotional-dialogue.md), [Chapter & Section](../structure/chapter-and-section.md), [Social Media & Texts](../setting/social-media-and-texts.md), [Revision Checklist](../revision/revision-checklist.md)

---

## 1. Why punctuation matters more here

Light-novel prose is **heard** more than read. Its short beats, silences, drawls, and interruptions are carried by punctuation the way a manga carries them with speech-bubble shapes and panel gutters. Get the marks right and the dialogue sounds like voices. Get them wrong and it sounds like a script.

Two dangers:
- **Under-marking**: Western-standard punctuation only, so hesitations become commas and silences become "He said nothing." It sounds flat and generic.
- **Over-marking**: tildes on every line, stutters in every sentence, `?!!` everywhere. It sounds like a parody of fan translation.

The measured source uses roughly: 4 silent `"..."` lines per chapter, 3 `--` per chapter, 1-2 `~` per chapter, and stutters only at genuine fluster. Use that as your density band.

## 2. The ellipsis family

### 2.1 `"..."`: the silent line

A line of dialogue that is **only** an ellipsis means *this character is present, has the floor, and says nothing*. It is one of the voice's most important tools.

> "You like her, don't you, Mina?"
> "..."
> "Thought so."

Uses:
| Use | Effect |
|---|---|
| Refusal to answer | Stubbornness, guilt |
| Speechlessness | Shock, awe |
| Judgment | The POV is silently evaluating |
| Grief | At climaxes, often repeated |
| Comic | Deadpan non-response to absurdity |

Rules:
1. **Always three periods, no spaces**: `"..."`. Not `". . ."`, not `"…"` mixed with `...` (pick one glyph and use it everywhere; this library uses three periods).
2. **Attribution is usually unnecessary.** The reader knows whose turn it is. If you must attribute, do it with a gesture on the next line: "Kuze looked away."
3. **The narration can follow a silent line to interpret it**, in its own paragraph, and the interpretation should be *the POV's guess*, not the author's:

   > "..."
   >
   > Was she angry? Or just tired?
4. **The silence duet** (one character talks at length and the other answers `"..."` five or six times) is reserved for the confidant thesis speech or a confession. See [Emotional Dialogue](../dialogue/emotional-dialogue.md).
5. **Narrative-line silence**: a narration paragraph consisting only of `...` is *not* used. Silence is always a character's line.

### 2.2 `...` inside speech: hesitation and trailing off

> "Well... um... it's not like... okay, fine."
> "I thought that maybe..."

Rules:
1. **No space before, one space after** when the sentence continues: `"Well... um..."`
2. **Leading ellipsis** for a line that starts after a pause: `"...Tch."` / `"...Yeah."` This is extremely common and very effective for reluctant replies.
3. **Trailing ellipsis** for a line that fades: `"I just..."`
4. **Mid-word ellipsis** for a breaking voice: `"Dam... n..."`
5. **Density**: at most two ellipses in a single line unless the character is a dandere or panicking. Three-plus is for a specific effect.

### 2.3 Ellipsis in narration

Use it rarely, and only in free indirect thought when the POV's thinking trails off:

> Why would Kujou, of all people... no. Not worth thinking about.

## 3. The dash

This library writes `--` (a double hyphen) in its examples, matching web-novel convention and staying typeable. The em dash (`—`) is equally correct. **Pick one per story and never mix them.**

**The dash rule (R2).** In story prose, a dash has exactly three jobs:

1. **Speech cut off or interrupted** (§3.1, §3.2)
2. **A thought that breaks off** in narration: `Why would Kujou, of all people--`
3. **A structural stamp** that opens a scene or holds a breath: `The next day--` (§3.3)

It is **never** used for narrative asides, appositives, or dramatic pauses in the middle of a narration sentence. That habit (`He had one rule--never volunteer--and he'd broken it.`) is a Western-literary tic, and it is one of the fastest ways a draft stops sounding like a translated LN. Test runs of this library found models producing 40-50 aside dashes per 5,000 words when this rule wasn't explicit. Target: **close to zero dashes in narration** outside the three jobs above. Replace an aside dash with a period, a comma, or a new one-line paragraph (§3.5).

### 3.1 Interruption

The speaker is cut off by someone else or by an event:

> "Hey, Tachibana, I wanted to ask--"
> "Kuze-kun! There you are!"

Rules:
1. The dash goes **inside** the closing quote.
2. The interrupting line follows immediately. There's no need for "she interrupted".
3. The interrupted character can finish later, and the callback is satisfying.

### 3.2 Calling out a name

A name shouted across distance takes a dash-plus-exclamation:

> "Kuze--!"

It feels like a voice cutting through a hallway. Use it for sudden arrivals.

### 3.3 Narrative cut / time stamp

A dash at the end of a narrative fragment marks a scene jump or a held breath:

> After school--
> The next day--
> May, second year of high school--
> Their eyes met--

Rules:
1. Stamps stand alone as a paragraph.
2. "Their eyes met--" style dashes create a suspended moment. The next paragraph must deliver.

### 3.4 Narration interrupted by dialogue

**Wrong** (narration and speech share a paragraph, which breaks R1 as well):

> He was about to say it-- "Everyone, next stop!" --when Momo's voice cut through.

Never do this. Break it into separate paragraphs instead:

> He was about to say it--
>
> "Everyone, next stop!"
>
> Momo's voice cut through before he could.

### 3.5 Parenthetical and aside dashes: not used

Standard Western use in narration (a pair of dashes around an aside, or a single dash before an appositive or punchline) is **not part of this voice** (R2). The LN rhythm prefers a new sentence, or a new paragraph, to a nested one.

| Aside dash (don't) | LN fix (do) |
|---|---|
| The one thing he'd never considered--that she might actually be lonely--hit him all at once. | He'd never once considered it. That she might actually be lonely. It hit him all at once. |
| Amamiya had one gift--timing. | Amamiya had one gift. Timing. |
| She smiled--the careful kind, with scaffolding behind it. | She smiled. The careful kind, with scaffolding behind it. |
| He took the stairs two at a time--past the poster, past the window--and didn't slow down. | He took the stairs two at a time. Past the poster. Past the window. He didn't slow down. |

Notice that each fix *adds* rhythm: the aside becomes its own short beat, which is exactly the short-beat texture the voice runs on (see [Rhythm & Flow](rhythm-and-flow.md)). A dash hides a beat inside a sentence, and the LN voice wants it out in the open.

## 4. The tilde `~`

The tilde marks a **drawn-out, sing-song, teasing, or cutesy** vowel, like a wavy speech-bubble tail.

> "Hey there~"
> "Kuze-kun's so mean~"
> "Hachi-chan~ Why'd you skip yesterday~?"

### 4.1 Who uses it

| Character type | Tilde use |
|---|---|
| Genki (Hina) | Occasional, for calling out and cheer |
| Airhead / two-faced (Momo) | Frequent, as a sugary performance |
| Bully queen (Hoshino) | Frequent, and **menacing**. The tilde becomes mockery |
| Onee-san / teasing senpai | Frequent, for teasing |
| Tsundere (Rin) | Almost never |
| Ojou (Kujou) | Never |
| Cynical POV (Kuze) | Never, unless mocking someone |
| Harem lead (Amamiya) | Rarely, when whining |

The tilde's menace in a bully's mouth is one of the best effects in the voice. The same mark that makes Hina cute makes Hoshino terrifying, because the cheerfulness is weaponized.

### 4.2 Rules

1. **Placement:** directly after the drawn word, before any punctuation: `"So cute~!"`, `"Right~?"`.
2. **Doubling** (`~~`) for extreme drawl: `"Totally~~"`. This is rare.
3. **Unison drawl:** `"""Totally~~~"""` for a clique agreeing.
4. **Never in narration.**
5. **Stretched letters** can substitute: "Fiiine." / "Sooo cute." Use them for emphasis without the sing-song tone.

## 5. Stutters

A stutter is **the first letter (or syllable) repeated with a hyphen**, signaling fluster, fear, or embarrassment:

> "W-Wait!"
> "I-It's not like that!"
> "Th-that's..."
> "S-Sorry!"

Rules:
1. **Capitalization:** capitalize both parts at the start of a line (`W-Wait`), both lowercase mid-line (`it's n-not`). Pick one convention for mid-line stutters and keep it.
2. **Stutter on the first word, rarely more than one per line.** `"W-w-w-what?!"` is a comic extreme. Use it once a book.
3. **Stutters are emotional evidence.** The narrator can note them: *She stuttered. So it did bother her.*
4. **Characters with default composure never stutter** unless something is seriously wrong. The first time Kujou stutters is a plot event.
5. **Consonant clusters:** stutter the natural sound: "Th-that", "Sh-shut up", "Wh-what".

## 6. `?!` and `!?`: shock marks

> "You're in the go-home club?!"
> "Eh?! Since when?!"

Rules:
1. **`?!` is the house order** (question first). The source mixes them. You should pick one.
2. **Dialogue only.** Never in narration.
3. **Double exclamations (`!!`)** only in comic peaks. `?!!` never.
4. A line of pure shock can be only the mark with a sound: `"Eh?!"`

## 7. Unison dialogue: triple quotes

When **multiple characters say the same thing at the same time**, enclose it in triple quotes:

> """Guess so."""
> """Totally~~~"""
> """Say it, say it, say it~"""

Two characters in unison use double quotes of quotes:

> ""So gross...""

Rules:
1. Reserve it for crowds, cliques, and pairs in comic sync.
2. At climaxes, a chanting crowd in triple quotes, repeated and intercut with the POV's one-line thoughts, is a strong effect. See [Emotional Dialogue](../dialogue/emotional-dialogue.md).
3. Never use it for a single speaker.
4. If the target platform mangles triple quotes, fall back to a narration paragraph (`The boys answered together.`) followed by the line on its own (`"Guess so."`). Never glue the chorus tag onto the quote (R1). Do this consistently.

## 8. Emphasis

1. **Italics** for stressed words in dialogue (*"I* didn't say that.") and, sparingly, for a remembered line of dialogue in narration.
2. **Free indirect thought is NOT italicized.** This is the key difference from Western genre fiction. The POV's thoughts flow as plain text: `Why was he like this?` Italics only for direct, quoted thought when you need to separate it sharply, and even then prefer plain text. One permitted house option: italicize **first-person, present-tense** thoughts (*What exactly is so special about him?*) and leave third-person free indirect thought plain. If you choose it, apply it consistently for the whole story, as the [sample chapters](../examples/sample-chapter-01.md) do (see also [Narration & POV](narration-and-pov.md)).
3. **No bold** in prose. (Bold is for the status windows and headers of game-system genres; see [Isekai & Reincarnation](../genres/isekai-and-reincarnation.md).)
4. **ALL CAPS** only for a comic scream: `"CUUUUT!"` Once a chapter at most.
5. **Quoted terms, scare quotes, and quoted-back phrases in narration** use *italics* (or single quotes if italics can't render): the *go-home club*, his *rational* choice, *I got them to make up*. **Never double quotes**, because double quotes are reserved for live speech (R1, §9.1). Scare-quote italics still carry the POV's irony.

## 9. Quotation marks

1. **Double quotes for speech.** Single quotes only for quotes within quotes: `"She said, 'Don't come.'"`
2. **Straight or curly, but consistent.** Web-novel output uses straight quotes (`"`). Typeset books use curly. Do not mix.
3. **Consecutive speakers on one line.** The source often runs multiple speakers' lines into one paragraph. **Don't.** One speaker per paragraph is the modern standard and is far easier to read. (It is an MTL/formatting artifact. See [MTL vs. Natural](../revision/mtl-vs-natural.md).)

   Wrong:
   > "Morning!" "You're late." "Sorry, sorry."

   Right:
   > "Morning!"
   > "You're late."
   > "Sorry, sorry."

   **No exception for group chatter.** Even when individual speakers don't matter, each line gets its own paragraph. If you want to signal overlap, put a narration paragraph first (`Voices overlapped.`) and then stack the lines.

### 9.1 Pure dialogue lines (R1)

**This is a hard rule.** A paragraph that contains spoken dialogue contains **only the quotation**:

- no speech tags (`she said`, `he asked`, `Rin whispered`)
- no action beats in the same paragraph (`Rin crossed her arms. "Whatever."`)
- no split quotes (`"Oh yeah," she paused, "so like, this is the problem."`)
- no narration before or after the quote in the same paragraph

**Wrong:**

```
"Oh yeah," she paused, "so like, this is the problem."
Rin crossed her arms. "Whatever."
"Fine," Kuze said.
```

**Right:**

```
Rin crossed her arms.

"Whatever."

"...Fine."
```

How attribution works without tags:

1. **Voice and tics.** Rin says *Tch* and calls him *you*, Hina says *Yup!*, and Kujou says *My.* A reader who knows the cast knows who's talking. This is why every character needs distinct tics ([Character Voices](../dialogue/character-voices.md)).
2. **A narration paragraph just before.** The speaker acts, and then the line comes in its own paragraph. The reader assigns the line to the last person who moved.
3. **A narration paragraph just after.** The line lands first, and the next paragraph shows who said it through a reaction or gesture.
4. **Several sentences from one speaker go in one quote.** Don't break a speaker's continuous speech into separate quoted paragraphs unless there's a silence between them.

Everything that isn't live speech stays out of double quotes: quoted-back phrases, scare quotes, and remembered words go in *italics* (§8, rule 5), and in-world text (phone text-to-speech, messages, posts, signs) uses its own block layout (§12). The result is a page where **every double quotation mark means someone is talking right now**, which is the visual rhythm of a translated LN: speech and narration alternate as separate bubbles and captions.

Why the rule exists: it keeps dialogue reading like manga speech bubbles, it forces the writer to make voices distinct instead of leaning on tags, and it eliminates the most Western-looking line shape in English prose. Test runs showed models writing 70-100 mixed paragraphs per 5,000 words when this wasn't stated as a rule. The full treatment, with many examples, is in [Dialogue Mechanics](../dialogue/dialogue-mechanics.md).

*Scope:* the rule governs story prose and example passages. Documentation prose (tables, bullets, analysis) may quote lines inline.

## 10. Section numerals and scene breaks

### 10.1 Numbered micro-sections

Inside a chapter, sections are marked with a **bare numeral on its own line**:

```
...and the bell rang.

2

The family restaurant was...
```

- Start at `1` (the first section may be left unnumbered if the chapter heading directly precedes it. Pick one convention).
- Numerals are plain and unpunctuated, with no "Part", "§", or "#".
- Numbering restarts every chapter. See [Chapter & Section](../structure/chapter-and-section.md).

### 10.2 Soft scene breaks

For a time skip *within* a section, use a blank line followed by a time stamp with a dash, or a centered `* * *`:

```
He left without saying goodbye.

* * *

After school--
```

Don't use both numerals and asterisks for the same kind of break. Numerals mark sections, and asterisks mark in-section skips.

### 10.3 POV cut-aways

A cut-away to another character's POV gets its own section numeral or an asterisk break, and **the first sentence must name the new POV character** so the reader re-anchors immediately:

> * * *
>
> In her room, Kujou uncapped a red pen.

See [Narration & POV](narration-and-pov.md).

## 11. Chapter headings

```
Chapter 7: Do You Like Class Duty? 2
```

- "Chapter N:" then the title. Arc-series titles carry a part number with no "Part" word (see [Chapter & Section](../structure/chapter-and-section.md)).
- In Markdown output, use a `#` or `##` heading consistently, or plain text if the user's platform strips Markdown.

## 12. In-world post and message formatting

Posts, texts, and call transcripts get their own layout. Full treatment is in [Social Media & Texts](../setting/social-media-and-texts.md). The typography rules:

```
Haruto
Grabbed food with Rin and Kuze today. Looked like they weren't getting along, so I helped them make up.
(Tap to view photo)

    Momo
    Haruto you're such a good guy~

    Hina
    Wait you went without me?!
```

1. Username on its own line, text on the next line. **No quotation marks.**
2. `(Tap to view photo)` in parentheses on its own line.
3. Replies indented (4 spaces or a blockquote) to show threading.
4. Chat messages use `Name: text` or a right/left description. Pick one per book.
5. After a post block, return to prose with the POV's reaction, usually `"..."` first.

## 13. Numbers, times, and units

- Spell out numbers under one hundred in narration ("five girls", "second year"). Use numerals for clock times, room numbers, class names, and prices ("Class 2-3", "4:30", "1,000 yen").
- "Yen" stays as yen. Don't convert currency.
- Metric units, since this is Japan: "a few meters", "thirty degrees".
- Grade years: "second-year" (adjective) / "second year" (noun). "Class 2-3" for homerooms.

## 14. Common punctuation failures

| Failure | Example | Fix |
|---|---|---|
| Silence as narration | `He said nothing.` (every time) | `"..."` as a line |
| Tilde spam | Every girl's every line ends in `~` | Only drawl characters, only drawled words |
| Stutter spam | `"I-I-I d-don't k-know"` | One stutter, on the first word |
| Western tags on everything | `"No," he said. "Why?" she asked.` | Untagged stacks, with gestures in their own paragraphs (R1) |
| Narration glued to a quote | `Rin crossed her arms. "Whatever."` | Two paragraphs: the gesture, then the line (R1) |
| Split quote with beat | `"Oh," she paused, "so..."` | `"Oh... so..."` with the pause inside the speech (R1) |
| Aside dashes in narration | `He had one rule--never volunteer--and broke it.` | `He had one rule. Never volunteer. He broke it.` (R2) |
| Double-quoted scare terms | his "rational" choice | his *rational* choice |
| Italicized thoughts | *Why is he like this?* he thought. | Plain free indirect: Why was he like this? |
| Mixed dashes | `--` here, `—` there | Pick one |
| Multiple speakers per paragraph | `"A." "B." "C."` | One per paragraph |
| `?!!!` | `"What?!!!"` | `"What?!"` |
| Footnotes / T/N | `(T/N: bento is a lunch box)` | In-world context |
| Semicolon-heavy narration | `He left; she stayed; the bell rang.` | Short separate sentences |

## 15. Punctuation as rhythm: a before/after

Flat punctuation (and an R1 violation):
> "I wasn't waiting for you," Rin said, embarrassed. Kuze didn't reply. "I said I wasn't waiting," she repeated, hesitating. "Well, maybe for a little while. But not for you specifically."

LN punctuation:
> "I-I wasn't waiting for you."
> "..."
> "I *said* I wasn't waiting!"
> "..."
> "...Okay, maybe a little. But not for *you*. For... the bus."
> "There's no bus stop here."
> "Shut up!"

What changed: the stutter carries "embarrassed", the silent lines carry "didn't reply", the leading ellipsis carries "hesitating", the italics carry stress, and one speaker per line, with no tags glued on, lets the rhythm breathe. No emotion word survived, and none was needed.

## 16. Checklist

- [ ] Silent lines are written as `"..."`, about 3-5 per chapter.
- [ ] Hesitation ellipses are inside speech, with leading `...` for reluctant replies.
- [ ] Dashes (`--` or `—`, one style per story) only for interruptions, broken-off thoughts, and scene stamps. Zero aside dashes in narration (R2).
- [ ] Every paragraph with double quotes contains only the quotation: no tags, no beats, no split quotes (R1).
- [ ] Quoted-back phrases and scare terms in narration are in italics, not double quotes.
- [ ] Tildes only from drawl characters, and menacing in the bully's mouth.
- [ ] Stutters only at genuine fluster, first word only.
- [ ] `?!` in dialogue only, in one consistent order.
- [ ] Triple quotes only for true unison.
- [ ] Free indirect thought is not italicized.
- [ ] One speaker per paragraph.
- [ ] Section numerals are bare on their own lines, and POV cut-aways name the new POV in the first sentence.
- [ ] Post blocks are formatted per the social media spec.

For the rhythm these marks create, see [Rhythm & Flow](rhythm-and-flow.md). For the whole-draft pass, see [Revision Checklist](../revision/revision-checklist.md).
