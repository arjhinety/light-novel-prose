# MTL vs. Natural: Keeping the Texture, Losing the Stiffness

> **Purpose:** Separate the Japanese-flavored texture readers love from the machine-translation (MTL) stiffness they merely tolerate, so your prose feels translated by a skilled human rather than a tool.
> **Load when:** Revising any draft, especially when imitating a web-novel translation closely, or when a draft feels "choppy", "stilted", or "like a translation".
> **Related:** [Anti-Robotic Prose](anti-robotic.md), [Revision Checklist](revision-checklist.md), [Rhythm & Flow](../core/rhythm-and-flow.md), [Diction & Japanese Terms](../core/diction-and-japanese-terms.md), [Punctuation & Typography](../core/punctuation-and-typography.md), [Honorifics & Address](../dialogue/honorifics-and-address.md), [Before & After](../examples/before-after.md)

---

## 1. The problem in one paragraph

The source novel this library studied is a fan translation of a Japanese web novel. Much of its charm comes from its Japanese-ness: honorifics, silent `"..."` lines, the analytical inner voice, sound effects like *Ding-dong-dang-dong*. But some of what readers experience as "the style" is actually **translation residue**: sentences that are choppy because Japanese clauses were split mechanically, subjects repeated because Japanese omits them and the tool put them all back, and idioms rendered word-for-word. When you imitate a translated novel, you must **copy the first category and repair the second**. This file draws the line.

The target is the prose of a professional light-novel localization: every Japanese texture kept on purpose, and every English sentence something a fluent writer might actually produce.

---

## 2. Keep vs. fix: the master table

| Keep (texture) | Fix (stiffness) |
|---|---|
| Honorifics: -kun, -san, -chan, -senpai, -sensei | Honorifics in narration ("Kuze-kun walked in") unless the POV character's own habit |
| `"..."` as a line of silence | `"..."` used five times in one exchange with no escalation |
| Sound-effect lines: *Ding-dong-dang-dong.*, *Creak.*, *Pat.* | Romanized SFX nobody can read (*Gatan. Zawa zawa.*) without context |
| Tildes for drawl: "Fiiine~" | Tildes in narration |
| Stutters from fluster: "W-What!?" | Stutters on every line of a calm character |
| Rhetorical question chains in narration | Questions that are really statements in disguise ("Wasn't it that he was tired?") |
| Short one-line paragraphs for impact | Every sentence as its own paragraph with no rhythm plan |
| Japanese school systems (class duty, go-home club) | Literal institutional names nobody explains ("Beautification Committee Member" with no context) |
| Surname-based narration | The surname repeated in every sentence of a paragraph |
| Interjections: "Eh?", "Haa...", "Tch" | "Eh?" as every reaction to everything |
| Recurring leitmotif ("the sediment") | The same adjective string ("dark, deep, murky") pasted every time without variation or growth |
| "It can't be helped" as a character's resigned catchphrase | "It couldn't be helped" as the narrator's default connective |
| Rom-com self-awareness | Literal "As expected of X" in every scene |

---

## 3. The twelve MTL artifacts (and their repairs)

Each artifact comes with an *original* MTL-style example written for this file (not quoted from any novel), plus its natural repair.

### 3.1 Clause-splitting choppiness

Japanese stacks many clauses into one long sentence. Tools often cut them into a string of short, disconnected statements. The result looks like the LN "short beat" style but has no **rhythm plan**: every sentence is the same length and nothing connects.

> ✗ Kuze finished his coffee. He stood up. He paid. He left the family restaurant. Outside was cold. He walked to the station.

> ✓ Kuze finished his coffee, paid for his own hamburger (and only his own hamburger), and stepped out into the cold.
> The station was a five-minute walk.
> He made it in four.

**Rule:** Short beats are a *choice* placed at emphasis points. Routine action gets joined with commas, "and", or "then", into one flowing sentence. See [Rhythm & Flow](../core/rhythm-and-flow.md).

### 3.2 Participial-opener stacking

Tools often render Japanese te-form sequences as "Having done X, Y did Z" or "Hearing that, she..." at the start of sentence after sentence.

> ✗ Hearing Rin's voice, Kuze turned. Seeing her expression, he frowned. Realizing she was angry, he sighed.

> ✓ "Hey. You."
> Kuze turned. Rin was standing at his desk with both hands flat on it, which was never a good sign.

