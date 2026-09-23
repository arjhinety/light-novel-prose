# Fan Fiction & Canon

> **Purpose:** a protocol for writing in an existing series (fan fiction, parody, crossover, alternate universe) so that the LN voice sits on top of canon characters without breaking them.
> **Load when:** the request names an existing anime, manga, light novel, game, or web novel, or uses characters the user didn't invent.
> **Related:** [POV Temperaments](../core/pov-temperaments.md), [Honorifics & Address](../dialogue/honorifics-and-address.md), [Character Design](../cast/character-design.md), [Dere Types](../cast/dere-types.md), [Harem](../genres/harem.md), [Story Bible template](../templates/story-bible.md), [Character Sheet template](../templates/character-sheet.md), [Dialogue Mechanics](../dialogue/dialogue-mechanics.md), [Revision Checklist](../revision/revision-checklist.md), [Tools](../tools/README.md)

## 1. Why fan fiction needs its own protocol

The rest of this library assumes you are building a cast from scratch. Fan fiction inverts that. The cast already exists, readers already love it, and they will notice every wrong detail before they notice any good sentence.

Test runs of this library on a harem-series fan fiction request showed the same five failures across different models:

| Failure | What it looked like | Why it happens |
|---|---|---|
| **Default-cast bleed** | A canon heroine was given the library's example tsundere's "silver-ash hair" | The model absorbed the example cast and mistook it for a style rule |
| **Invented canon** | A shy heroine was given a stuffed-animal companion she doesn't have, written as if canon | The model filled a gap with a plausible trope instead of admitting the gap |
| **Wrong naming convention** | Narration called everyone by surname because the library's default says "anchor on the surname", but the series uses given names | A house rule overrode the source's convention |
| **Archetype flattening** | A loud, prideful tsundere became apologetic and self-effacing | The model wrote "a shy girl" from the scene's needs instead of the character's canon core |
| **Fake extras** | New "girlfriends" were invented and named in a way that implied they were canon | The model was padding a harem |

None of these failures is about prose quality. A chapter can have perfect rhythm and still be unreadable to a fan because the heroine has the wrong hair and the wrong personality. **In fan fiction, canon fidelity comes before style.** The LN mechanics are the delivery system; canon is the payload.

## 2. The order of operations

Do these steps in order, before drafting a single sentence of prose:

1. **Identify the source.** Name the series, its medium (manga, LN, anime, game), and, if relevant, the translation you're following (official localization or fan translation, since names and honorifics differ).
2. **Pick the cast** for this chapter. Fewer is safer. Three well-drawn canon characters beat seven vague ones.
3. **Write a canon sheet for each character** (§3), with confidence markers (§4).
4. **Record the source's conventions** (§5): name order, narration naming, honorifics, POV style, and tone.
5. **Decide the POV temperament.** If the source's protagonist isn't a cynical loner, load [POV Temperaments](../core/pov-temperaments.md) and re-aim the monologue engine to match.
6. **Place the chapter in the timeline** (§10): after which events, and which relationships exist yet.
7. **Write the chapter plan** (see [Chapter Plan template](../templates/chapter-plan.md)), then draft.
8. **Run the canon pass** (§14) before the usual [Revision Checklist](../revision/revision-checklist.md).

Skipping step 3 is the root cause of almost every failure in §1.

## 3. The canon sheet

Fill one per canon character. Keep it short, since it's a working document, not an encyclopedia entry.

```
CANON SHEET: <Character name as the source writes it>
Source / version:        <series, medium, translation followed>
Role in source:          <e.g. "second heroine", "rival", "the lead's best friend">
Appearance (anchor):     <1-3 details fans would recognize instantly>   [C/L/U]
Signature item or look:  <hairpin, glasses, a specific bag>              [C/L/U]
Core trait:              <the one thing that must be true in every scene>
Surface behavior:        <how the core trait shows: loud? deadpan? formal?>
Speech style:            <register, sentence length, verbal tics, catchphrase>
What they call the lead: <exact form, with honorific>                   [C/L/U]
What the lead calls them:<exact form>                                   [C/L/U]
Relationships in play:   <who they're close to, rivals with, and so on>
Running gags:            <1-3 recurring jokes attached to them>
Do-not list:             <things that would be out of character>
Uncertain / skip:        <facts you're unsure of that you'll leave out>
```

Field guidance:

