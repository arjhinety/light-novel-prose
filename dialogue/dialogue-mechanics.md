# Dialogue Mechanics

> **Purpose:** The nuts and bolts of putting speech on the page in the light-novel voice: pure dialogue lines, stacking, attribution, group chatter, silence, interruption, and banter rhythm.
> **Load when:** Any scene with two or more characters talking. In practice, almost every scene you write.
> **Related:** [Character Voices](character-voices.md), [Honorifics & Address](honorifics-and-address.md), [Emotional Dialogue](emotional-dialogue.md), [Punctuation & Typography](../core/punctuation-and-typography.md), [Rhythm & Flow](../core/rhythm-and-flow.md), [Inner Monologue](../core/inner-monologue.md), [Anti-Robotic](../revision/anti-robotic.md), [Revision Checklist](../revision/revision-checklist.md)

---

## 1. Why dialogue is the skeleton of this voice

In the reference novel, roughly **47% of all words sit inside quotation marks**. That is not an accident of genre. The light novel descends from serialized web fiction, which is read fast, on phones, in bursts. Dialogue is the fastest-reading material in prose: short lines, lots of white space, and instant character. The narration exists largely to *react* to dialogue. It interprets, dissects, and resents what was just said.

That gives you a working model of every scene:

1. **People talk.** Quick, overlapping, in character.
2. **The POV character hears something small.** A word choice, an omission, a shift in who is addressed.
3. **The narration chews on it.** See [Inner Monologue](../core/inner-monologue.md).
4. **The POV character replies with something tiny**, or with nothing at all.
5. Repeat.

If you write a scene where the narration carries the story and dialogue only decorates it, you have written a Western literary scene, not a light-novel one. Flip the ratio.

**Target band (chapter level, a hard gate):** 40-55% of a chapter's words are in dialogue. Only a chapter the plan explicitly marks as "introspective" may drop to 35%, and never lower. Inside a chapter, individual scenes vary. A solo scene (the POV alone reading Chirp posts, walking home, staring at the ceiling) can sit near 10-25%, and club-room chaos or a confrontation can push to 65%. The chapter total still has to land in the band, so a long solo scene must be paid for with dialogue-heavy scenes elsewhere. "This chapter is introspective" is not a license to skip the gate. See [Revision Checklist](../revision/revision-checklist.md) for how to measure it.

## 2. The pure dialogue line (hard rule)

This is the most visible formatting rule in the library. It is also the one models break most often, because Western fiction trains them to do the opposite.

### 2.1 The rule

**A paragraph that contains spoken dialogue contains only the quotation.** That means:

- **No speech tags.** No "she said", "he asked", or "Rin whispered".
- **No action beats in the same paragraph.** Not before the quote, and not after it.
- **No split quotes.** Nothing like `"Well," she paused, "maybe."`
- **No narration trailing the line** ("...," he said, looking away).

Attribution comes from one of three places, and only these three:

1. **Voice and tics.** The line itself tells you who spoke (see [Character Voices](character-voices.md)).
2. **A separate narration paragraph just before the line.** The speaker acts, then speaks.
3. **A separate narration paragraph just after the line.** Someone reacts, or the speaker does something that confirms it was them.

When one speaker says several sentences in a row, all of them go inside **one** quote in one paragraph.

### 2.2 Wrong vs. right

The pattern the user explicitly dislikes, and the fix:

```
WRONG:
"Oh yeah," she paused, "so like, this is the problem."

RIGHT:
She paused, lips pressed together.

"Oh yeah... so like, this is the problem."
```

```
WRONG:
Rin crossed her arms. "Whatever."
"Fine," Kuze said.

RIGHT:
Rin crossed her arms.

"Whatever."

"...Fine."
```

```
WRONG:
"It's not like I was waiting for you or anything." Rin looked everywhere but at him. The tips of her ears had gone red.

RIGHT:
"It's not like I was waiting for you or anything."

Rin looked everywhere but at him. The tips of her ears had gone red.
```

```
WRONG:
"The thing is--" Amamiya scratched the back of his head. "--I kind of promised everyone we'd go together."

RIGHT:
"The thing is..."

Amamiya scratched the back of his head.

"I kind of promised everyone we'd go together."
```

In the last pair, the split quote becomes two separate lines with the gesture between them. The pause is still there. It is carried by white space instead of a tag.

### 2.3 Why this rule serves the voice