**Rule:** Allow **one** participial opener per paragraph at most. Prefer plain sequence or dialogue first, reaction second.

### 3.3 Over-literal subject repetition

Japanese drops subjects freely. An English rendering that puts them all back produces a name in every sentence.

> ✗ Kuze looked at Amamiya. Kuze thought Amamiya was a hypocrite. Kuze did not say anything. Kuze drank his coffee.

> ✓ Kuze looked at Amamiya.
> Hypocrite.
> He didn't say it. He drank his coffee instead.

**Rule:** Name once when the subject changes, then use pronouns. When two same-gender characters are in play, re-anchor with a name each new paragraph, not each sentence.

### 3.4 Dropped subjects in English

The opposite failure: the tool drops the subject the way Japanese does, producing telegraphic fragments with no intent behind them.

> ✗ Went to the station. Waited for the train. Was tired.

> ✓ He went to the station and waited for the train. He was tired, the specific kind of tired that came from spending two hours pretending not to listen to other people's conversations.

**Rule:** A fragment is legal only when it *lands* something: a verdict ("Hypocrite."), a sound, a realization. Fragments of routine action read as machine output.

### 3.5 Literal idioms

| MTL literal | What it means | Natural LN English |
|---|---|---|
| "My face is on fire" (as narration, repeatedly) | Embarrassed | "Her face went red to the ears." (once), then vary |
| "It can't be helped" (every scene) | Resignation | "Oh well." / "Nothing to do about it." / keep "It can't be helped" as one character's tic |
| "Please take care of me" (yoroshiku) | Nice to meet you / I'm in your hands | "Nice to meet you." / "Looking forward to working with you." / "Be nice to me, okay?" |
| "Good work" (otsukaresama) at every parting | Thanks for your effort | "Good work today." for clubs and jobs; "See ya." for friends |
| "I'll be going / I'm home" (ittekimasu / tadaima) | Ritual phrases | Keep in dialogue for flavor ("I'm home."), but don't narrate them |
| "Excuse me for intruding" (ojama shimasu) | Entering someone's house | "Sorry for barging in." |
| "As expected of Kujou-san" | Admiration | "Of course Kujou would know." / "Typical Kujou." |
| "That kind of thing" | Vague reference (sonna koto) | "Something like that" or name the thing |
| "Is that so?" (sou desu ka) | Mild acknowledgment | "Oh." / "Huh." / "Really?" / "I see." |
| "What are you saying?" (nani itten no) | Disbelief | "What are you talking about?" / "Are you stupid?" (friends) |
| "It's not like that!" | Denial | Fine for a tsundere, but not for everyone |
| "Somehow" (nantonaku) as a sentence opener | Vaguely, for no clear reason | "For some reason," or cut and give the actual reason |
| "A certain boy" | Storytelling mannerism | Once in a prologue is charming; afterward use his name |
| "The atmosphere became heavy" | Mood shift | `"..."` / "Nobody said anything." |
| "His heart went doki" | Heartbeat SFX | *Ba-dump.* as an SFX line, once, or "His chest tightened." |

### 3.6 Sentence-final particle mistranslation

Particles like *ne*, *yo*, *na*, and *wa* carry tone. Tools either drop them (flattening the character) or overtranslate them ("right?" on every line).

| Particle function | Weak rendering | Better options |
|---|---|---|
| *ne* (seeking agreement) | "..., right?" every time | "right?", "huh?", "isn't it?", "yeah?", or a tilde: "Nice weather~" |
| *yo* (asserting) | "..., you know!" every time | an exclamation mark, "I'm telling you", or just assertion |
| *na* (musing, male-casual) | dropped | "...huh.", "Man, ...", a trailing ellipsis |
| *wa* (soft feminine or ojou) | dropped | Formal diction and full sentences: Sayo's "My." / "Indeed." |
| *zo / ze* (rough masculine) | dropped | "Let's go, man.", clipped imperatives |
| *kashira* (feminine wondering) | "I wonder" every time | "I wonder" occasionally; otherwise "Hm." with a finger to the lips |

**Rule:** Distribute particle flavor across **character voice** ([Character Voices](../dialogue/character-voices.md)), not across every sentence. Hina's lines end in `!` and `~`. Sayo's end in periods. Kuze's barely end at all.

### 3.7 Tense wobble

Japanese narration shifts between past and non-past freely. Tools often keep that wobble.

> ✗ Kuze walks into the classroom. Amamiya was already surrounded. He sits down.

