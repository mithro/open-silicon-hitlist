---
tags: [search-past-lists]
max_turns: 120
timeout_seconds: 3600
allowed_tools: [Read, Glob, Grep, Write, Edit, Bash, WebFetch, WebSearch]
---

Build one part of the source pack for the hit-list item open-pnr. Its document and resources file are projects/open-pnr.md and resources/open-pnr.md in the frozen copy of the hit-list repository.

Question for the item's Needs section: Which real FPGA boards could the item's agents use to check placed-and-routed designs in hardware without buying boards, and how would an agent reach them? Start from the item's own two files.

Write findings.md with: the answer in one paragraph; a table of each option you found (name, link, boards, how an agent reaches it, terms, how you found it); the searches you ran (route, query, date, result), failed ones included; and what you could not reach.
