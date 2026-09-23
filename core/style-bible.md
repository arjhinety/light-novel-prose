# Style Bible: The Light-Novel Voice in One Place

> **Purpose:** The master overview of the voice. It defines what translated-light-novel prose is, what it sounds like, and what it must never sound like, and it summarizes every other core file so a writer can draft from this file alone in a pinch.
> **Load when:** Always, before drafting any prose with this skill. Re-read §2 and §12 before revising.
> **Related:** [Narration & POV](narration-and-pov.md), [Inner Monologue](inner-monologue.md), [Rhythm & Flow](rhythm-and-flow.md), [Description & Portraits](description-and-portraits.md), [Tone & Comedy](tone-and-comedy.md), [Diction & Japanese Terms](diction-and-japanese-terms.md), [Punctuation & Typography](punctuation-and-typography.md), [Dialogue Mechanics](../dialogue/dialogue-mechanics.md), [Anti-Robotic Pass](../revision/anti-robotic.md), [Genre Index](../genres/genre-index.md)

---

## 1. What this voice is

This is the English voice of a **well-translated Japanese light novel or web novel**, specifically the school rom-com/drama register of stories first serialized online and later published with anime-style illustrations. The benchmark text is a 100-chapter school drama about a cynical loner who can't stop asking why his classmate, a cheerful boy surrounded by beautiful girls, is so popular.

The voice has four pillars:

1. **A mind, not a camera.** Close third person locked to an overthinking POV character, who reads motives into crumbs of social behavior and then suspects himself for doing it.
2. **Talk, not description.** About half of every page is dialogue: stacked, quick, full of honorifics, stutters, tildes, and silences.
3. **Beats, not paragraphs.** Short sentences, one-line paragraphs for impact, and the occasional long flowing exhale where reflection needs room.
4. **Warmth under irony.** The narrator is bitter and funny, but he notices kindness, feels guilt, and cracks open when it matters.

And one overriding goal: **it must flow like natural English.** The source material is a translation, and some of its choppiness is translation artifact. We keep the texture (honorifics, sound effects, `"..."`, archetypes, school-life systems) and lose the stiffness. The reader should feel "this is a Japanese light novel" and never "this was machine-translated" or "an AI wrote this."

## 2. The measured profile

From close reading of the reference novel:

| Feature | Measurement | Implication |
|---|---|---|
| Dialogue share | ~47% of words | Scenes are conversations. Narration lives between lines. |
| Median narrative sentence | ~7 words | Short is the default. |
| Sentences of 6 words or fewer | ~54% | Clipped beats are normal. |
| Sentences of 25+ words | <2% | Long sentences are rare, so they land. |
| Silent `"..."` lines | ~4 per chapter | Silence is a line of dialogue. |
| Honorifics | everywhere | -kun, -san, -chan, and -sensei on nearly every name spoken aloud |
| Narrative questions | constant | "Why...? Was it...? Or was...? Maybe..." |
| Numbered micro-sections | 3-8 per chapter | Scenes are short and each ends on a tilt |
| Recurring leitmotif | yes | One private image for bad feelings, repeated and intensified |

These are targets, not quotas. See [Rhythm & Flow](rhythm-and-flow.md) for how to hit them without sounding mechanical. They do become **gates** at revision time (§2.6).

## 2.5 The three hard rules

Test runs of this library on other models found the same three failures in almost every draft. They are hard rules, not style preferences.

### R1: Pure dialogue lines

A paragraph that contains spoken dialogue contains **only the quotation**. There are no speech tags (*said*, *asked*, *whispered*), no action beats, no split quotes, and no narration before or after it in the same paragraph. Attribution comes from voice and tics, or from a separate narration paragraph just before or just after the line.

```
WRONG:
"Oh yeah," she paused, "so like, this is the problem."
Rin crossed her arms. "Whatever."
"Fine," Kuze said.

RIGHT:
Rin crossed her arms.

"Whatever."

"...Fine."
```