- **Appearance (anchor)** is not a full portrait. Pick the 1-3 details a fan would recognize from across a room. The [portrait formula](../core/description-and-portraits.md) still applies, but in fan fiction it's used to *confirm*, not to *introduce*. Readers already know what she looks like, so one anchor detail on entry is enough.
- **Core trait** is the most important line on the sheet. Write it as a sentence the character would never violate: "She is proud and will never admit she's jealous out loud, even when it's obvious." Every line of her dialogue gets tested against it.
- **Surface behavior** is how the core trait leaks out. Two tsunderes can share a core trait and differ completely on the surface: one shouts, one goes silent and kicks things.
- **Speech style** should be specific enough to identify the speaker without a tag, because under the [pure dialogue lines rule](../dialogue/dialogue-mechanics.md) most lines will have no tag at all.
- **Do-not list** is where you write the failure you're most afraid of: "Never makes her apologize repeatedly. Never makes her quiet."

## 4. Confidence marking and the underspecify rule

Mark every factual field with a confidence level:

| Mark | Meaning | How to use it in prose |
|---|---|---|
| **C** (certain) | You know this reliably: it's central, repeated, and iconic | Use it freely |
| **L** (likely) | You're fairly sure, but it could be wrong or version-dependent | Use it lightly, once, in a non-load-bearing spot |
| **U** (unsure) | You don't know, or you know you're guessing | **Don't write it.** Leave it out. |

**The underspecify rule:** when you're unsure of a fact, write around it instead of inventing it. If you don't know a heroine's hair color, don't give her one. Anchor her with something you *are* sure of: her voice, her catchphrase, the way she enters a room. Readers forgive a missing detail. They don't forgive a wrong one.

Useful underspecify moves:

- **Describe action instead of appearance.** "She swept in like the room had been waiting for her" says more than a guessed hair color.
- **Describe effect instead of fact.** "The hairpin she never went anywhere without" works without naming its shape.
- **Let other characters carry it.** A friend's reaction ("You're wearing *that* again?") implies a signature look without specifying it.
- **Keep offstage what you can't render.** If you're unsure how a character speaks, give her a small role in this chapter.

If the user has supplied reference material (wiki pages, their own notes, a pasted chapter), that material is **C** for anything it states clearly. It outranks your memory, so read it before filling the sheet.

## 5. Naming, honorifics, and conventions

### 5.1 Follow the source's naming convention in narration

The library's default (anchor the POV on their surname, "Kuze thought") exists because the reference novel does it. **Many series don't.** Harem and rom-com series often narrate with the lead's given name, and fans think of the heroines by given name. Before drafting, answer:

- How does the source's narration refer to the POV character: given name, surname, or first person?
- How does the narration refer to the other characters?
- How do fans refer to them? (If the narration is first person, fan convention decides third-person narration.)

Then apply those answers consistently. A chapter that calls a heroine "Hanamura" in narration when every fan calls her "Rika" reads as if the writer has never met her.

### 5.2 Honorifics follow the source, not the library's defaults

The honorific system in [Honorifics & Address](../dialogue/honorifics-and-address.md) is a general map. In fan fiction, the source's specific pairings override it. If a heroine calls the lead by a nickname with no honorific in canon, she does so here too, even if the general rule says a girl in her position would use -kun.

Build an **address ledger** from the canon sheets before drafting: every speaker and listener pair, with the exact form. A cast of five heroines and one lead produces at least ten entries. Check every line of dialogue against it in revision.

### 5.3 Translation variants

Names and honorifics can differ between the official localization and fan translations. Some localizations drop honorifics; some translate nicknames. Pick one version (the user's, if they say; otherwise the most widely read English version you're confident of) and stay in it. Don't mix a localized nickname with a fan-translation honorific in the same chapter.

### 5.4 Name order

Japanese order (surname first) or Western order (given name first) should match the version you're following. Keep it consistent, including in any chapter title or in-world text.

## 6. Tone matching: layering the LN voice on canon

The LN mechanics (short beats, pure dialogue lines, silence beats, numbered sections, the analytical monologue) are compatible with almost any source. What changes is the **tone dial**, and that is set by the source, not by the library's default.

| Source tone | Keep from the library | Adjust |
|---|---|---|
| Absurd, high-energy harem comedy | Stacked banter, group chatter bursts, deadpan beats, callbacks | Monologue aims at *effort and affection* instead of suspicion. Earnest peaks come fast and unironically. |
| Cynical school drama | Nearly everything, as written | Nothing major. This is the library's home register. |
| Gentle slice of life | Rhythm, silence beats, small observed details | Lower the comedy ratio, soften the verdict lines, and let scenes breathe longer |
| Action / fantasy | Short beats, tactical monologue | Follow the source's power system exactly, and don't invent abilities |
| Melodrama / tearjerker | Silence beats, simple repetition at peaks | Slow the long exhales, and cut the meta-humor |

