# Index

> **Purpose:** a map of every file in the library, how the files depend on each other, and reading paths for common tasks.
> **Load when:** you need to find the right file, or you're orienting yourself in the library for the first time.
> **Related:** [SKILL.md](SKILL.md), [PROMPT.md](PROMPT.md), [README.md](README.md)

## 1. How the library is layered

```
                ┌──────────────────────────┐
                │ SKILL.md (router)        │
                └────────────┬─────────────┘
          ┌──────────────────┼────────────────────┐
          ▼                  ▼                    ▼
   core/ (the voice)   genres/ (voice dials)   revision/ (quality gate)
          │                  │                    │
    ┌─────┴──────┐     ┌─────┴─────┐              │
    ▼            ▼     ▼           ▼              ▼
 dialogue/    cast/  setting/   scenes/     examples/ (calibration)
          \      |      |      /
           ▼     ▼      ▼     ▼
          structure/ + templates/ (planning)
```

- **core/** defines *how sentences and paragraphs sound*. Everything else assumes it.
- **genres/** says *which dials to turn* (comedy ratio, description density, and POV habits) for a given genre, and adds genre tropes.
- **dialogue/** and **cast/** define *who talks and how*.
- **setting/** and **scenes/** supply *material*, meaning where stories happen and repeatable scene recipes.
- **structure/** and **templates/** handle *planning* at the chapter, arc, and series levels.
- **revision/** is the *quality gate* every draft passes through.
- **examples/** show the result, for calibration.

## 2. Every file

### Root
| File | What it covers |
|---|---|
| [SKILL.md](SKILL.md) | Entry point: load order, workflow, genre router, length defaults, content boundaries |
| [INDEX.md](INDEX.md) | This map |
| [PROMPT.md](PROMPT.md) | Condensed standalone system prompt for environments that can't load multiple files |
| [README.md](README.md) | Installation per provider/tool, layout, provenance |

### core/: the voice
| File | What it covers |
|---|---|
| [core/style-bible.md](core/style-bible.md) | Master overview: the measured voice profile and a summary of every core technique |
| [core/narration-and-pov.md](core/narration-and-pov.md) | Close third, surname anchoring, free indirect thought, omniscient cut-aways, POV switching |
| [core/inner-monologue.md](core/inner-monologue.md) | The analytical engine: asymmetries, quoting back, hypothesis chains, self-suspicion, verdicts, leitmotifs |
| [core/rhythm-and-flow.md](core/rhythm-and-flow.md) | Sentence-length bands, one-line paragraphs, spirals, the long exhale, connective tissue, SFX lines |
| [core/description-and-portraits.md](core/description-and-portraits.md) | The portrait formula, anime expression shorthand, scenery economy, body-language tags |
| [core/tone-and-comedy.md](core/tone-and-comedy.md) | Cynical-not-cruel, deadpan, underreaction, meta rom-com awareness, earnest peaks, running gags |
| [core/diction-and-japanese-terms.md](core/diction-and-japanese-terms.md) | Register rules and a large glossary: keep, translate, or avoid |
| [core/punctuation-and-typography.md](core/punctuation-and-typography.md) | `"..."`, `--`, `~`, stutters, `?!`, unison quotes, section numerals, post formatting |

### dialogue/
| File | What it covers |
|---|---|
| [dialogue/dialogue-mechanics.md](dialogue/dialogue-mechanics.md) | Stacking, action tags, group chatter, silent replies, interruptions, banter |
| [dialogue/honorifics-and-address.md](dialogue/honorifics-and-address.md) | The honorific system, name escalation as plot, the consistency ledger |
| [dialogue/character-voices.md](dialogue/character-voices.md) | Speech patterns per archetype, tic design, sample lines |
| [dialogue/emotional-dialogue.md](dialogue/emotional-dialogue.md) | Outbursts, confessions, breakdowns, the monologue-and-silence duet, chants |

### cast/
| File | What it covers |
|---|---|
| [cast/archetypes.md](cast/archetypes.md) | Story roles: loner POVs, the harem lead, rivals, bullies, confidants, teachers, masterminds |
| [cast/character-design.md](cast/character-design.md) | Visual signature, tic, contradiction, secret, arc, relationship web, public vs. private face |
| [cast/dere-types.md](cast/dere-types.md) | Tsundere, yandere, kuudere, dandere, deredere, himedere, and more, written to feel psychologically real |
| [cast/character-tropes.md](cast/character-tropes.md) | Onee-san, kouhai, senpai, childhood friend, ojou-sama, genki, gyaru, chuuni, class rep, transfer student, and more |

### genres/
| File | What it covers |
|---|---|
| [genres/genre-index.md](genres/genre-index.md) | Choosing and blending genres, and the voice-dial matrix |
| [genres/school-drama-and-slice-of-life.md](genres/school-drama-and-slice-of-life.md) | The home genre: hierarchy, loneliness, bullying, quiet everyday chapters |
| [genres/romcom-and-comedy.md](genres/romcom-and-comedy.md) | Misunderstanding engines, gag timing in prose, tsukkomi/boke, callbacks |
| [genres/harem.md](genres/harem.md) | Heroine differentiation, the lead's likability problem, the ending problem, reverse harem |
| [genres/ecchi-and-fanservice.md](genres/ecchi-and-fanservice.md) | Fanservice comedy with timing and restraint. **Adults-only rule.** |
| [genres/fantasy.md](genres/fantasy.md) | Magic academies, guilds, worldbuilding through dialogue |
| [genres/isekai-and-reincarnation.md](genres/isekai-and-reincarnation.md) | Openings, status windows, OP MCs, slow life, the meta-aware narrator |
| [genres/villainess-and-otome.md](genres/villainess-and-otome.md) | Doom flags, ballroom politics, the ojou narrator |
| [genres/action-and-battle.md](genres/action-and-battle.md) | Fight prose, attack names, tactics monologue, rivalry |
| [genres/mystery-psychological-horror.md](genres/mystery-psychological-horror.md) | School mysteries, manipulation, unreliable narration, dread |
| [genres/sports-idol-and-club.md](genres/sports-idol-and-club.md) | Competition arcs, training in prose, idols and bands |
| [genres/romance-and-melodrama.md](genres/romance-and-melodrama.md) | Slow burn, tearjerkers, adult/workplace romance, the gentle voice |

### setting/ and scenes/
| File | What it covers |
|---|---|
| [setting/school-life.md](setting/school-life.md) | Authentic Japanese school life: calendar, schedule, spaces, systems, customs, story uses |
| [setting/social-media-and-texts.md](setting/social-media-and-texts.md) | In-world posts, chat messages, calls, and how the POV reads them |
| [scenes/scene-playbook.md](scenes/scene-playbook.md) | 20+ scene recipes with beats and snippets |
| [scenes/emotional-climaxes.md](scenes/emotional-climaxes.md) | Outburst, breakdown, confession, reconciliation, farewell, and how prose changes at peaks |

### structure/ and templates/
| File | What it covers |
|---|---|
| [structure/chapter-and-section.md](structure/chapter-and-section.md) | Chapter anatomy, titles, numbered sections, openings, scene skips |
| [structure/arc-design.md](structure/arc-design.md) | The 9-beat arc, variants, pacing, unanswered questions |
| [structure/series-planning.md](structure/series-planning.md) | Multi-arc plans, cast rotation, the mastermind thread, web serial cadence |
| [structure/hooks-and-cliffhangers.md](structure/hooks-and-cliffhangers.md) | Hook taxonomy and section tilts |
| [templates/story-bible.md](templates/story-bible.md) | Fillable story bible plus a filled example |
| [templates/chapter-plan.md](templates/chapter-plan.md) | Fillable chapter plan plus a filled example |
| [templates/character-sheet.md](templates/character-sheet.md) | Fillable character sheet plus a filled example |

### revision/ and examples/
| File | What it covers |
|---|---|
| [revision/anti-robotic.md](revision/anti-robotic.md) | Banned AI-isms, generic-LLM tells, clichés, with a detection method and fix for each |
| [revision/mtl-vs-natural.md](revision/mtl-vs-natural.md) | Translationese vs. natural LN English: what to keep, what to fix |
| [revision/revision-checklist.md](revision/revision-checklist.md) | Multi-pass edit protocol, scoring rubric, self-critique loop |
| [examples/annotated-passages.md](examples/annotated-passages.md) | Original passages annotated technique by technique |
| [examples/before-after.md](examples/before-after.md) | Flat or robotic drafts transformed into the voice |
| [examples/sample-chapter-01.md](examples/sample-chapter-01.md) | Full sample Chapter 1 |
| [examples/sample-chapter-02.md](examples/sample-chapter-02.md) | Full sample Chapter 2 |
| [examples/sample-chapter-climax.md](examples/sample-chapter-climax.md) | Full sample climax chapter |

## 3. Reading paths

**"Write me chapter 1 of a new LN."**
SKILL, then templates/story-bible, then core/style-bible, then the genre file, then cast/character-design, then structure/chapter-and-section, then templates/chapter-plan. Draft, then revise with revision/revision-checklist.

**"Continue this in the same style."**
Read the user's text, then core/style-bible, then dialogue/honorifics-and-address (build the ledger from their text), then core/rhythm-and-flow. Draft, then revise with revision/anti-robotic.

**"Make this sound less robotic."**
revision/anti-robotic, then revision/mtl-vs-natural, then examples/before-after, then core/rhythm-and-flow. Rewrite, then score with revision/revision-checklist.

**"I want a yandere / kuudere / onee-san character."**
cast/dere-types or cast/character-tropes, then dialogue/character-voices, then core/description-and-portraits, then templates/character-sheet.

**"Isekai / fantasy / villainess story."**
genres/genre-index, then the specific genre file, then core/style-bible (the base voice still applies), then genres/action-and-battle if there is combat.

**"Plan a whole arc."**
structure/arc-design, then structure/series-planning, then structure/hooks-and-cliffhangers, then scenes/emotional-climaxes, then templates/story-bible.

## 4. Shared example cast

Files use one original default cast for continuity: **Minato Kuze** (cynical POV), **Haruto Amamiya** (harem lead), **Rin Tachibana** (tsundere), **Sayo Kujou** (ojou and mastermind), **Hina Matsuri** (genki), **Momo Shirasagi** (two-faced airhead), **Daichi Enomoto** (confidant), **Reika Hoshino** (bully queen), **Kasumi Ogata-sensei** (homeroom teacher), and **Gon Iwashita** (otaku friend), at Seiryou Private High School, Class 2-3. Genre files add their own small casts. See [templates/story-bible.md](templates/story-bible.md) for the filled bible.