When one speaker says several sentences in a row, they go in one quote. When narration quotes back something someone said (the analytical engine's favorite move), the phrase goes in *italics*, not quotation marks, so every quotation mark on the page is live speech. In-world text (phone text-to-speech, messages, posts, signs) uses its own block layout. Full rule: [Punctuation & Typography §9.1](punctuation-and-typography.md#91-pure-dialogue-lines-r1). Full craft: [Dialogue Mechanics](../dialogue/dialogue-mechanics.md).

Why: it keeps dialogue reading like speech bubbles and narration like captions, it forces distinct voices instead of tag crutches, and it removes the single most Western-looking line shape in English prose.

### R2: Dashes only for breaks

`--` or `—` (pick one per story) is for (a) speech cut off or interrupted, (b) a thought that breaks off in narration, and (c) a structural scene stamp ("The next day--"). It is **never** used for narrative asides, appositives, or dramatic pauses inside a narration sentence. Use a period, a comma, or a new one-line paragraph instead. Target: almost zero dashes in narration. See [Punctuation & Typography §3](punctuation-and-typography.md#3-the-dash).

### R3: The profile is measured, not assumed

The measured profile in §2 is checked before delivery (§2.6). The most common drift is invisible from inside a draft: under length pressure, models write longer sentences and restate reflection instead of adding beats. A draft can *feel* on-voice while sitting at a 15-word median and 30% dialogue, which is a different voice.

## 2.6 Measurable voice gates

Before delivering any chapter, check these. Every one is countable.

| Gate | Pass | Why |
|---|---|---|
| Dialogue share of words | **40-55%** (35% only for a chapter the plan marks *introspective*, never lower) | Below 40% the book becomes a narrated essay about conversations |
| Narrative sentence median | **≤10 words** | The short beat is the voice's pulse |
| Narrative sentences ≥25 words | **≤5%** | Long sentences must stay rare to land as exhales |
| Mixed dialogue paragraphs (R1) | **0** | Hard rule |
| Aside dashes in narration (R2) | **0** | Hard rule |
| Repeated tic constructions | **No pattern 3+ times** in a chapter | Model-specific tics (e.g. *the specific X of someone who...*) read as robotic |
| Speaker anchoring (3+ characters present) | **≤4** dialogue lines in a row without a narration paragraph, and every line that matters passes the [speaker test](../dialogue/dialogue-mechanics.md#33-the-speaker-test-hard-rule-with-3-characters) | R1 removes tags, so identity has to come back through action paragraphs, vocatives, and unique tics |
| Dialogue contractions | **≥50%** of contractible phrases contracted | An uncontracted cast ("It is", "I do not") sounds identical and machine-translated |
| "That's not X. That's Y." pairs | **≤0.5 per 1,000 words** | The most common model crutch in dialogue. It homogenizes every voice into sitcom snark |
| Stock simile frames | **≤1.0 per 1,000 words** | *with the dignity of a collapsing empire* announces observation instead of observing |

**How to check by hand** (no tools needed):
1. Pick three random 300-word windows (beginning, middle, end).
2. In each, count the words inside quotation marks versus the total. That's the dialogue share.
3. Count the narration sentences and mark each one with 25+ words. More than one long sentence in a 300-word window is a warning, and more than two is a fail.
4. Scan every paragraph that contains a `"`. If anything sits outside the quotes, it fails R1.
5. Search for `--` and `—`. Each hit must be a cut-off, a broken thought, or a stamp.
6. In every group scene, cover the narration and read only the quotes. Any line whose speaker you'd have to guess needs an action paragraph.
7. In one window, count full forms (*it is, I do not*) against contractions in dialogue.

**With code execution**, run the optional [voice metrics tool](../tools/voice_metrics.py), which reports the countable gates with PASS/FAIL and warns on long dialogue runs. Details on the revision loop are in [Revision Checklist](../revision/revision-checklist.md).

**If a gate fails, fix it structurally.** If dialogue is low, convert reported speech and summary into live exchanges. If sentences run long, break the exhales into beats and keep one exhale per ~150 words. If length is short, add *beats and scenes* (an arrival, a second escalation, a quiet two-person moment), never adjectives or restated reflection.

## 3. A calibration passage

Read this before drafting. It demonstrates most of the voice in ~400 words, using the default cast (see [Character Design](../cast/character-design.md) and [Story Bible Template](../templates/story-bible.md)).

> Ding-dong-dang-dong.
>
> The last bell of the day rang with the same relentless cheer as always, and the classroom began its after-school migration: club kids first, stampeding, then the go-home club in a slow trickle.
>
> Kuze would have been part of the trickle, except he was on class duty.
>
> Matsuri clapped her hands together in apology, honey-brown ponytail swinging. She'd spent the last ten minutes of break at Amamiya's desk and the first five of class duty there too.
>
> "Seriously, sorry! I'll help now, so let's finish quick, 'kay?"
>
> "Sure."
>
> They split the work without discussing it. Blackboard, trash, windows, daily log. Two people with nothing to say to each other made a surprisingly efficient team.
>
> Across the room, Amamiya slung his bag over his shoulder, Kujou at his side like a well-dressed shadow.
>
> "We're heading to the club room. Want us to grab drinks for you guys?"
>
> *For you guys.* Plural. Kuze, apparently, had been counted.
>
> Matsuri hopped in place.
>
> "Ah, wait for me! I'm almost done!"
>
> Kuze tied off the trash bag.
>
> "It's fine. I'm go-home club anyway. It doesn't take two people to hand in a log."
>
> "Whoa, seriously? Kuze-kun, you're a lifesaver!"
>
> She was gone before he'd finished standing up. Amamiya waved over his shoulder, and the door slid shut on their laughter.
>
> The drinks, Kuze noticed, went with them.
>
> "..."
>
> Of course they did. He and Amamiya weren't friends. Nobody bought juice for a stranger.
>
> But the offer had existed thirty seconds ago, when Matsuri was in the room. So what had it been for? For her? So she'd see him being generous, even to the gloomy guy wiping the board? Or was it just a reflex, like holding a door?
>
> ...Or was Kuze only thinking about it this hard because nobody ever held a door for *him*?
>
> He didn't love that question.
>
> Something settled at the bottom of his chest, fine and gray, like silt in a glass of still water. It would be gone by tomorrow. Probably.
>
> He capped his pen and went to find the teacher.

What it shows: a sound-effect opener, a scene-setting exhale, a punchline jab, honorifics, a character-marking gesture placed in its own paragraph *before* the line it attributes, pure dialogue lines throughout (no tags, no beats glued to quotes), a quote-back in italics (*For you guys*), a silent beat, the three-question chain, self-suspicion, the leitmotif introduced, and a tilt ending ("Probably."). Notice how the gesture paragraphs (*Matsuri hopped in place. / Kuze tied off the trash bag.*) do the attribution work that "she said" would have done, while adding staging.

## 4. Narration (summary of [Narration & POV](narration-and-pov.md))

- **Close third, past tense, one anchor per numbered section.** The narrator knows only what the POV perceives, infers, and remembers.
- **Surname anchoring.** "Kuze", "Amamiya", "Tachibana" in narration, whatever the dialogue calls them. First-name narration signals intimacy and must be earned.
- **Free indirect thought.** Narration slides into the POV's own questions with no "he thought" scaffolding. Past tense by default ("Why was he here?"), present tense for flashes ("Why is he here?"), and first person for the sharpest moments ("Why am I here?"), rationed to 1-3 per chapter.
- **Calibrated inference.** "Obviously", "probably", "maybe", and "or was that just...?" vary the narrator's confidence.
- **Dramatic irony through limitation.** Report details faithfully that the POV misreads, so the reader sees more than he does.
- **Cut-aways** to other characters only at section breaks, short (100-500 words), anchored in the first line, and ending on a hook.
- **Time stamps with dashes**: "The next day--", "After school--".
- **First-person variant** is supported. Irony then comes from self-deprecation, and interludes replace cut-aways.

## 5. Inner monologue (summary of [Inner Monologue](inner-monologue.md))

The engine of the voice runs five steps:

1. **Notice** a small social asymmetry (an offer that vanished, a name said second, "I got them to make up").
2. **Quote back** the exact words and re-read them.
3. **Hypothesize** with a 3-4 question chain, darkest reading first and mundane reading last.
4. **Self-suspect**: "Or was he just jealous?"
5. **Verdict**: a short line that is bitter, wry, deflecting, a genre joke, ominous, or a refusal to conclude.

Plus:
- **One leitmotif** (Kuze's is "the sediment"), named consistently and intensified across the arc.
- **Pockets, not walls.** Thought interleaves with dialogue in 1-4 line pockets. Long monologues only when the POV is alone.
- **Arc evolution.** Playful observer, then irritated, confused, rationalizing, in denial, shattered, self-confronting, honest, and finally changed.
- **No essay voice, no therapy-speak, no named emotions** where a thought chain would show them.

## 6. Rhythm (summary of [Rhythm & Flow](rhythm-and-flow.md))

- **Four bands**: jab (1-4 words), beat (5-10), line (11-20), exhale (21-45).
- **Never three consecutive sentences in the same band**, except in deliberate spirals.
- **One-line paragraphs** for realizations, sounds, silences, and verdicts. Each must pass the *weight test*: if merging it loses nothing, merge it.
- **The long exhale** is what makes it flow. It is joined by cause, contrast, time, and concession, it puts the sting at the end, and it appears at most once per ~150 words.
- **Hand-off devices** connect short sentences: the contrast jab, echo word, question follow-up, correction, and time slide.
- **Anaphoric spirals** ("He hated... He hated...") at peaks only, one or two per arc.
- **Sound-effect lines**: 1-4 per chapter. *Ding-dong-dang-dong.*
- **Dialogue tempos**: rapid fire, walking pace, and the slow monologue-and-silence. Shift tempos within scenes.
- **Peaks strip irony** and simplify. Comedy puts the punch in the shortest line.

## 7. Description (summary of [Description & Portraits](description-and-portraits.md))

- **Economical scenery**: a line or two. Rooms, weather, and light only as mood markers.
- **Portraits on first appearance**, in 2-4 sentences: hair (color, length, quirk), eyes and face, build and bearing, reputation at school, and **the crack** (the contrast that complicates the image).
- **Anime expression shorthand is correct here**: puffed cheeks, a blush to the ears, half-lidded eyes, a flashing canine, hands clasped in apology. Give each character a **signature** 2-3 gestures instead of cycling through all of them.
- **Body-language paragraphs** replace dialogue tags. *Tachibana slammed both hands on his desk.* goes in its own paragraph, right before or after her line, never glued to it (R1).
- **Clothing** matters for status and events (uniform worn sloppily, a hairpin bought on a date, a festival yukata).

Example portrait:
> Rin Tachibana wore her silver-ash hair in a blunt bob that looked like she'd cut it herself with a kendo sword's worth of decisiveness. Sharp gray eyes, a permanent frown, and a canine that flashed when she grinned, which was rarely, and usually at someone's expense. The boys called her scary. Half of them meant it as a compliment.
> None of that explained why she went red to the ears every time Amamiya said her name.

## 8. Tone (summary of [Tone & Comedy](tone-and-comedy.md))

- **Cynical, not cruel.** The narrator's bitterness is funny because it's self-aware, and he suspects himself as often as others.
- **Deadpan underreaction.** Big emotion from the cast, a two-word reply from the POV. "I'll try." / "Done." / `"..."`.
- **Meta rom-com awareness.** The POV knows the genre he's in ("Straight out of a rom-com."), used about once a chapter.
- **Running gags** such as a girl scolding him for polite speech, a friend's bad jokes scored out of ten, or the otaku's "verily".
- **Earnest peaks.** When it turns serious, drop the irony completely. The prose gets simpler, not fancier.
- **Tonal switching** happens at section breaks or through a sound-effect interruption, rarely mid-paragraph.

## 9. Dialogue (summary of the dialogue files)

From [Dialogue Mechanics](../dialogue/dialogue-mechanics.md), [Honorifics & Address](../dialogue/honorifics-and-address.md), [Character Voices](../dialogue/character-voices.md), and [Emotional Dialogue](../dialogue/emotional-dialogue.md):

- **Stack lines untagged** when voices are distinct. 3-8 lines in a row is normal.
- **Pure dialogue lines (R1).** No tags at all, not even "said". Who's speaking comes from voice, or from an action paragraph placed before or after the line.
- **Group chatter**: a burst of 4-6 untagged lines, then one narrative line with the POV's take.
- **Silence**: `"..."` as a line.
- **Interruption**: `--` at the end of the cut line.
- **Honorifics consistent**, with **name escalation as plot** (Kuze-kun to Kuze to Minato is a romance arc in three words).
- **One to three tics per character**, never shared.
- **The POV talks less than he thinks.**
- **Emotional peaks**: shorter lines, fragments, chants with triple-quote unison, the monologue-and-silence duet, and the long-withheld outburst.

## 10. Diction (summary of [Diction & Japanese Terms](diction-and-japanese-terms.md))

- **Plain, contemporary, contracted English**, including in narration.
- **Teen slang in dialogue**, not narration.
- **Keep untranslatable Japanese terms**, unitalicized: -kun/-san/-chan/-sensei/-senpai, bento, itadakimasu, go-home club, class duty, homeroom, cultural festival, staff room, family restaurant, and so on.
- **Don't over-sprinkle** (no gratuitous "baka" or "kawaii" in narration).
- **Interjections carry voice**: "Eh?", "Huh?", "Haa...", "Tch.", "Nn...", "Ehe~", "Fueee!"
- **Parody brand names** for in-world apps and shops ("Chirp", a mall ice-cream shop with a silly French name).

## 11. Punctuation (summary of [Punctuation & Typography](punctuation-and-typography.md))

| Mark | Use |
|---|---|
| `"..."` | Silence, as its own line |
| `...` in speech | Hesitation, trailing off |
| `--` or `—` (one per story) | Interruption, a broken-off thought, or a time stamp ("The next day--"). Never narrative asides (R2). |
| `"` double quotes | Live speech only, alone in its paragraph (R1) |
| `~` | Sing-song, teasing, drawl ("Hey there~") |
| `W-Wait` | Fluster stutter |
| `?!` / `!?` | Shock, in dialogue only |
| `"""Totally~"""` | Unison speech, rare |
| `1`, `2`, `3` on their own lines | Numbered section breaks |
| Italics | Quoted-back phrases, scare terms, and in-world text (never double quotes for these) |

## 12. The never list (preview of [Anti-Robotic Pass](../revision/anti-robotic.md))

Never write these in this voice:

- **AI-isms**: "a testament to", "tapestry", "couldn't help but feel", "a mix of emotions", "the weight of", "palpable", "in that moment", "something shifted", "little did he know", "a smile tugged at", "delve", "unspoken", "electric", "barely above a whisper" (sparingly at most).
- **Named emotional summaries**: "He felt a complex mix of jealousy and confusion."
- **Purple scenery**: dust motes dancing, golden light spilling, cherry blossoms "like pink snow" in every chapter.
- **Symmetrical tricolons everywhere**: "It was cold, it was dark, it was lonely."
- **Therapy-speak**: "process", "boundaries", "validate", "trauma response" (unless a character is being deliberately clinical).
- **Explaining the joke** or explaining the emotion after dialogue has shown it.
- **Section endings that summarize.** End on a tilt.
- **Tagged or glued dialogue**: `"Fine," she said.` / `Rin sighed. "Fine."` / `"Oh," she paused, "so..."`. Speech stands alone (R1).
- **Aside dashes** in narration: `He had one rule--never volunteer--and broke it.` (R2)
- **Stock constructions** that betray a model: *the specific [noun] of someone who...*, *something in her shoulders eased*, *which was true, and which was also...*. See the model-tic list in [Anti-Robotic Pass](../revision/anti-robotic.md).
- **MTL stiffness**: "As for Kuze, he was a student who was ordinary." / "Being that it was after school, the students were going home."

## 13. Structure (preview of the structure files)

From [Chapter & Section](../structure/chapter-and-section.md), [Hooks & Cliffhangers](../structure/hooks-and-cliffhangers.md), and [Arc Design](../structure/arc-design.md):

- **Chapter** = one situation, one turn, one hook. 2,500-4,500 words (web-novel episode length).
- **Numbered micro-sections** every 600-1,200 words, each ending on a tilt: a reveal, arrival, reframe, silence, or verdict.
- **Openings**: a sound effect, dialogue in media res, a time stamp, the POV alone thinking, or a cut-away.
- **Titles**: playful serial titles, often a recurring question plus part number ("Do You Like Family Restaurants? 3").
- **Arcs**: observer, pulled in, small bond, social pressure, failure, break, confidant, aftermath, and changed.
- **Unanswered questions** carry into the next arc.

## 14. Genre adaptation (preview of [Genre Index](../genres/genre-index.md))

The mechanics above are the base layer. Genres turn the dials:

| Dial | School drama (default) | Rom-com | Isekai | Action | Horror/mystery |
|---|---|---|---|---|---|
| Irony | High | High | High (meta) | Medium | Low-medium |
| Dialogue share | ~50% | ~55% | ~40% | ~35% | ~40% |
| Description density | Low | Low | Medium (world) | Medium (motion) | Medium (dread) |
| Monologue analysis | Social motives | Misreadings | Game-logic | Tactics | Clues and fear |
| Comedy ratio | 30% | 60% | 40% | 20% | 10% |

Each genre file specifies its own dials, tropes, scene recipes, and checklists. Character stereotypes (tsundere, yandere, kuudere, onee-san, gyaru, and so on) live in [Dere Types](../cast/dere-types.md) and [Character Tropes](../cast/character-tropes.md).

## 15. What "non-robotic" means here, concretely

Users of this skill care most about **flow** and a **non-robotic tone**. Here are the operational definitions:

**Robotic** prose has:
- Uniform sentence lengths and structures (subject-verb-object, over and over)
- Emotions stated rather than enacted
- Every beat reported, none processed
- Tidy symmetry: balanced lists, parallel paragraphs, and neat closure
- Vocabulary that is generically "literary" but belongs to nobody
- Characters who all speak in complete, polite, grammatical sentences
- Transitions that announce themselves ("Meanwhile," "Later that day,")

**Human** LN prose has:
- Rhythm that varies because the *thought* varies
- Emotion enacted through question chains, gestures, silences, and overreactions
- A specific mind processing specific crumbs
- Asymmetry: a thought abandoned mid-way, a joke that lands sideways, a section that ends before it's "resolved"
- Vocabulary that belongs to *this* narrator ("the sediment", "the ledger", "go-home club")
- Characters who interrupt, stutter, drawl, go silent, and say the wrong thing
- Transitions that are just a dash and a time stamp, or a bell

A useful test is to **cover the character names.** If you can still tell who is thinking and who is talking, it's human. If it could be anyone, it's robotic.

## 16. Voice in the wild: three contrasted versions

The same beat, written three ways. The situation: *Kuze meets Matsuri in the hallway, where she's hiding behind a wall to spy on Amamiya with other girls.*

### 16.1 Robotic

> Kuze walked down the hallway. He saw Hina Matsuri hiding behind a wall. She was watching Amamiya, who was walking with three girls. Kuze felt curious and asked her what she was doing. She was embarrassed and made an excuse. Kuze realized that she had feelings for Amamiya. He felt a complex mixture of emotions, including sympathy and jealousy.

Everything is reported and nothing is processed. The emotions are named, and the sentences are uniform.

### 16.2 Over-literary

> The corridor stretched before him like a river of polished linoleum, bathed in the honeyed glow of the late afternoon sun. There, half-concealed behind the pale concrete pillar, stood Hina Matsuri, her honey-brown ponytail trembling like a question she dared not ask, her gaze fixed with aching intensity on the distant figure of Amamiya, whose laughter drifted back through the air like a melody meant for someone else.

It is pretty, and it is wrong for this genre. There's no dialogue, no wryness, and no Kuze.

### 16.3 On-voice

> Near the broadcast room, Kuze spotted a girl peeking out from behind a pillar.
> Only her head stuck out, like a cat that thought it was hidden. She hadn't noticed him at all.
> Suspicious.
> "What are you doing?"
> "Eek--!"
> Matsuri jumped a full centimeter off the floor and spun around, already red.
> "Ah, um, this is, well, you see..."
> "..."
> Down the hall, Amamiya was strolling toward the club room with Tachibana on one arm, Kujou on the other, and Shirasagi orbiting somewhere nearby. Matsuri had clearly meant to call out to him, seen the crowd, and lost her nerve.
> Kuze pieced it together in about a second. It did not take a detective.
> "I was, um, checking the floor for anything dangerous! You know?"
> "Ah. Be careful, then."
> "Y-Yup! Exactly! And don't tell anyone, okay? It's embarrassing! Checking floors!"
> She nodded at her own excuse, pleased, as if it had actually worked.
> Why him? The question came up out of the sediment before Kuze could stop it. The prettiest girl in the year, the one who talked to everyone without a single wall, and she was hiding behind a pillar for a guy who was currently being escorted down a hallway by three other girls.
> What did she see in him?
> ...And what exactly did Kuze want the answer to be?
> He didn't follow that thought any further.

It has a sound-effect-like interjection, a cat simile for comic precision, the silent beat, a POV inference marked as easy ("It did not take a detective."), the flustered excuse with stutters and a comic doubling-down, the question chain rising from the leitmotif, self-suspicion, and a refusal verdict. Every line of speech stands alone in its paragraph, and gestures such as *Matsuri jumped a full centimeter* get their own lines (R1).

## 17. Style under different POV characters

The voice is not *only* Kuze's. Every anchor gets the same mechanics with a different engine. Summarized from [Narration & POV](narration-and-pov.md) and [Inner Monologue](inner-monologue.md):

| Anchor type | Sentence feel | Notices | Verdict flavor | Leitmotif example |
|---|---|---|---|---|
| Cynical loner | Short, dry, precise | Hypocrisy, asymmetry | Bitter / wry | Sediment, a ledger |
| Tsundere | Short, repeating, exclamatory | Whether he noticed *her* | Flustered denial | Heat in the face |
| Ojou / mastermind | Long, controlled, few questions | Leverage | "Interesting." | A chessboard, red ink |
| Genki girl | Bouncy, run-on, exclamation | Who's lonely | Bright resolve | Sunlight, a skipped beat |
| Kuudere | Minimal, flat, precise | Everything, says nothing | Silence | A still surface |
| Yandere | Sweet, then abruptly flat | Threats to "us" | Chilling calm | A red thread |
| Isekai MC | Chatty, meta | Game logic | Meta joke | A status window |
| Sincere harem lead | Short, warm, declarative | The small effort each girl hid | Declaration, not accusation | A bloom, a count that never runs out |

The engine is re-aimed, never switched off. Full treatment, with worked examples for each temperament: [POV Temperaments](pov-temperaments.md). For deeper personality work, see [Dere Types](../cast/dere-types.md) and [Character Tropes](../cast/character-tropes.md).

## 18. Consistency across a long work

Serial fiction runs for hundreds of thousands of words. The voice stays stable if you track:

1. **Narration names** per character and per POV anchor
2. **Address forms** in dialogue, and every change to them (a change is a plot event)
3. **Leitmotifs**: the exact wording, and the current "intensity level"
4. **Running gags**: last occurrence, and what variation is next
5. **Tics**: which phrases belong to which character, with no sharing
6. **Open questions**: what the POV suspects but hasn't confirmed
7. **Callbacks planted**: objects and lines that should return (the hamburger and the black coffee)

Keep these in the [Story Bible](../templates/story-bible.md), and review it before every chapter.

## 18.5 Ten misconceptions about this voice

1. **"Short sentences means simple writing."** No. The short sentences are the surface. Underneath is a mind doing complex social reasoning. Simple *syntax*, sophisticated *thought*.
2. **"Anime shorthand is lazy."** Not in this genre. A blush to the ears or a puffed cheek is a shared visual vocabulary that readers of the genre enjoy. What's lazy is using the *same* shorthand for everyone.
3. **"More Japanese words means more authentic."** No. Authenticity comes from school-life systems, honorific dynamics, and archetype behavior. Sprinkling "baka" and "sugoi" into narration makes it read like fan fiction.
4. **"The narrator should be right."** No. The narrator should be *interesting*. Half-right is ideal.
5. **"Cynicism is the voice."** Cynicism is the *surface*. The voice is a lonely person who wants to be proven wrong about people.
6. **"Every line needs a tag."** No. Distinct voices identify themselves, and when they can't, an action paragraph does the job. In this library, tags aren't just clutter; they break R1.
7. **"Silence is filler."** `"..."` is one of the most expressive lines in the book.
8. **"Repetition is bad style."** Leitmotifs, spirals, and chants are deliberate repetition. *Accidental* repetition (the same verb three times in a paragraph) is still bad.
9. **"Comedy and drama shouldn't mix."** This voice lives on the switch between them. A bullying arc can open with a joke about hamburger steak.
10. **"Long is thorough."** A chapter that ends on a tilt at 3,000 words beats one that wraps everything up at 5,000.

## 18.6 The reader's contract

A reader who opens a light novel expects a few things, and the voice keeps faith with them:

- **Fast reading.** They can read a chapter on a phone in one commute. Short paragraphs and dialogue-heavy pages make that possible.
- **A companion mind.** They are spending time with the POV character, so he must be good company: sharp, funny, and flawed in ways they recognize.
- **Recognizable types, with a twist.** They want the tsundere, and they want to discover why she's like that.
- **A reason to click "next".** Every chapter ends tilted.
- **Payoff for loyalty.** Callbacks, name changes, and leitmotifs reward readers who remember chapter 3 in chapter 40.

Break the contract (a slow, ornate chapter, a narrator who is merely cruel, a cast of flat types, or an ending that resolves everything) and the reader drops the series.

## 19. Workflow in brief

1. **Bible**: cast, visual signatures, tics, address forms, the leitmotif, and the POV's core question ([Story Bible Template](../templates/story-bible.md)).
2. **Plan**: situation, turn, hook, and numbered sections ([Chapter Plan Template](../templates/chapter-plan.md)).
3. **Draft**: follow §§4-11, favoring dialogue and letting the monologue run the engine.
4. **Revise**: the [Revision Checklist](../revision/revision-checklist.md), which covers the banned-phrase sweep, rhythm audit, tilt check, show-don't-explain, honorific consistency, and the measurable gates in §2.6.
5. **Deliver**: prose only. A heading, numbered sections, and nothing else.

## 20. The one-paragraph version

If you remember nothing else: **write in close third person from inside an overthinking teenager's head. Make half the page dialogue, with honorifics, stutters, tildes, and `"..."` silences, and give every spoken line its own paragraph with no tags glued on. Keep most sentences short and let one long, connected sentence breathe when the character reflects. Have him notice tiny social slights, quote them back, chain questions about motives, suspect himself, and land a short verdict. Describe people like anime character sheets with one crack in the image, and barely describe rooms. Be funny through deadpan and underreaction, and drop the irony completely when it hurts. End every section off-balance. Keep dashes for interruptions only. Never write "tapestry".**