The rule of thumb: **the source decides *what* is felt, and the library decides *how* it reads on the page.** If a source's protagonist is relentlessly sincere, a chapter in which he's suspicious of the heroines is out of character no matter how good the suspicion sounds.

For a sincere lead specifically, the analytical engine doesn't disappear. It turns around: instead of noticing the asymmetry that suggests a hidden motive, he notices the tiny thing each heroine did for him that nobody else caught. See [POV Temperaments](../core/pov-temperaments.md) for the full treatment.

## 7. Characterization and the OOC problem

"OOC" (out of character) is the fan term for a canon character acting against their established nature. It is the most common complaint about fan fiction and the easiest one to prevent.

### 7.1 The flip test

For every heroine, find one line she says in your draft and ask: *if I removed the name, would a fan know who said it?* If not, the line is generic. Rewrite it using her speech style and core trait from the canon sheet. Under the pure dialogue lines rule this matters even more, because there are no tags to rescue an ambiguous line.

### 7.2 Show the core trait early

Each canon character's core trait should be visible within their first few lines on the page. Fans check. A tsundere's first line should have some tsun in it; a deadpan character's first line should be deadpan.

### 7.3 Scene needs versus character needs

The most common OOC failure: the plot needs someone to feel insecure, so the writer makes whoever is handy insecure, whether or not she canonically would. The fix is to **route the need through the character's own nature**. A proud tsundere can be insecure, but her insecurity comes out as anger, a challenge, or a boast that's too loud, not as quiet apologies.

| Plot needs | Generic (OOC) execution | In-character execution for a proud tsundere |
|---|---|---|
| She feels her gift is worse than the others' | She apologizes and tries to leave | She declares it's obviously the best and dares anyone to say otherwise, too loudly |
| She's moved by the lead's words | She cries and thanks him softly | She shouts at him to stop saying embarrassing things, and she's red to the ears |
| She wants him to choose her gift first | She asks shyly | She shoves it at him and says it's not like she *wants* him to eat it first |

### 7.4 Common flattening patterns to avoid

- **The sweetening:** every heroine becomes kind, soft, and supportive. Canon heroines have edges, and the edges are why fans love them.
- **The convergence:** all heroines start to sound alike by the second half of the chapter. Re-read each one's lines in isolation.
- **The borrowed arc:** a canon character is given an emotional arc that belongs to someone else in the series.
- **The lead's personality drift:** a sincere lead becomes snarky, or a snarky lead becomes sincere, because the library's default POV leaked in.

## 8. The default-cast firewall

The library uses an original example cast (Minato Kuze, Rin Tachibana, Sayo Kujou, Hina Matsuri, and others) so that its examples stay consistent. **That cast is example material only.** In fan fiction:

- **Never transfer an example character's traits to a canon character.** A canon tsundere does not get Rin's silver-ash bob, kendo club, or canine grin, even though both are tsunderes.
- **Never import the example cast's names, school, club, or social app** (Seiryou, Class 2-3, "Chirp") into a canon setting. Use the source's school, class, and in-world details, or keep them generic.
- **Treat archetype files as psychology, not appearance.** [Dere Types](../cast/dere-types.md) tells you how a tsundere's denial works. It doesn't tell you what any particular tsundere looks like.
- **If you catch yourself writing a detail you can't source, check whether it came from the example cast.** That's the usual origin of an invented detail.

## 9. Original additions: labeling and restraint

Fan fiction can add things. It must not pretend they're canon.

- **Original characters (OCs):** fine in small roles (a classmate, a shopkeeper, a rival club member). Give them names that don't collide with canon characters, and don't present them as canon members of a canon group. In a harem series, **never invent new members of the canonical harem** unless the user asks for it. If the story needs "more girlfriends" offstage, reference them generically ("the rest of the group chat exploded") instead of inventing named ones.
- **Original props and events:** invent freely at the scene level (a cooking contest, a broken vending machine, a school event). Don't invent *character-defining* props, such as a companion object or a signature item a character "always" carries, unless canon has it.
- **Labeling:** if the user asks what's canon, be honest. If you deliver bible notes after the chapter (see [SKILL.md](../SKILL.md) delivery rules), list original additions there: "Original to this chapter: the cooking contest, the class rep from 1-4."

## 10. Timeline and continuity

Decide where the chapter sits relative to canon:

