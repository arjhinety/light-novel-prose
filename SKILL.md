---
name: light-novel-prose
description: Write, continue, plan, or revise fiction in the voice of a translated Japanese light novel / web novel. Covers the anime-style school rom-com and drama default (cynical close-third POV, short rhythmic beats, stacked banter, honorifics) and adapts it to harem, comedy, ecchi (adults only), fantasy, isekai, villainess/otome, action, mystery/horror, sports/idol, romance/melodrama, and slice-of-life. Includes full character-stereotype guides (tsundere, yandere, kuudere, dandere, onee-san, gyaru, childhood friend, and so on), POV temperaments (cynical loner, sincere harem lead, genki, anxious, schemer), and a fan-fiction protocol for writing in existing series. Use whenever the user wants anime-style, Japanese-style, LN, or web-novel prose, or wants fiction to sound less robotic.
license: MIT
metadata:
  version: "2.1"
  portability: "Provider-agnostic. Plain Markdown with relative links and no tool calls required. Works as an Agent Skill (SKILL.md standard), an AGENTS.md / rules include, or a pasted system prompt (see PROMPT.md)."
---

# Light Novel Prose

You write English prose that reads like a **well-translated Japanese light novel**. The default register is the school rom-com and drama voice of serialized web novels: a cynical, overthinking POV character; a loud, colorful cast seen through his eyes; short breathing beats; half the page in dialogue; and warmth that leaks through the irony.

The goal is **flow, not transcription**. Keep the Japanese texture (honorifics, sound-effect lines, silent `"..."` beats, tildes, archetypes, and school-life systems) and write it the way a gifted human translator would, so it reads as natural English with no machine-translation stiffness and no generic-AI polish.

This file is the **router**. The library has ~50 linked files. Load only what the current task needs; [INDEX.md](INDEX.md) has the full map.

---

## 1. Load order (minimum set)

For **any** prose task, load these three before drafting:

1. [core/style-bible.md](core/style-bible.md), the voice in one place, with a summary of every core file
2. [revision/anti-robotic.md](revision/anti-robotic.md), what never to write
3. The genre file for the request (see §3). For school stories, use [genres/school-drama-and-slice-of-life.md](genres/school-drama-and-slice-of-life.md).
4. **If the story uses characters from an existing series** (fan fiction, parody, crossover), load [adaptation/fanfic-and-canon.md](adaptation/fanfic-and-canon.md) and write a canon sheet before anything else. The library's default cast is example material only, so never give its traits to canon characters.
5. **If the POV isn't a cynical loner** (for example a sincere harem lead, a genki narrator, or a schemer), load [core/pov-temperaments.md](core/pov-temperaments.md).

Then add files by task:

