# Document Index

Master map of this project. Update this file whenever a document is created, moved to `/final`, superseded, or when a decision is recorded.

## Structure

| Path | What it holds |
|---|---|
| `README.md` | Human-facing overview for GitHub — what this repo is and how to use it |
| `Project Instructions.md` | The rules — governs all work in this project |
| `INDEX.md` | This file — the map; start here |
| `glossary.md` | Canonical terminology and acronyms |
| `config/config.yaml` | Runtime parameters: model, temperature, limits, endpoints — plus the complete paths map (all folders + INDEX.md + glossary.md) |
| `prompts/` | Reusable zero-/few-shot task prompts, referenced by skills (see registry below) |
| `drafts/` | Documents in progress |
| `final/` | Completed, reviewed docs — everything here is current |
| `archive/` | Superseded docs — kept for history, never rely on these |
| `decisions/` | Decision records (what was chosen, why, alternatives rejected) |
| `references/sources/` | External material docs depend on: vendor docs, specs, manuals (versioned) |
| `references/reading/` | External material kept for convenience: articles, tutorials, threads |
| `assets/images/` | Screenshots referenced by docs |
| `assets/diagrams/` | Diagrams referenced by docs |
| `templates/` | Skeletons every new document starts from (see below) |
| `skills/doc-writer/` | Skill: document lifecycle procedure (create → finalize → archive) |
| `skills/doc-reviewer/` | Skill: quality checklist run before finalizing any doc |
| `notes/` | Scratch notes, ideas, TODOs not yet formalized |

## Filing rule for references/

Test: **"If this external thing is updated or deleted, must I re-verify one of my docs?"**
- Yes → `references/sources/` (evidence; name as thing-version-topic, e.g. `nginx-1.27-config-reference.pdf`)
- No → `references/reading/` (background; name as format-topic, e.g. `blog-zfs-vs-btrfs.md`)

References feed docs; they never replace them. A fix found in a saved thread still gets its own troubleshooting doc.

### Academic papers

Papers (survey, research, review, preprint, thesis, whitepaper) can live in **either** folder — the same dependency test decides, not the paper type:

- A research paper whose method/results a doc relies on → `sources/`
- A survey read for orientation, nothing depends on it → `reading/`

Name papers as `paper-<type>-<year>-<firstauthor>-<topic>.pdf`, e.g.
`paper-survey-2024-zhang-vector-databases.pdf`, `paper-research-2017-vaswani-attention.pdf`.
The type lives in the filename, so both folders stay flat — no per-type subfolders.

Register every saved paper in the References table below.

## Templates

| Template | Use for |
|---|---|
| `templates/how-to.md` | Step-by-step procedures (prerequisites → steps → verify → rollback) |
| `templates/reference.md` | Canonical facts: versions, paths, configs, common commands |
| `templates/troubleshooting.md` | Symptom → cause → fix records |
| `templates/decision.md` | Decision records: context, decision, rejected alternatives |

## Prompts

Reusable task prompts. Naming: `snake_case_prompt.txt`. Each file starts with a
header block (PROMPT / TYPE / USE / INPUT / CONFIG). Runtime values come from
`config/config.yaml` — prompts never hardcode model settings.

| Prompt | Type | Does |
|---|---|---|
| `prompts/extract_metrics_prompt.txt` | zero-shot | Pulls quantitative facts from a document into a table |
| `prompts/format_to_json_prompt.txt` | zero-shot | Converts unstructured text into strict schema-matching JSON |
| `prompts/glossary_entry_prompt.txt` | few-shot | Turns a new term + context into a canonical glossary row |

## Final (current, trustworthy)

| Document | Topic | Updated | Tags |
|---|---|---|---|
| _none yet_ | | | |

## Drafts (in progress)

| Document | Topic | Updated | Blocking on |
|---|---|---|---|
| _none yet_ | | | |

## Decisions

| Decision | Date | Status |
|---|---|---|
| _none yet_ | | |

## References (papers and key external material)

| File | Type | Folder | Used by (docs) |
|---|---|---|---|
| _none yet_ | | | |

Type: survey, research, review, preprint, thesis, whitepaper, vendor-doc, spec, article.

## Archived (superseded — do not rely on)

| Document | Superseded by | Archived |
|---|---|---|
| _none yet_ | | |