- **It's the translated-LN look.** In the reference novel, speech and narration sit on separate lines far more often than not. A page of pure quote lines interleaved with short narration lines is the visual signature of the genre.
- **It forces distinct voices.** When you can't lean on "Rin snapped", the line has to sound like Rin. That pressure is healthy (see [Character Voices](character-voices.md)).
- **It gives the narration its own beat.** A gesture on its own line gets a full breath of attention. Rin's red ears land harder alone than tucked behind a quote.
- **It keeps the dialogue ratio honest.** Mixed paragraphs hide how much of the page is actually speech.

### 2.4 What the rule does NOT cover

- **Quoted-back phrases inside narration.** When the POV dissects something someone said, the phrase goes in *italics*, not quotation marks, so every quotation mark on the page stays live speech. For example: Not *they made up*. *I got them* to make up.
- **In-world text.** Texts, Chirp posts, phone text-to-speech, and signs use their own block formatting (see [Social Media & Texts](../setting/social-media-and-texts.md)).
- **A device's voice (text-to-speech, a recording, a robot).** The quote holds only what the device actually says aloud. Attribution goes in its own narration paragraph, never inside the quote. `"'The flower does not decide,' the book said."` fails, because it reads as if the phone is also saying *the book said*. Write it this way instead:

  > Shizuka tapped her screen. The speaker read a line from her book.
  >
  > "The flower does not decide. It is a witness."

  If the device quotes a published source, the narration can say so once per scene ("a line from her book"). After that, the reader knows where the voice is coming from.
- **Unison lines.** `"""Guess so."""` is still a pure dialogue line.
- **Documentation prose.** Tables, bullet lists, and analysis in these reference files may quote lines inline. The rule governs *story prose and example passages*.

### 2.5 Attribution toolkit under the rule

| Situation | Technique |
|---|---|
| New speaker enters | A narration line of the speaker *doing* something, then their quote |
| Two speakers, long stack | A pure stack; reanchor every 6-10 lines with a one-line action paragraph |
| Three or more speakers | A tic in every line, plus an action paragraph whenever a speaker is new to the stack |
| The same speaker twice in a row | Put an action paragraph for that speaker between the two lines, or merge them into one quote |
| Whisper or shout | Carry it in the line (caps, `...`, stutter, `~`), or in a sound-describing narration line afterward: *It came out barely louder than the radiator.* |
| A pause mid-thought | Split into two quote paragraphs with a gesture paragraph between |
| Ambiguous who's talking | Rewrite the line so the voice gives it away, or add an action paragraph *before* it |

### 2.6 Self-check

After drafting, scan every paragraph that contains a quotation mark. If there are *any* words outside the quote marks, the paragraph fails. Split it. The optional script [`tools/voice_metrics.py`](../tools/voice_metrics.py) counts these "mixed paragraphs" automatically; the target is zero.

## 3. Stacking: lines without tags

The single most recognizable feature of LN dialogue on the page is **the stack**: several lines of speech in a row, each its own paragraph, with no attribution at all.

> "You're late."
>
> "I'm not late. The bell hasn't rung."
>
> "You're late by my standards."
>
> "Your standards aren't a school rule."
>
> "They should be."

Nobody is named, and the reader never gets lost. That works for three reasons:

- **Only two speakers**, established in the line before the stack.
- **Distinct voices.** Sayo's clipped superiority against Kuze's flat correction. You could shuffle the names and still sort the lines.
- **Alternation is strict.** Line 1 is A, line 2 is B, and so on.

### 3.1 Rules for safe stacking

| Situation | Max untagged lines | Why |
|---|---|---|
| Two speakers, distinct voices | 6-10 | Alternation carries it |
| Two speakers, similar voices (two polite girls) | 3-4 | Readers lose count; reanchor with an action paragraph |
| Three speakers | 3-4, then reanchor | Alternation breaks down |
| Group of 4-6, **throwaway chatter** | A burst of up to 6 lines, then one narration paragraph (see §5) | The blur is the point, but only for lines that carry no plot, information, or feeling |
| Group of 4-6, **any line that matters** | Every such line must pass the speaker test (§3.3) | A plot line from an unknown mouth is a lost line |
| A line that breaks the alternation (same speaker twice) | Put an action paragraph between the two lines | Otherwise the reader assigns it wrong |

