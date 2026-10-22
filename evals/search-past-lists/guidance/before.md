# Search rules before this change

As on main at 4087288 (2026-10-22), the parts of GUIDELINES.md and PROCESS.md that govern searching, links to other sections removed.

## Claim statuses for an absence

| Status | Meaning | Survives landing |
| --- | --- | --- |
| `None found (searched: <where>, <date>)` | A required element with nothing to report, after a named search. | yes |
| `Unknown (settled by: <what>)` | A fact nobody has, with the measurement, experiment or question that settles it. | yes |

A negative claim ("no open process design kit (PDK) has a complete per-rule suite") is a claim like any other: it carries `(as of YYYY-MM)` and names where the writer looked.

A broken link is removed or replaced, never left; "unreachable from this sandbox" is a status to record, never a pass. Invented or unverifiable references are a blocker in review.

## The source pack: inputs

**Source pack.** The writer assembles `sources.md` before writing a word. Its format is in section 8, Source pack format. Inputs, in this order:

1. The current `projects/<id>.md`, `resources/<id>.md`, `resources/misc.md`, and this item's rows in `items.json` (`related`, in both directions).
2. The project's working notes for the item (the staging notes), with their sensitivity flags, which decide the sensitivity of every document (GUIDELINES.md 5.2, Material outside the allow-list, and the private workflow notes).
3. Tim's documents and talks for the item, read through the Drive connector. For each: the sharing check with its date, what was read (in full or summary), and its sensitivity. A document that cannot be read is not in the pack.
    - Tim's documents are sources with their own failure modes (a design written before the experiment, a number never re-measured, a conclusion overtaken by a later tool) and get the same cross-check as any other; nothing is taken as true because he wrote it.
4. The project's paper trackers (section 9, Literature: the paper trackers), filtered to the item's tabs, before any search tool is used.
5. Search tools for the gaps only. The private workflow notes list the hosts the writing sandbox can and cannot reach.
    - Papers: the paper-search skill and [OpenAlex](https://openalex.org/), the open index of scholarly works, with the paper-discovery tools listed in the private workflow notes.
    - Repositories: a shallow clone (`git clone --depth 1`), which pins the commit and date that every count and quote from the repository cites; the hosting site's pages and interface are not reachable from every sandbox, and a count made on a fetched page has no commit.
    - Contribution rules, licences and status: the cloned files first; web fetch of the hosting site's page only for what the clone does not carry (the archived marking, a named successor), which is one source, with the clone's last commit date as the second (GUIDELINES.md 5.5, Status of tools and projects).
    - A deep-research run only when the field is wide and the trackers are thin.
6. The neighbours' Goal sections (every id in `related`), so the dependency claims can be checked.
7. `FACTS.md` and `DECISIONS.md`.

## Research

**Research.** Every *research* finding becomes a bounded task. The task: the question, where to look, what evidence settles it, a time box. The writer runs them (paper search, fetching repositories and documentation, re-reading Tim's documents, a deep-research run where justified). Results go into the pack with sources; a result that cannot be found becomes `None found (searched: …)` or `Unknown (settled by: …)` in the draft, with the search recorded.

## The claim audit, its first check

- [ ] Every attribution to Tim and every absence claim ("nobody has", "no open tool does") checked against the live source.