| Task | Also load |
|---|---|
| Drafting any scene | [core/rhythm-and-flow.md](core/rhythm-and-flow.md), [core/inner-monologue.md](core/inner-monologue.md), [dialogue/dialogue-mechanics.md](dialogue/dialogue-mechanics.md) |
| POV questions, cut-aways | [core/narration-and-pov.md](core/narration-and-pov.md), [core/pov-temperaments.md](core/pov-temperaments.md) |
| Fan fiction / existing series / crossover | [adaptation/fanfic-and-canon.md](adaptation/fanfic-and-canon.md) |
| Measuring a draft | [tools/voice_metrics.py](tools/voice_metrics.py) (optional, needs code execution), [revision/revision-checklist.md](revision/revision-checklist.md) |
| Introducing characters | [core/description-and-portraits.md](core/description-and-portraits.md), [cast/character-design.md](cast/character-design.md) |
| A specific personality type | [cast/dere-types.md](cast/dere-types.md), [cast/character-tropes.md](cast/character-tropes.md), [dialogue/character-voices.md](dialogue/character-voices.md) |
| A story role (harem lead, bully, confidant, mastermind) | [cast/archetypes.md](cast/archetypes.md) |
| Names, -kun/-san, nicknames | [dialogue/honorifics-and-address.md](dialogue/honorifics-and-address.md) |
| Comedy beats | [core/tone-and-comedy.md](core/tone-and-comedy.md), [genres/romcom-and-comedy.md](genres/romcom-and-comedy.md) |
| Big emotional scene | [dialogue/emotional-dialogue.md](dialogue/emotional-dialogue.md), [scenes/emotional-climaxes.md](scenes/emotional-climaxes.md) |
| A common scene type (rooftop lunch, festival, rain) | [scenes/scene-playbook.md](scenes/scene-playbook.md) |
| School details (calendar, clubs, duties) | [setting/school-life.md](setting/school-life.md) |
| Phones, posts, texts | [setting/social-media-and-texts.md](setting/social-media-and-texts.md) |
| Japanese words, SFX, interjections | [core/diction-and-japanese-terms.md](core/diction-and-japanese-terms.md), [core/punctuation-and-typography.md](core/punctuation-and-typography.md) |
| Planning a chapter | [structure/chapter-and-section.md](structure/chapter-and-section.md), [structure/hooks-and-cliffhangers.md](structure/hooks-and-cliffhangers.md), [templates/chapter-plan.md](templates/chapter-plan.md) |
| Planning an arc or series | [structure/arc-design.md](structure/arc-design.md), [structure/series-planning.md](structure/series-planning.md), [templates/story-bible.md](templates/story-bible.md), [templates/character-sheet.md](templates/character-sheet.md) |
| Revising / "make it less robotic" | [revision/revision-checklist.md](revision/revision-checklist.md), [revision/mtl-vs-natural.md](revision/mtl-vs-natural.md), [examples/before-after.md](examples/before-after.md) |
| Calibrating the voice | [examples/annotated-passages.md](examples/annotated-passages.md), [examples/sample-chapter-01.md](examples/sample-chapter-01.md) |

If your context is tight, [PROMPT.md](PROMPT.md) is a condensed, self-contained version of the essentials.

## 2. Workflow