**The chatter exception is narrow.** Test runs of this library showed models treating an entire five-person scene as "chatter" and running 11-13 lines without a single anchor, so the reader couldn't tell who proposed the plan, who objected, or who made the joke. A multi-character scene is not a chatter burst. A burst is a handful of interchangeable reaction lines ("No way!" / "Seriously?" / "Again?!"), and then the scene gets its speakers back.

### 3.2 Reanchoring with an action paragraph

When a stack runs long, drop in **one narration paragraph** that names the next speaker by showing them doing something. The quote that follows stands alone:

> "They should be."
>
> Sayo flicked a strand of black hair over her shoulder, as if the matter were settled.
>
> "It's not a rule, Kujou."
>
> "My. You remember my name. How touching."

The action paragraph is also a chance to *characterize*. Sayo's hair flick says "I have won" without her saying it. That's two jobs for one line, which is the efficiency the voice depends on.

### 3.3 The speaker test (hard rule with 3+ characters)

The pure-dialogue rule (§2) takes tags out of the quote. That means you **must** put identity back some other way, or the stack turns into anonymous voices. With three or more characters in a scene, every line that carries plot, information, or feeling must be attributable by at least one of these cues, checked in this order:

1. **An action paragraph** naming the speaker, directly before the line (best), or directly after it.
2. **A vocative or answer cue in the line itself.** "Hina, stop." tells us who is being spoken to, and the next line is Hina. "*You* wrote the rules!" is aimed at the rule-writer.
3. **A tic only one character owns.** "Fueee~", "My.", "verily", "Mufufu", a text-to-speech phone voice, a stopwatch reading. This works only if the tic is truly unique in the scene.
4. **Strict two-person alternation** that has already been established, inside a scene where the others are clearly silent.

**Run the test.** Cover the narration and read only the quotes. For every line that matters, can you name the speaker? If you have to guess, add an action paragraph. A practical ceiling: **with 3+ speakers, never more than 4 consecutive dialogue lines without a narration paragraph.** A duet between two characters with distinct voices can run far longer.

**Don't over-correct into tags in disguise.** The fix isn't a narration paragraph that only says "Karane said this." It's a real beat: Karane planting her hands on the table, Nano clicking her stopwatch. Those paragraphs characterize, pace the scene, and anchor the speaker at the same time.

**Measuring it:** [`tools/voice_metrics.py`](../tools/voice_metrics.py) reports the longest run of consecutive dialogue lines and warns above 8. The warning is harmless in a two-person duet, but in a group scene it means the speaker test almost certainly fails.

## 4. Attribution: actions over verbs

### 4.1 The hierarchy

From best to worst in this voice:

1. **No attribution.** Voice alone identifies the speaker.
2. **An action paragraph before or after**, on its own line. *Rin slammed both palms onto his desk.* Then, as a new paragraph: "What's that supposed to mean!?"
3. **A sound paragraph.** When volume matters, describe the sound in its own narration line: *The words came out small enough to lose to the air conditioner.*
4. **Speech tags of any kind** ("said", "asked", "muttered", "retorted", "exclaimed", or "she said angrily"). **Not used in this library's story prose.** Under the pure-line rule, even the invisible "said" goes. If a line can't be attributed without a tag, fix the line or add an action paragraph.

Attitude verbs and adverbs were always the worst option ("snapped", "quipped", "admonished", "replied sarcastically"). They tell the reader how to feel about a line that should already show it. Now they are simply gone. If the line isn't angry without "angrily", fix the line.

### 4.2 Where the action paragraph goes

- **Before the line**, to prepare an entrance or a shift in energy:

  > Hina skipped up from behind and peered into his face.
  >
  > "Morning, Kuze-kun! You look like a gloomy cloud today!"

- **After the line**, to show a reaction or to land the joke:

  > "It's not like I was waiting for you or anything."
  >
  > Rin looked everywhere but at him. The tips of her ears had gone red.

- **Between two halves of a thought**, for a pause with weight. Split the speech into two quote paragraphs:

  > "The thing is..."
  >
  > Amamiya scratched the back of his head.
  >
  > "I kind of promised everyone we'd go together."

Don't overuse the split. Once or twice per scene is plenty. A stack of pure lines is the default; action paragraphs are the seasoning.

### 4.3 The "narrative tag" LN habit

Translated LNs often follow a line with a sentence that restates the speech act:

> "Let's all go eat together!"
>
> Amamiya suggested that they all eat together.

