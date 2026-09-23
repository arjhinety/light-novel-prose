---
name: light-novel-prose
description: Write, continue, plan, or revise fiction in the voice of a translated Japanese light novel / web novel. Covers the anime-style school rom-com and drama default (cynical close-third POV, short rhythmic beats, stacked banter, honorifics) and adapts it to harem, comedy, ecchi (adults only), fantasy, isekai, villainess/otome, action, mystery/horror, sports/idol, romance/melodrama, and slice-of-life. Includes full character-stereotype guides (tsundere, yandere, kuudere, dandere, onee-san, gyaru, childhood friend, and so on). Use whenever the user wants anime-style, Japanese-style, LN, or web-novel prose, or wants fiction to sound less robotic.
license: MIT
metadata:
  version: "2.0"
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

Then add files by task:

| Task | Also load |
|---|---|
| Drafting any scene | [core/rhythm-and-flow.md](core/rhythm-and-flow.md), [core/inner-monologue.md](core/inner-monologue.md), [dialogue/dialogue-mechanics.md](dialogue/dialogue-mechanics.md) |
| POV questions, cut-aways | [core/narration-and-pov.md](core/narration-and-pov.md) |
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
- **Continuation:** read the prior text first. Extract names, honorifics in use, running jokes, leitmotifs, and open questions. Never silently contradict an established address form.

### Step 2: Plan
Fill [templates/chapter-plan.md](templates/chapter-plan.md): one situation, one turn, and one hook, with numbered micro-sections every 600-1,200 words, each ending on a tilt.

### Step 3: Draft
Non-negotiables (full detail in the core files):
1. **Close third anchored to one POV** in each section. Free indirect thought slips into the character's own questions without italics or "he thought".
2. **About half the words are dialogue.** Stack lines, tag with action, and let voices identify speakers.
3. **Short beats with long exhales.** Mostly short sentences, one-line paragraphs for impact, and one flowing, connected sentence where reflection needs room.
4. **The analytical monologue** reads motives into small social details, doubts itself, and lands a verdict.
5. **Silence is dialogue.** `"..."` is a line.
6. **Portraits on entry:** hair, eyes, bearing, reputation, and the crack in the image.
7. **Warmth under the irony.** Earnest peaks drop the irony entirely.
8. **Genre dials:** apply the voice shifts in the genre file (comedy ratio, description density, and so on).

### Step 4: Revise
Run [revision/revision-checklist.md](revision/revision-checklist.md): the banned-phrase sweep, rhythm audit, tilt check, show-don't-explain check, honorific consistency, and genre checklist.

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
- If your output limit is smaller than the request, finish complete numbered sections, stop at a section boundary on a hook, and say which section comes next. Never stop mid-sentence.

## 5. Content boundaries
- Match the rating the user asks for. The default register is teen drama: jealousy, bullying, embarrassment, and heartache.
- **Sexualized or suggestive content only between characters who are unambiguously adults (18+).** Characters in high school or younger get non-sexual embarrassment comedy only. Nothing explicit in any case. See [genres/ecchi-and-fanservice.md](genres/ecchi-and-fanservice.md).
- Imitate **mechanics**, never sentences. Do not reproduce text from published novels.
