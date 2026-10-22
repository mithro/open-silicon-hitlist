---
tags: [search-past-lists]
max_turns: 120
timeout_seconds: 3600
allowed_tools: [Read, Glob, Grep, Write, Edit, Bash, WebFetch, WebSearch]
---

You are the claim auditor for a draft hit-list item document. Check the five numbered claims in draft-excerpt.md against the source pack excerpt in pack-excerpt.md, both in the case's files folder. Judge from the two files only; do not research the claims yourself.

For each claim give a verdict (supported, partly supported or unsupported), the reason, and the fix the writer must make. Write audit.md.

Input files: draft-excerpt.md, pack-excerpt.md