> ✓ Kuze walked into the classroom. Amamiya was already surrounded.
> Of course he was.

**Rule:** Narration is **past tense**. Free indirect thought is **present tense** ("Why does he always do that?") and should be clearly the character's voice: a question, an exclamation, a fragment. Never mix tenses in plain narration.

### 3.8 The "as for X" topic structure

Japanese topic markers (*wa*) turn into "As for Kuze, he..." or "Speaking of Amamiya, ...".

> ✗ As for Kuze, he did not have any plans. As for Rin, she had club.

> ✓ Kuze had no plans. Rin had kendo.

Keep "Speaking of which" only in dialogue, and only when a character is visibly changing the subject.

### 3.9 Reported emotion with "feeling"

Tools love "He had a feeling of unease" and "a feeling of loneliness welled up."

> ✗ A feeling of unease welled up in Kuze's chest.

> ✓ Something was off.
> Kuze ran back through the conversation. Amamiya had said "we". He'd said "we" three times, and not once had it included Kuze.

**Rule:** Convert "a feeling of X" into the **evidence** that produces X, delivered through the analytical monologue ([Inner Monologue](../core/inner-monologue.md)).

### 3.10 Over-politeness mapped wrong

Japanese keigo (polite speech) has no clean English equivalent. Tools make polite characters sound like hotel staff.

> ✗ "I humbly apologize for the inconvenience I have caused you, Kuze-san."

> ✓ "I apologize. That was careless of me." (Sayo: formal, crisp, not servile.)

Formality in English comes from **complete sentences, no contractions, and precise vocabulary**. It does not come from stacked apologies or "humbly". See [Honorifics & Address](../dialogue/honorifics-and-address.md) for when a character switching *into* polite speech is itself a plot beat ("Why are you being polite with me all of a sudden?").

### 3.11 Unanchored onomatopoeia

> ✗ *Zawa zawa.* *Kyun.* *Gyu.* *Pero.*

These mean nothing to most English readers without context.

**Rule:** Use English-readable SFX lines (*Creak. Thud. Ring, ring, click. Squeak.*) or choose widely known ones (*Ba-dump*, *Pat pat*). If you want a Japanese one for flavor, anchor it: "The class went *zawa*, that particular murmur of thirty people pretending not to gossip." See [Diction & Japanese Terms](../core/diction-and-japanese-terms.md).

### 3.12 Emotion-verb literalism

| MTL | Natural |
|---|---|
| "She made a troubled face." | "She looked troubled." / "Her eyebrows drooped." |
| "He made a bitter smile." | "He smiled bitterly." / "a wry smile" |
| "She made her cheeks swell." | "She puffed out her cheeks." |
| "His expression became cloudy." | "His face fell." |
| "She showed a flustered appearance." | "She got flustered." / "H-Hey!" |
| "A vein popped on his forehead." (literal manga symbol) | "Something in his temple twitched." |
| "Sweat dropped from her head." (manga sweat-drop) | "Hina laughed weakly." |
| "Her eyes became dots." | "She stared, blank." |

**Rule:** Manga symbols (sweat drops, anger veins, sparkles) must be translated into **the behavior they represent**, not described literally.

---

## 4. What natural LN English sounds like

Four properties separate a good localization from MTL:

1. **Contractions everywhere**, in narration too. "He didn't" and not "He did not", unless the character is formal.
2. **Connectives that carry logic**: *because, so, but, even though, which meant, until*. MTL loses them and leaves the reader to infer. A human translator restores them.
3. **Varied reaction vocabulary.** An MTL text reacts with "Eh?" twenty times. A natural one uses "Eh?", "Huh?", "Hah!?", "What?", `"..."`, and a physical reaction, each chosen for the character.
4. **Idiomatic compression.** "He was on class duty today, so he stayed behind." That's one sentence, not three.

### Side-by-side: a full MTL passage and its natural rendering

**MTL-style (written for this example):**
> After school. Kuze was class duty. Kuze wiped the blackboard. Then, Hina came. "Kuze-kun, you are doing class duty? Please let me help!" Hina said. Kuze made a troubled face. "It is fine. It is my duty." Kuze said. Hina puffed her cheeks. "Muu, you are using polite language again!" Somehow, Kuze felt a feeling of embarrassment. As expected of the school's idol. Kuze thought.