This is a **translation artifact** (Japanese narration often re-summarizes for clarity). It reads robotic in English. It's also where models sneak tags back in after the pure-line rule removes them. Fix it by making the follow-up paragraph *add* something the line didn't say:

> "Let's all go eat together!"
>
> Amamiya had already decided. The question mark was a formality.

Now the narration paragraph is doing the POV's work, reading motive into the line. See [MTL vs. Natural](../revision/mtl-vs-natural.md) for more pairs.

## 5. Group chatter

Club rooms, classroom mornings, and the harem swarming the lead are the scenes where the voice sounds most like an anime. Five people talk at once, and the reader is meant to feel slightly overwhelmed, exactly like the POV character.

### 5.1 The burst

Write 4-8 unattributed lines from different speakers, each with a distinct tic, with no attempt to make them a coherent conversation:

> "Morning, Haru!"
>
> "You're late again, you know."
>
> "My, is that bedhead? How unbecoming of my husband."
>
> "H-Husband!? Since when!?"
>
> "Fueee, Haruto-kun, your tie's crooked~ Let me fix it!"
>
> "Whoa, whoa, one at a time!"

Then **one narration paragraph** that pulls back to the POV:

> Kuze took one step back. Then another. The little world around Amamiya closed like a door he had never been invited through.

### 5.2 Why the burst works

- **Tics identify the speakers.** "My" is Sayo, the stammer is Rin, "Fueee" is Momo, and "Whoa, whoa" is Amamiya. You never needed a tag. This only works if the [Character Voices](character-voices.md) are distinct. Chatter bursts are the stress test of the pure-line rule.
- **The POV isn't in it.** The physical step backward is the emotional content. Kuze's exclusion is shown by *where he stands*.
- **The pull-back paragraph is interpretive**, not descriptive. Never write "Everyone greeted Amamiya enthusiastically." The reader just watched that. Write what Kuze makes of it.

### 5.3 Unison lines

When two or more characters say the *same* thing together, the LN convention is doubled or tripled quotation marks:

> ""No way!""
>
> """Guess so."""