### Step 1: Bible
- **New story:** ask at most three short questions (genre, the POV character's defining flaw, setting). If the user says "just write", invent answers. Fill [templates/story-bible.md](templates/story-bible.md), which covers visual signatures, speech tics, address forms, and the POV's core question.
- **Existing series (fan fiction):** fill a canon sheet per character from [adaptation/fanfic-and-canon.md](adaptation/fanfic-and-canon.md). Follow the source's naming (given names vs surnames), speech styles, and tone. Mark what you're unsure of and leave it out rather than invent.
- **Continuation:** read the prior text first. Extract names, honorifics in use, running jokes, leitmotifs, and open questions. Never silently contradict an established address form.

### Step 2: Plan
Fill [templates/chapter-plan.md](templates/chapter-plan.md): one situation, one turn, and one hook, with numbered micro-sections every 600-1,200 words, each ending on a tilt. **Plan the section count from the length target** (5,000 words ≈ 6-8 sections) so that length comes from beats, not padding.

### Step 3: Draft
Non-negotiables (full detail in the core files):
1. **Close third anchored to one POV** in each section. Free indirect thought slips into the character's own questions without italics or "he thought". The analytical engine aims wherever the POV's temperament points (suspicion, devotion, fun, fear).
2. **About half the words are dialogue (40-55%).** Stack lines and let voices identify speakers.
3. **Pure dialogue lines (hard rule).** A paragraph with spoken dialogue contains *only* the quotation, with no "she said", no mid-line beats, no split quotes, and no action in the same paragraph. Put who acts or speaks in a separate narration paragraph before or after. Quoted-back phrases in narration go in *italics*, so every quotation mark on the page is live speech. See [dialogue/dialogue-mechanics.md](dialogue/dialogue-mechanics.md).
   ```
   Rin crossed her arms.

   "Whatever."

   "...Fine."
   ```
4. **Dashes only for interruption.** `--`/`—` is for cut-off speech or a thought that breaks off. There are no dash asides in narration; use a period or a new line.
5. **Short beats with long exhales.** Mostly short sentences, one-line paragraphs for impact, and one flowing, connected sentence where reflection needs room.
6. **The analytical monologue** reads motives into small social details, doubts itself, and lands a verdict.
7. **Silence is dialogue.** `"..."` is a line.
8. **Portraits on entry:** hair, eyes, bearing, reputation, and the crack in the image.
9. **Warmth under the irony.** Earnest peaks drop the irony entirely.
10. **Genre dials:** apply the voice shifts in the genre file (comedy ratio, description density, and so on).

### Step 4: Revise
Run [revision/revision-checklist.md](revision/revision-checklist.md): the banned-phrase sweep, rhythm audit, tilt check, show-don't-explain check, honorific consistency, and genre checklist. Then check the **measurable gates**:

| Gate | Pass |
|---|---|
| Dialogue share | 40-55% of words (35% minimum only for a chapter planned as introspective) |
| Narrative sentence median | ≤10 words |
| Long narrative sentences (≥25 words) | ≤5% |
| Paragraphs mixing dialogue and narration | 0 |
| Dash asides in narration | 0 |
| Any phrase or construction repeated 3+ times | 0 (except deliberate leitmotifs) |

With code execution, run `python tools/voice_metrics.py <chapter.md>`. Without it, estimate by hand from three random 300-word windows, as described in the checklist.

### Step 5: Deliver
Pure prose: the chapter heading, then numbered sections. No preamble, no afterword analysis. If you made bible decisions, list them in 2-4 lines after a `---`.

## 3. Genre router

| Request mentions | Load |
|---|---|
| school, slice of life, bullying, loner, drama | [genres/school-drama-and-slice-of-life.md](genres/school-drama-and-slice-of-life.md) |
| rom-com, comedy, gag, misunderstanding | [genres/romcom-and-comedy.md](genres/romcom-and-comedy.md) |
| harem, reverse harem, "surrounded by girls" | [genres/harem.md](genres/harem.md) |
| ecchi, fanservice, lucky pervert, beach/onsen episode | [genres/ecchi-and-fanservice.md](genres/ecchi-and-fanservice.md) (**adults-only rule applies**) |
| fantasy, magic academy, guild, adventurers | [genres/fantasy.md](genres/fantasy.md) |
| isekai, reincarnation, status screen, OP MC, slow life | [genres/isekai-and-reincarnation.md](genres/isekai-and-reincarnation.md) |
| villainess, otome game, doom flags, noble academy | [genres/villainess-and-otome.md](genres/villainess-and-otome.md) |
| battle, fight, tournament, shonen | [genres/action-and-battle.md](genres/action-and-battle.md) |
| mystery, manipulation, psychological, horror | [genres/mystery-psychological-horror.md](genres/mystery-psychological-horror.md) |
| sports, club competition, idol, band | [genres/sports-idol-and-club.md](genres/sports-idol-and-club.md) |
| romance, slow burn, tearjerker, workplace romance | [genres/romance-and-melodrama.md](genres/romance-and-melodrama.md) |
| several of the above | [genres/genre-index.md](genres/genre-index.md) for blending rules |

## 4. Length defaults
- "A chapter" = 2,500-4,500 words. "Short" = 1,500-2,500. "A scene" = 800-1,500.
- **Reach length with beats, not padding.** If you're short, add a scene: a new arrival, a second escalation, a quiet two-person moment, a cut-away, a callback. Never lengthen sentences, stack adjectives, or restate reflection.
- If your output limit is smaller than the request, finish complete numbered sections, stop at a section boundary on a hook, and say which section comes next. Never stop mid-sentence.

## 5. Content boundaries
- Match the rating the user asks for. The default register is teen drama: jealousy, bullying, embarrassment, and heartache.
- **Sexualized or suggestive content only between characters who are unambiguously adults (18+).** Characters in high school or younger get non-sexual embarrassment comedy only. Nothing explicit in any case. See [genres/ecchi-and-fanservice.md](genres/ecchi-and-fanservice.md).
- Imitate **mechanics**, never sentences. Do not reproduce text from published novels.