**Natural LN rendering:**
> After school, Kuze was stuck with class duty.
> He was halfway through the blackboard when the door slid open.
> "Kuze-kun! You're on duty today? I'll help!"
> Hina Matsuri, the most popular girl in their year and possibly the most popular person in the building, bounced in with her ponytail swinging.
> "It's fine. It's my job."
> "Muu~ You're being polite again!"
> She made an "X" with her forearms. It was apparently a rule now. He didn't remember agreeing to it.
> "...Sorry. It's fine, I've got it."
> "Better!"
> She grabbed an eraser anyway.

**What changed:** repeated subjects became pronouns; "was class duty" became "was stuck with class duty"; "made a troubled face" was cut; "a feeling of embarrassment" became his wry observation about a rule he never agreed to; "As expected of..." became a portrait with a comic hyperbole; the honorific stays in dialogue only; Hina's tic ("Muu~", the X gesture) survives as characterization.

---

## 5. Things to keep even though they look "wrong" in standard English

Standard English style guides would flag these. Keep them anyway, because they *are* the genre.

1. **The silent line** `"..."` as a full paragraph.
2. **Sound-effect paragraphs** in the middle of a scene.
3. **Rhetorical question chains** of four or more in narration.
4. **Stutters** ("W-Wait") and **drawls** ("Fiiine~").
5. **Triple-quoted unison speech** for crowds: `"""Totally~"""`
6. **The section numeral** alone on a line.
7. **Surname narration** for the POV character, even in intimate moments.
8. **Honorifics** kept untranslated, including the shift from surname plus honorific to a bare given name as a plot beat.
9. **"Haa..."** as a sigh rendered as a line of dialogue.
10. **Self-aware genre commentary** ("This was straight out of a rom-com.").

---

## 6. Quick repair procedure

1. **Highlight every sentence under five words.** For each, ask: *is this landing something?* If not, merge it with its neighbor.
2. **Highlight every sentence that begins with the POV's surname.** Keep the first in each paragraph and turn the rest into pronouns or restructure.
3. **Search for** `feeling of`, `made a ... face`, `As expected`, `Somehow`, `As for`, `It can't be helped`, `that kind of thing`, `Is that so`. Fix each per §3.
4. **Check tense** in every narration sentence.
5. **Read reactions only** ("Eh?", "Huh?", `"..."`). Make sure no single reaction appears more than three times per scene.
6. **Check SFX.** Every SFX line should be readable by an English reader with no Japanese.
7. **Confirm the keep-list** (§5) survived. Over-correction that sands away the texture is its own failure. The result must still sound like a light novel.

---

## 7. Over-correction: the opposite failure

Some drafts fix MTL stiffness by turning everything into Western literary fiction. Every honorific becomes "Mr." or disappears, SFX lines vanish, the silent lines become "He didn't reply," and the chains of questions become one tidy paragraph of reflection. The result is smooth and *wrong*.

> ✗ (over-corrected) Minato didn't reply. He wondered, not for the first time, whether Haruto's generosity was genuine or merely performed for the benefit of the girls around him.

> ✓ "..."
> Kuze didn't answer.
> Was it generosity? Or was it for Hina's benefit? Or was Amamiya just the kind of guy who offered drinks to whoever happened to be standing in his field of vision, and Kuze, as usual, hadn't been standing there?

The first version uses given names (wrong register), a literary cadence ("not for the first time"), and an abstract dichotomy. The second keeps surnames, the silence line, and the spiral, and it adds a self-deprecating third hypothesis. **Natural does not mean Westernized.**

---

## 8. Dialogue pair bank

Common MTL dialogue renderings and natural alternatives, split by character type so the voice survives the repair. See [Character Voices](../dialogue/character-voices.md) for full voice profiles.

