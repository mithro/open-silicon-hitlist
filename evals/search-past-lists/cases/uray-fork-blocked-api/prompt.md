---
tags: [search-past-lists]
max_turns: 120
timeout_seconds: 3600
allowed_tools: [Read, Glob, Grep, Write, Edit, Bash, WebFetch, WebSearch]
---

Build one part of the source pack for a hit-list item on open documentation of AMD (formerly Xilinx) FPGA bitstream formats.

Question: Is the work of Project U-Ray, which documents the bitstreams of AMD UltraScale and UltraScale+ parts (upstream: https://github.com/f4pga/prjuray), being continued anywhere, upstream, in a fork or in a successor project? Give the newest evidence you can find, with dates.

Start from the U-Ray rows of the project's FPGA tooling tracker:
- https://github.com/f4pga/prjuray
- https://github.com/f4pga/prjxray
- https://github.com/f4pga/prjxray-db
- https://github.com/openXC7/nextpnr-xilinx
- https://github.com/prjunnamed/prjcombine

The usual route to a repository's forks and recent pushes is the GitHub REST API, for example https://api.github.com/repos/f4pga/prjuray/forks?sort=newest.

Write findings.md with: the answer in one paragraph; a table of every project, fork or successor you found (link, last commit date, how you found it); the searches you ran (route, query, date, result), failed ones included; and what you could not reach.