Use this for crowds, for cliques speaking in chorus, and for comedic synchrony (two rivals shouting the same denial). Keep it rare, at most once or twice a chapter, or it becomes a gimmick. At a climax it can escalate into a chant; see [Emotional Dialogue §6](emotional-dialogue.md#6-chants-and-crowd-pressure).

### 5.4 Overheard gossip

A cousin of the burst is **gossip at a distance**: the POV hears fragments from across the room. Render it as short, disconnected lines. Some are cut off mid-sentence, and none are attributed:

> "Did you see them at the station yesterday--"
>
> "No way, Tachibana-san? With *Kuze*?"
>
> "I heard she--"
>
> "Seriously~ that's so gross."
>
> Kuze kept his eyes on his textbook. The words on the page had stopped meaning anything several lines ago.

The cut-off dashes make it feel overheard. The final narration paragraph shows the effect without naming the feeling.

## 6. The silent reply: `"..."`

The reference novel uses a standalone `"..."` roughly four times per chapter. It is the most important piece of punctuation in the voice, and it is the purest dialogue line there is.

### 6.1 What silence can mean

| Context | What `"..."` says |
|---|---|
| After an accusation | Refusal to dignify it, or guilt |
| After a confession of feeling | Shock, or the inability to answer |
| After a joke | Deadpan, "that wasn't funny" |
| In a monologue-and-silence duet | Listening, being broken open |
| Alone, reading a post | Speechless disgust, or hurt |
| From the POV's crush | Something the POV can't read, and fears |

The meaning comes from **what's around it**. The paragraph after the silence decides what it was.

### 6.2 Three ways to follow a silence

1. **Nothing.** Cut straight to a new section or a scene skip. The silence is the ending. This is the strongest option and the one to use most rarely.
2. **A gesture, as its own paragraph.** `"..."`, then a new paragraph: *Kuze looked away.* The body finishes the sentence the mouth refused.
3. **Another character reacts to the silence.** `"..."`, then `"Say something!"` Now silence is an action that provokes.

### 6.3 Silence in sequence

Two silent characters facing each other is a standoff:

> "..."
>
> "..."
>
> The clock above the blackboard ticked, loud as a dropped tray.

Keep it to two or three `"..."` lines at most in a row, unless you're doing the confidant duet (see [Emotional Dialogue §4](emotional-dialogue.md#4-the-monologue-and-silence-duet)), where long runs are deliberate.

### 6.4 Don't

- Don't write `"..." Kuze said nothing.` That is redundant, since the ellipsis already said nothing, and it breaks the pure-line rule twice.
- Don't use `"..."` as a filler beat because you don't know what comes next. Each one should be a choice the character is making.

## 7. Interruptions

The cut-off mark is `--` (or `—`; pick one per story and stay consistent). **In dialogue, it only marks speech that is cut off or interrupted.** In narration, it only marks a thought that breaks off. Never use it for asides, appositives, or dramatic pauses in narration; that is a Western-literary tic this voice avoids (see [Anti-Robotic](../revision/anti-robotic.md) and [Punctuation & Typography](../core/punctuation-and-typography.md)).

The LN form:

> "Hey, Tachibana-san, about yesterday--"
>
> "Shut--up!"

Or with the interrupter arriving:

> "I was going to say that Kujou-san is actually--"
>
> "Everyone! Let's hit the next shop!"
>
> Momo's voice cut through the air, bright as a camera flash. Whatever Hina had been about to say was gone.

### 7.1 Interruption as plot

Interruptions aren't just realism. In this voice they are often **engineered**. A character deliberately cuts someone off to stop a reveal. The POV should notice the timing:

> Twice now. Twice, the moment someone said Kujou's name, Shirasagi had needed to go somewhere urgently.
>
> Was that coincidence?

This turns a punctuation habit into a clue. The mastermind thread ([Series Planning](../structure/series-planning.md)) lives on moments like this.

### 7.2 Self-interruption

A character cuts themselves off, usually from embarrassment:

> "It's not like I bought this for you, I just had an extra, and it's not like I remembered you like black coffee or anyth-- Just take it!"

The dash lands right at the moment of accidental honesty. This is the tsundere's natural rhythm. See [Character Voices §3](character-voices.md#3-archetype-speech-profiles).

## 8. Banter mechanics

### 8.1 Snap-back rhythm

The protagonist's default comic weapon is **the flat correction**: an emotional accusation, then a logical, too-precise reply, then outrage, then an even flatter reply.

> "You told me to shut up!"
>
> "I told you the library has a rule about volume."
>
> "That's the same thing!"
>
> "It's not."
>
> "It IS!"
>
> "It's on the sign."

The escalation curve is lopsided: one character's intensity rises while the other's falls. The joke is the gap. Rules:

- The flat speaker's lines get **shorter** as the other's get louder.
- End on the flat speaker, or on a physical action from the loud one (a smack, a stomp, a puffed cheek) in its own paragraph.
- Don't explain the joke in narration afterward.

### 8.2 Boke and tsukkomi

Japanese comedy's two-role structure maps perfectly onto LN banter. The **boke** says something absurd, and the **tsukkomi** corrects it with a sharp retort (often with a smack). Daichi is a natural boke and Kuze a natural tsukkomi:

> "Mina. Serious question. If you had to be a vending machine drink, which one?"
>
> "I'd rather not be a drink."
>
> "I'd be corn soup. Warm, surprising, nobody asks for me, but I'm there."
>
> "That's the saddest thing you've ever said."
>
> "Right? Deep, huh."

Kuze's deadpan tsukkomi is lower-energy than the classic anime slap. That's the character. See [Tone & Comedy](../core/tone-and-comedy.md) and [Rom-Com & Comedy](../genres/romcom-and-comedy.md).

### 8.3 Scoring the joke

A signature move: the protagonist **grades** a friend's joke.

> "Got hit by alien slime in the war."
>
> "Fifteen points."
>
> "Up from two!? I'm improving!"

This makes the friendship visible (you only grade jokes for people you like), keeps Kuze in deadpan, and gives the friend a comic comeback. Make it a running gag with an escalating scoreboard across chapters.

### 8.4 The needle and the counter-needle

Rival exchanges trade barbs of **equal length and escalating precision**:

> "You're seriously annoying. No wonder you're not popular."
>
> "You're not exactly beloved yourself."
>
> "I'm plenty popular, thank you."
>
> "..."
>
> Annoyingly, that was true.

The POV loses the round, and admits it in narration. Readers trust a narrator who admits losing.

### 8.5 Call and callback

Plant an exchange early; return to it later with the charge reversed:

- Ch. 3: Rin mocks Kuze for drinking black coffee ("Trying to act mature?").
- Ch. 20: Rin hands him a can of black coffee without a word. He notices she remembered.
- Ch. 38: Kuze, in the hospital corridor, buys two cans of black coffee. She drinks hers without complaint.

The dialogue callback carries emotion without anyone stating it.

## 9. Dialogue that carries subtext

Characters in this voice **rarely say what they mean**, and the narrator obsessively tries to decode what they *did* say. So the dialogue needs things worth decoding.

### 9.1 Plant asymmetries

Give the POV character something to catch:

- **The addressee shift.** Amamiya greets "Hina, morning" and then adds "...and Kuze? Morning," with a question mark on the name.
- **The inclusion slip.** "Want me to grab drinks for you *both*?", and later no offer when Kuze is alone.
- **The telling verb.** In a Chirp post, "I got them to make up" instead of "they made up".
- **The first question.** Not "What are you doing here?" but "You came *with Hina*?"

Each of these is an ordinary line on the surface. The narration pulls it apart, quoting the phrase back in *italics* (§2.4). See [Inner Monologue](../core/inner-monologue.md) for the dissection pattern.

### 9.2 Let characters dodge

When cornered, characters in this genre dodge in recognizable ways:

| Dodge | Sample |
|---|---|
| Change of subject | "A-Anyway! Why are you being so polite, Kuze-kun?" |
| Flimsy excuse | "I was just checking the floor for, um, dangerous things!" |
| Appeal to the lead | "Haruto-kun, Kujou-san's saying weird stuff again~" |
| Counterattack | "Why do *you* care, anyway?" |
| Fake cheer | "I'm totally fine! Haha!" |
| Silence | `"..."` |

The POV character notices the dodge, and usually lets it go. Letting it go is characterization too.

### 9.3 Don't make characters explain themselves

The most common robotic failure: characters speak in full, self-aware psychological sentences.

- **Robotic:** "I feel conflicted because I care about you but I'm also afraid of being hurt again."
- **In voice:** "Just-- forget it. Forget I said anything, idiot."

Real people, and good anime characters, protect themselves when they speak. The truth leaks through the gaps. See [Anti-Robotic](../revision/anti-robotic.md).

## 10. Pacing a conversation scene

### 10.1 The shape

A typical 1,000-word conversation scene in this voice:

1. **Opening line of dialogue**, often in media res (~1-3 lines)
2. **Quick orientation**: who, where, one portrait detail if someone new (~2-4 short sentences, in narration paragraphs)
3. **Stack** (6-15 lines)
4. **POV analysis** of one line from the stack (~80-200 words of monologue)
5. **Terse reply** from the POV
6. **Escalation stack** (6-15 lines)
7. **A tilt**: an interruption, an arrival, a silence, or a reveal
8. **Section ends**

### 10.2 Where the monologue interrupts

Never interrupt a comic stack with analysis. Let the joke finish. Interrupt **after** a line that stings, when the POV would naturally go quiet and think. The analysis should feel like time slowing down in his head while the room keeps moving.

A good transition back out of monologue is someone else's voice cutting in:

> Was it jealousy? Or was it something uglier than that, something he didn't have a name for yet?
>
> "Hey. Hey, Kuze. You listening?"
>
> "No."
>
> "At least lie!"

### 10.3 Length of individual lines

- Median spoken line: **4-12 words**.
- Long speeches (40+ words) are reserved for: the righteous lead's speech, the confidant's thesis, the bully's mockery, the outburst. Each is a set piece.
- The POV's median line should be *shorter* than everyone else's. His words are rationed. When he finally talks at length, it means something.

## 11. Phone calls, texts, and posts

- **Phone calls**: open with a sound line (*Ring, ring, click.*), then dialogue as normal pure lines. The voice on the other end can be described once, in its own narration paragraph, by its texture ("Her voice was hollow, scraped thin").
- **Texts and DMs**: set off as their own lines, with the sender's name and message, with no quotation marks.
- **Chirp posts**: username line, post line, `(Tap to view photo)`.

Full rules and formatting are in [Social Media & Texts](../setting/social-media-and-texts.md).

## 12. Worked example: all mechanics in one scene

> "Kuze-kun, got a second?"
>
> Hina's face appeared over the top of his textbook, upside down, ponytail swinging.
>
> "No."
>
> "Ugh, you're so cold! Just one second! One!"
>
> "You've used three already."
>
> "Those don't count!"
>
> She dropped into the empty seat in front of him, turned it backward, and folded her arms across the backrest.
>
> "So. Haruto's birthday is next week, right? We're all doing a surprise thing. And, um."
>
> "..."
>
> "Um!"
>
> "You said that."
>
> "I'm *building up* to it!"
>
> She puffed her cheeks.
>
> "Would you... maybe... help carry the cake? You're in the go-home club, so you're free, right?"
>
> *So you're free, right.*
>
> There it was. Not *we'd like you there*. Not *you should come*. He was free, and so he was useful. Transport. A pair of hands.
>
> Was that unfair to her? Probably. Matsuri didn't have a calculating bone in her body, or at least none that he'd found. But the question had been built by someone. And he could guess whose idea it had been to make the loner carry the cake: the person who needed the party to have no second boy in it who mattered.
>
> "Sure."
>
> "Really!? Yay! Thanks, Kuze-kun!"
>
> She bounced up, already turning, already waving across the room.
>
> "Haru! He said yes--"
>
> She stopped. Clapped both hands over her mouth.
>
> "...I mean. Nobody. Said. Anything."
>
> "..."
>
> From across the room, Amamiya looked up. For just a moment, too short for anyone else to notice, he didn't smile.

**What it uses:** an entrance by action paragraph; every quote alone on its line; snap-back ("You've used three already"); a strategic `"..."`; the quoted-back phrase in italics as the monologue trigger (*So you're free, right.*), with no quotation marks, because it isn't live speech; a hypothesis with self-suspicion; the terse "Sure."; a self-interruption with `--`; the silence at the reveal; and a section-ending tilt carried by a look, not a line. Count the paragraphs that mix a quote with narration: zero.

## 13. Dialogue checklist

- [ ] **Every paragraph containing a quotation mark contains only the quote.** Zero mixed paragraphs (§2).
- [ ] No speech tags anywhere in story prose, "said" included.
- [ ] Quoted-back phrases in narration are in italics, not quotation marks.
- [ ] Dialogue is 40-55% of the chapter's words (35% floor only for a planned introspective chapter).
- [ ] Stacks never exceed the safe length for the number of speakers.
- [ ] Every character in the scene could be identified from one line alone.
- [ ] At least one line contains an asymmetry the POV can dissect.
- [ ] Every `"..."` is a deliberate choice, followed by nothing, a gesture paragraph, or a reaction.
- [ ] Dashes appear only on cut-off speech or a thought that breaks off. No dash asides in narration.
- [ ] No character explains their own feelings in full therapy-speak.
- [ ] The POV speaks less than anyone else in the scene.
- [ ] The scene ends on a tilt, not a summary ([Hooks & Cliffhangers](../structure/hooks-and-cliffhangers.md)).

## 14. Appendix: quick fixes for common dialogue drafts

| Draft symptom | Quick fix |
|---|---|
| Lines like `"...," she said.` or `"...," he paused, "..."` | Delete the tag. If attribution is lost, add an action paragraph before the line, or sharpen the line's tic |
| `Rin crossed her arms. "Whatever."` in one paragraph | Split into two paragraphs: the action, then the quote |
| `"Whatever." Rin crossed her arms.` in one paragraph | Split into two paragraphs: the quote, then the action |
| A split quote with a beat in the middle | Two quote paragraphs with the beat as its own paragraph between them, or cut the beat |
| Narration quotes back a line using quotation marks | Switch the quoted-back phrase to italics |
| A scene opens with three paragraphs of narration before anyone talks | Move the first line of dialogue to the top; fold the setup into a two-sentence orientation after it |
| The POV answers everything at length | Replace every second reply with a short word or `"..."` |
| Characters greet, exchange pleasantries, then talk | Cut the greetings. Enter late, on the line that matters |
| Two characters agree with each other for several lines | Give one of them a counter, a dodge, or a joke. Agreement is dead air |
| Narration repeats what a line just said | Replace it with the POV's interpretation of the line, or delete it |
| A long speech with no interruptions | Break it with one gesture paragraph or one listener reaction every 3-4 sentences, unless it's a set piece |
| Dialogue ratio under 40% | Convert summarized exchanges ("They argued about the rubric") back into live stacks; add a chatter burst; add a scene with a second character rather than more reflection |
