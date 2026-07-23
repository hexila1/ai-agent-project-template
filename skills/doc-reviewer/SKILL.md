---
name: doc-reviewer
description: >
  Use this skill whenever the user wants an existing document in this project
  checked, reviewed, audited, or validated. Triggers include: "review this
  doc", "check this document", "is this ready to finalize", "audit my docs",
  "quality check", or before any Draft is promoted to Final. Runs the
  project's quality checklist and reports pass/fail per item with specific
  fixes. Do NOT use for creating new documents — use doc-writer instead.
---

# Doc Reviewer

Quality checklist for documents in this project. Run every item, then report
results as a pass/fail table followed by concrete fixes. Do not silently fix
issues — report first, fix on confirmation.

This skill defines the ROLE and checklist only. Reusable task prompts live in
`prompts/`; thresholds (e.g. `limits.max_doc_length_words`) come from
`config/config.yaml` — read them from there, never assume values. All folder
and file locations referenced in the checklist resolve through the `paths:`
section of the same config.

## Checklist

### Front matter
- [ ] All fields present: `title`, `type`, `status`, `updated`, `tags`
- [ ] `type` matches one of: how-to, reference, troubleshooting, decision
- [ ] `updated` is a real date in YYYY-MM-DD
- [ ] Filename is `lowercase-with-hyphens.md` and reflects the title

### Structure
- [ ] Document covers exactly ONE topic (flag anything that should be split)
- [ ] Follows its template's section structure; no sections silently dropped
- [ ] H1 title, then a one-line/short-paragraph purpose statement
- [ ] Procedures use numbered steps, one action per step, imperative mood
- [ ] All code/commands in fenced blocks with a language tag

### Accuracy
- [ ] No unverified commands, flags, versions, or API details presented as
      fact — each is either verifiable or explicitly marked UNVERIFIED
- [ ] Version-dependent claims state the version
- [ ] How-to docs include a Verify section and a Rollback section (or an
      explicit "Not reversible")
- [ ] Troubleshooting causes marked UNVERIFIED unless confirmed

### Consistency
- [ ] All terminology matches `glossary.md`; new terms were added there
- [ ] Acronyms defined on first use
- [ ] No content duplicated from another doc — links to the canonical doc
      instead
- [ ] Cross-references point to docs that actually exist
- [ ] Doc length under `limits.max_doc_length_words` from `config/config.yaml`
      (flag for splitting if over)
- [ ] No hardcoded runtime values (model names, temperatures, endpoints) —
      those belong in `config/config.yaml` and should be referenced, not copied

### Bookkeeping
- [ ] Document has a row in `INDEX.md` in the correct table for its status
- [ ] If Archived: file is in `archive/`, `superseded_by` is set when a
      replacement exists, INDEX.md "Superseded by" column filled

### Style (from Project Instructions.md)
- [ ] Technical and precise; no filler, no marketing language, no emojis
- [ ] Active voice; no hedging unless uncertainty is real
- [ ] Understandable in isolation — assumes no memory of context

## Report format

| # | Check | Result | Fix needed |
|---|---|---|---|
| 1 | Front matter complete | PASS / FAIL | ... |

End with a verdict: **READY TO FINALIZE** or **NEEDS WORK** (with the blocking
items listed). Only recommend promotion to Final when every item passes.