- **In-gap:** set between canon events, and consistent with both. It's the safest option; only relationships established by that point exist.
- **Post-canon:** after the latest events you're confident of. Say so, and don't assume details of arcs you don't know.
- **Alternate universe (AU):** canon characters in a changed setting (a café AU, a fantasy AU). Personalities and relationships stay canon; the setting changes. State the AU premise in the first section so readers adjust.
- **Divergence:** canon until a specific event, then something happens differently. Name the divergence point for yourself in the plan.

The practical rule: **don't reference events you're not sure happened**, and don't make one character aware of another if that meeting might not have happened yet at this point in the timeline.

## 11. Crossovers

When two series meet:

1. Write canon sheets for both casts, with conventions recorded separately (their naming and honorific systems may differ).
2. Decide whose **tone** governs the chapter, usually the POV character's series.
3. Keep each character's speech style intact. The comedy of a crossover often comes from one series' logic colliding with another's.
4. Don't let one series' power system or rules silently apply to the other's characters.

## 12. Not reproducing source text

Fan fiction borrows characters and worlds, not text.

- **Don't reproduce dialogue, narration, or scene sequences** from the source, even paraphrased closely.
- **A signature catchphrase** of a few words, used once as a character beat, is acceptable and often expected. A recreated scene isn't.
- **Don't retell canon events line by line.** If the chapter depends on a canon event, reference it in a sentence of narration and move on to your original material.
- **Invented chapter titles and in-world text** should be original too, not copied episode or chapter names.

## 13. Ensemble chapters in harem series

Harem series make fan fiction especially hard: many canon heroines, each with a devoted fanbase. The rules in [Harem](../genres/harem.md) apply, plus:

- **Screen-time budget.** For a 5,000-word chapter, plan 3-5 heroines with real lines. Assign each one at least one beat that shows her core trait and one moment with the lead. Give the extras a line each, or keep them offstage.
- **The equal-love constraint.** If the source's premise is that the lead loves every heroine equally, the chapter must honor it. The climax can't pick a winner. The payoff is usually the lead naming something specific and irreplaceable about each one.
- **Differentiation comes from canon.** Don't invent new differentiators. Use each heroine's canon speech style, core trait, and running gag. If two canon heroines are similar, choose scenes that expose their differences.
- **The lead's line to each heroine must be different in kind,** not just in content. One gets a joke, one gets a quiet sentence, one gets a physical gesture.

## 14. The canon pass (revision)

Run this before the general [Revision Checklist](../revision/revision-checklist.md):

- [ ] Every appearance detail on the page is marked **C** or **L** on a canon sheet. No **U** facts appear.
- [ ] No trait, name, place, or app from the library's example cast appears.
- [ ] Narration uses the source's naming convention consistently.
- [ ] Every address form in dialogue matches the address ledger.
- [ ] Each canon character passes the flip test on at least three of their lines.
- [ ] Each canon character's core trait shows within their first few lines.
- [ ] No invented character is presented as a canon member of a canon group.
- [ ] No character-defining prop was invented.
- [ ] The POV temperament matches the source protagonist.
- [ ] No source text is reproduced beyond a brief catchphrase.
- [ ] Original additions are listed after the chapter if you're delivering bible notes.

## 15. Worked example: an invented series

To avoid making claims about real series, this example uses an invented one. Treat it exactly as you would a real source.

**Source:** *The Library Committee Is a Battlefield* (an invented rom-com LN). The narration is close third on the lead, Aoi Minase, a sincere second-year boy who joined the library committee by accident. **The narration uses given names for everyone.** The tone is gentle comedy with earnest peaks. The lead is sincere, not cynical.

### 15.1 Canon sheets (abridged)

```
CANON SHEET: Tsukasa Hozumi
Source / version:        The Library Committee Is a Battlefield, LN
Role in source:          committee head, first heroine
Appearance (anchor):     silver-rimmed glasses she pushes up when annoyed   [C]
Signature item:          a red date stamp she carries everywhere            [C]
Core trait:              believes rules are a form of kindness; never raises her voice
Surface behavior:        kuudere, speaks in short, complete sentences, stamps things when flustered
Speech style:            formal, "Minase-kun", no contractions when upset
What she calls the lead: Minase-kun                                        [C]
What the lead calls her: Hozumi-senpai                                     [C]
Running gags:            stamps "OVERDUE" on things that aren't books
Do-not list:             never shouts; never giggles; never breaks a rule without a reason
Uncertain / skip:        her hair color (sources vary), her family
```

