---
name: doc-writer
description: >
  Use this skill whenever the user wants to create, finalize, supersede, or
  archive a document in this project. Triggers include: "write a doc",
  "new how-to", "document this", "create a reference for", "record this
  decision", "add a troubleshooting entry", "this doc is done", "finalize",
  "this is outdated", "archive this". Covers the full document lifecycle:
  choosing the right template, filling front matter, saving to the correct
  folder, and updating INDEX.md. Do NOT use for reviewing existing docs —
  use doc-reviewer instead.
---

# Doc Writer

Workflow for creating and managing documents in this project. Always follow
`Project Instructions.md` for tone and constraints; this skill covers procedure.

This skill defines the ROLE and workflow only. Task-execution prompt text lives
in `prompts/` (see the Prompts registry in `INDEX.md`); runtime parameters
(model, temperature, limits) come from `config/config.yaml`. When a step needs
a task prompt — e.g. adding a glossary term via
`prompts/glossary_entry_prompt.txt` — load it from the file rather than
improvising, and never hardcode config values.

All folder and file locations named below (drafts, final, archive, decisions,
templates, references, INDEX, glossary) resolve through the `paths:` section of
`config/config.yaml`. If a path is ever changed there, this skill follows the
config — the names below are the defaults, not independent truths.

## Step 1 — Choose the template

| User wants to capture... | Use template | Type |
|---|---|---|
| A step-by-step procedure | `templates/how-to.md` | how-to |
| Canonical facts: versions, paths, configs, commands | `templates/reference.md` | reference |
| A problem and its fix (symptom → cause → fix) | `templates/troubleshooting.md` | troubleshooting |
| A choice made and why (alternatives rejected) | `templates/decision.md` | decision |

If the request spans multiple types, split into multiple documents — one topic
per document. Never invent a hybrid format.

## Step 2 — Create the document

1. Copy the chosen template. Never edit the template itself.
2. Fill ALL front matter fields: `title`, `status: Draft`, `updated` (today,
   YYYY-MM-DD), `tags`, `type`.
3. Name the file `lowercase-with-hyphens.md`.
4. Save to `drafts/` — except decision records, which go directly to
   `decisions/` with status `Accepted`.
5. Check every term against `glossary.md`. If a new term or acronym is
   introduced, add it to the glossary FIRST, then use it.
6. Mark anything unconfirmed as **UNVERIFIED** — never guess commands, flags,
   or version numbers.

## Step 3 — Update INDEX.md

Add a row to the matching table (Drafts or Decisions) in `INDEX.md`.
This is not optional. A document that isn't in the index doesn't exist.

## Finalizing a draft

When the user says a doc is done:

1. Confirm the doc passes review (offer to run doc-reviewer).
2. Change front matter `status: Draft` → `status: Final`, update `updated`.
3. Move the file from `drafts/` to `final/`.
4. Move its INDEX.md row from Drafts to Final.

## Superseding / archiving

When a doc is outdated or replaced:

1. NEVER delete. Move the file to `archive/`.
2. Set front matter `status: Archived` and add `superseded_by: <new-doc>` if
   a replacement exists.
3. Move its INDEX.md row to Archived, filling the "Superseded by" column.

## Filing external material

When the user saves an external doc, article, or spec, apply the test:
"If this is updated or deleted, must a doc be re-verified?"

- **Yes** → `references/sources/`, named thing-version-topic
  (e.g. `nginx-1.27-config-reference.pdf`). These are evidence — docs cite them.
- **No** → `references/reading/`, named format-topic
  (e.g. `blog-zfs-vs-btrfs.md`). Background only.

References feed docs, never replace them: if a saved thread contains a fix,
also create a troubleshooting doc — the doc is canonical, the reference is not.

### Academic papers

Papers can go in EITHER folder; the dependency test decides, never the paper
type. A research paper a doc's claims rest on → `sources/`; a survey read for
orientation → `reading/`.

1. Name it `paper-<type>-<year>-<firstauthor>-<topic>.pdf`
   (type: survey, research, review, preprint, thesis, whitepaper).
2. Add a row to the References table in `INDEX.md`: file, type, folder, and
   which docs use it (leave "Used by" empty if none yet).
3. If a doc cites the paper, list the paper in that doc's Related section.

## Hard rules (from Project Instructions.md)

- Never overwrite a file in `final/` without explicit confirmation.
- One topic per document.
- Version-dependent claims must state the version.