| MTL-style line | Genki (Hina) | Tsundere (Rin) | Ojou (Sayo) | POV (Kuze) |
|---|---|---|---|---|
| "Is that so?" | "Oh, really!?" | "...Huh. Whatever." | "Is that so." (flat, ominous) | "Huh." |
| "What are you saying?" | "Whaaat? No way!" | "Hah!? Are you stupid?" | "What nonsense." | "Meaning?" |
| "Please wait!" | "Wait wait wait!" | "H-Hold it right there!" | "A moment, please." | "Hold on." |
| "I am sorry." | "Sorry sorry sorry!" | "...My bad. Happy?" | "I apologize." | "Sorry." |
| "Thank you very much." | "Thanks a million!" | "D-Don't expect me to say thanks again." | "You have my thanks." | "Thanks." |
| "It is fine." | "It's all good!" | "It's fine! Stop asking!" | "It's no trouble." | "It's fine." |
| "I don't understand." | "I don't get it at all~" | "What's that supposed to mean!?" | "Explain yourself." | "...I'm not following." |
| "Good morning." | "Mornin'!" | "...Morning." | "Good morning." | "Morning." |
| "Let's go together." | "Let's all go! All of us!" | "F-Fine, I'll walk with you. Only to the station." | "Shall we?" | "...Sure." |
| "You are an idiot." | "You dummy~" | "Idiot. Idiot idiot idiot." | "How foolish." | "You're an idiot." |
| "I like you." | "I like you! Like, like-like!" | "I-It's not like I... ugh. I like you. There. Happy!?" | "I have feelings for you. I'd appreciate a reply." | "...I think I like you. Probably." |
| "Leave me alone." | "Just... not right now, okay?" | "Go away!" | "Kindly leave." | "Go to your club." |
| "Are you all right?" | "Are you okay? Are you okay!?" | "Y-You're not hurt, right? Not that I care." | "Are you injured?" | "You good?" |
| "It cannot be helped." | "Oh well! Next time!" | "Tch. Fine." | "There's no helping it." | "Whatever. It's fine." |
| "I will do my best!" | "I'll give it everything I've got!" | "Watch me. I'll win." | "I'll handle it properly." | "I'll try." |

The last column is the protagonist's. Notice it's always the shortest. That gap is the voice ([Dialogue Mechanics](../dialogue/dialogue-mechanics.md)).

## 9. Onomatopoeia conversion list

| Japanese SFX | Meaning | English SFX line or narration |
|---|---|---|
| *doki doki* | Heart pounding | *Ba-dump.* / "His chest tightened." |
| *zawa zawa* | Crowd murmuring | "The class murmured." |
| *gatan* | Clatter, chair falling | *Clatter.* |
| *bishi* | Sharp poke or chop | *Chop.* |
| *piku* | Twitch | "Her eyebrow twitched." |
| *nikori* | Gentle smile | "She smiled." |
| *niyari* | Sly grin | "Momo grinned." |
| *jii* | Staring intensely | "Rin stared. And stared." |
| *shiin* | Dead silence | `"..."` / "Silence." |
| *pachi pachi* | Clapping | *Clap, clap.* |
| *gara* | Sliding door | *Rattle.* / "The door slid open." |
| *kyun* | Heart squeeze (cute) | "Something in his chest went stupid." |
| *mogu mogu* | Chewing | "Munch, munch." (comic eaters only) |
| *puku* | Puffing cheeks | "She puffed out her cheeks." |
| *nade nade* | Patting a head | *Pat, pat.* |
| *gyu* | Squeezing, hugging | "She squeezed his sleeve." |
| *kacha* | Click (door, lock) | *Click.* |
| *pinpon* | Doorbell | *Ding-dong.* |
| *kin-kon-kan-kon* | School bell | *Ding-dong-dang-dong.* |

Use these sparingly: 1-4 SFX lines per chapter, placed where a manga would put a panel. Full glossary in [Diction & Japanese Terms](../core/diction-and-japanese-terms.md).

## 10. MTL self-test

Before delivering, ask of each paragraph:
1. Would a fluent English novelist write *this sentence structure*? If not, fix it.
2. Would a Japanese reader recognize *this texture* as theirs? If not, restore it.
3. Is every short sentence doing work?
4. Is every Japanese term either widely known or explained by context?
5. Does every character's politeness level match who they're talking to?

If all five answers are "yes", the paragraph has the texture without the stiffness.

## 11. Checklist

- [ ] No fragments of routine action; every fragment lands something (§3.1, §3.4)
- [ ] One participial opener per paragraph at most (§3.2)
- [ ] Surname once per subject change, then pronouns (§3.3)
- [ ] No literal idioms from the §3.5 table in narration
- [ ] Particle flavor carried by character voice, not by "right?" on every line (§3.6)
- [ ] Narration in past tense; free indirect thought in present (§3.7)
- [ ] No "a feeling of X"; the evidence is shown instead (§3.9)
- [ ] Formality through diction, not stacked apologies (§3.10)
- [ ] Manga symbols translated into behavior (§3.12)
- [ ] Keep-list texture intact (§5); not over-corrected into Western literary prose (§7)