```
CANON SHEET: Nanami Egawa
Role in source:          gyaru classmate, second heroine
Appearance (anchor):     decorated nails, phone charm shaped like a book    [C]
Core trait:              loud about everything except what she actually cares about
Surface behavior:        teasing, nicknames, drags Aoi around by the sleeve
Speech style:            fast, slangy, tildes, calls him "Aocchi"
What she calls the lead: Aocchi                                            [C]
Do-not list:             never cruel; never stupid (she's secretly the best reader on the committee)
Uncertain / skip:        her club, whether she has siblings
```

Notice what's skipped. Tsukasa's hair color is marked uncertain, so the chapter never mentions it. Her glasses and stamp are certain, so they carry her visually.

### 15.2 A passage that follows the protocol

This passage applies the canon sheets, uses the source's given-name narration, the sincere-lead temperament, pure dialogue lines, and no dash asides.

> The return cart was supposed to hold thirty books.
>
> Nanami had loaded forty-one onto it and was now sitting on top of the pile.
>
> "Aocchi~ Push."
>
> "The cart has a weight limit."
>
> "It's a cart. Carts are brave."
>
> Tsukasa appeared at the end of the aisle. She pushed her glasses up with one finger. Aoi had learned, over two months on the committee, that this was the equivalent of anyone else slamming a door.
>
> "Egawa-san. Get down."
>
> "Senpai~ You wanna ride too?"
>
> "..."
>
> The red stamp came out of Tsukasa's blazer pocket.
>
> *Ka-chunk.*
>
> A small red OVERDUE now sat on the back of Nanami's hand.
>
> "Hey! I'm not a book!"
>
> "You are currently being stored on a book cart. The system does not distinguish."
>
> Aoi looked at the stamp, and then at Tsukasa's hand, which was shaking very slightly.
>
> She had stamped the back of Nanami's hand. Not her sleeve, not the cart. Her hand, gently, the way you'd stamp a library card for a first-year who was nervous about borrowing. Tsukasa never stamped anything hard. Aoi had never once seen her press down with her full weight, not even on the returns that were a month late.
>
> Was that the rule? Or was that just her?
>
> He decided it was her. He decided he liked knowing that.
>
> "Hozumi-senpai."
>
> "What is it, Minase-kun."
>
> "Thank you for going easy on her."
>
> Tsukasa's glasses went up again. Twice.

What the passage gets right:

- **Given names in narration** (Nanami, Tsukasa, Aoi), because the invented source does that. The library's surname default is overridden.
- **Address forms match the ledger:** "Aocchi", "Senpai~", "Egawa-san", "Minase-kun", "Hozumi-senpai".
- **Anchor details are only C facts:** the glasses, the stamp, the nails are implied, and hair color is never mentioned.
- **The sincere temperament:** Aoi's analytical move (noticing *how* she stamped) lands on kindness, not suspicion. His verdict line is "He decided he liked knowing that."
- **Pure dialogue lines:** every quoted paragraph holds only speech. Actions (glasses, the stamp) are separate paragraphs.
- **No dash asides in narration.** The one pause is a separate `"..."` line.
- **The core trait shows immediately:** Tsukasa's first move is a rule, delivered quietly. Nanami's first line is a nickname and a tilde.

### 15.3 The same beat written wrong

> Tsukasa Hozumi, her long silver-ash hair swaying, marched down the aisle. "Egawa-san!" she shouted, cheeks red. "Get down this instant--you'll break it!" She pulled out Mr. Bookworm, the plush owl she always carried, and hugged it nervously. Minase frowned. Why did she care so much? Was she jealous?

Every failure from §1 in five sentences:

- **Default-cast bleed:** "silver-ash hair" came from the library's example tsundere.
- **An unsure fact written anyway:** her hair color was marked **U**.
- **OOC:** she shouts, and her do-not list says she never raises her voice.
- **Invented character-defining prop:** "Mr. Bookworm, the plush owl she always carried".
- **Wrong naming convention:** "Minase" in narration, where the source uses given names.
- **Wrong POV temperament:** a sincere lead suddenly suspects a heroine of jealousy.
- **R1 violations:** dialogue and narration share paragraphs.
- **R2 violation:** a dash inside a line that also carries narration.

## 16. Quick checklist

- [ ] Source and version identified
- [ ] Canon sheet per character, with C/L/U marks
- [ ] Address ledger built
- [ ] Narration naming convention recorded
- [ ] POV temperament chosen from the source protagonist
- [ ] Timeline placement decided
- [ ] Cast limited to what the length can serve (3-5 heroines with lines per 5,000 words)
- [ ] Draft written with the canon sheets open
- [ ] Canon pass (§14) done
- [ ] General revision checklist done
- [ ] Original additions listed if delivering notes
