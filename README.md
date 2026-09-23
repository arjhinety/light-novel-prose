# light-novel-prose

A provider-agnostic skill library for writing English fiction in the voice of a **translated Japanese light novel / web novel**, the anime-style school rom-com and drama register. It adapts to harem, comedy, ecchi (adults only), fantasy, isekai, villainess, action, mystery/horror, sports/idol, and romance.

It is built around one obsession: **flowing, human, non-robotic prose** that keeps the Japanese texture without machine-translation stiffness or generic-AI polish.

- ~50 linked Markdown files, 150k+ words
- No tool calls, no vendor APIs, no scripts. Any model that can read Markdown can use it.
- `SKILL.md` is the router, `INDEX.md` is the map, and `PROMPT.md` is a single-file condensed version

## 1. Layout

```
light-novel-prose/
├── SKILL.md          router + workflow (entry point)
├── INDEX.md          every file, what it covers, reading paths
├── PROMPT.md         condensed standalone system prompt
├── core/             the voice: style bible, POV, monologue, rhythm, description, tone, diction, punctuation
├── dialogue/         mechanics, honorifics, character voices, emotional dialogue
├── cast/             story roles, character design, dere types, other tropes
├── genres/           genre index + 11 genre guides
├── setting/          school life, social media & texts
├── scenes/           scene playbook, emotional climaxes
├── structure/        chapters & sections, arcs, series, hooks
├── revision/         anti-robotic, MTL vs natural, revision checklist
├── examples/         annotated passages, before/after, 3 full sample chapters
└── templates/        story bible, chapter plan, character sheet
```

## 2. Installing it

The folder follows the open **Agent Skills** convention (a folder with a `SKILL.md` containing YAML frontmatter `name` and `description`). Tools that support that convention can load it directly; for anything else, point the model at `SKILL.md` or paste `PROMPT.md`.

| Environment | How |
|---|---|
| **Claude Code / Claude apps** | Copy the folder to `~/.claude/skills/light-novel-prose/` (personal) or `.claude/skills/` in a project. |
| **OpenAI Codex CLI** | Copy it to `~/.codex/skills/light-novel-prose/` if your version supports skills. Otherwise add to `AGENTS.md`: *"For fiction in light-novel style, read `light-novel-prose/SKILL.md` and follow it."* |
| **Gemini CLI** | Add to `GEMINI.md`: *"For light-novel / anime-style fiction, read and follow `light-novel-prose/SKILL.md` and the files it links."* |
| **Cursor / Windsurf / Cline / Continue** | Add a rule file (e.g. `.cursor/rules/light-novel.mdc`) that says to read `light-novel-prose/SKILL.md` for fiction requests, and keep the folder in the workspace. |
| **Aider / other file-aware agents** | Add `SKILL.md` plus the core files to the read-only context. |
| **ChatGPT / Gemini / any chat UI** | Paste `PROMPT.md` into custom instructions / a system prompt, or upload the folder's files to a Project / Gem / custom GPT knowledge base with `SKILL.md` as the entry instruction. |
| **API use (any provider)** | Put `PROMPT.md` in the system prompt. For higher fidelity, also append `core/style-bible.md`, `core/rhythm-and-flow.md`, `revision/anti-robotic.md`, and the relevant genre file. |

## 3. Using it

Example requests:
- "Write chapter 1 of a light novel about a loner who keeps noticing why the popular guy is popular."
- "Continue from here in the same style: [paste]."
- "Rewrite this scene so it reads like a translated LN and not like AI."
- "Isekai slow-life, kuudere elf heroine, comedic tone, 3,000 words."
- "Give me a yandere childhood friend who's scary but sympathetic."

## 4. Provenance

The voice was derived from close reading of a 100-chapter translated school-drama web novel (measured dialogue ratio, sentence-length distribution, silence beats, honorific frequency, monologue patterns). All example prose in this library is original, and no source text is reproduced beyond short analytical fragments.

## 5. Content policy baked in

Suggestive content only between unambiguous adults, non-sexual embarrassment comedy only for high-school characters, and nothing explicit. See `genres/ecchi-and-fanservice.md`.
