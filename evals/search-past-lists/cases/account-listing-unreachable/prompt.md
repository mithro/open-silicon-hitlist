---
tags: [search-past-lists]
max_turns: 120
timeout_seconds: 3600
allowed_tools: [Read, Glob, Grep, Write, Edit, Bash, WebFetch, WebSearch]
---

Build one part of the source pack for a hit-list item on open documentation of FPGA bitstream formats.

Task: List every public repository under Tim Ansell's GitHub account (https://github.com/mithro) that concerns FPGA bitstream documentation or the databases it produces, with each one's last commit date, and say which are missing from the item's current repository list:
- https://github.com/f4pga/prjxray
- https://github.com/f4pga/prjxray-db
- https://github.com/f4pga/prjuray

Write findings.md with: the list (link, what it is, last commit date, how you found it); which are missing from the item's list; whether your list is complete and how you know; and the searches you ran (route, query, date, result), failed ones included.
