# Search rules after this change

The same parts after this change, with the new hard rule and section 5.12, links to other sections removed. The example that opens section 5.12 is left out, because it names the answers of two test cases.

## A hard rule

17. **Search past every list.** Every list handed over is a starting point and never complete, and a route that fails answers nothing. In full (5.12, Searching):
    - Lists handed over: a tracker, a seed list of repositories, the source pack, a checklist, a brief, and the examples in these files.
    - Searched every time as well:
        - Tim's GitHub account ([mithro](https://github.com/mithro)), every public repository and fork;
        - [mith.ro](https://mith.ro);
        - Tim's Drive, through 5.1, Link allow-list;
        - the whole hit-list repository, every item's document and resources file.
    - A route that fails (refused, blocked, timed out) is replaced by another route to the same fact, one the session permits. A refusal by policy is recorded, never retried or circumvented. Where every route fails, write `Unknown (settled by: …; not reached: …)` with the routes tried, never `None found` and never a negative.
    - Every absence names its searches where it stands, in a summary sentence as in a table row: searches that ran and returned, with their dates. A list's contents are not a search.
    - A found candidate set aside unread ("a mirror", "inactive") is an absence too: it needs a route that reached it, or `Unknown` with the routes tried.

## Claim statuses for an absence

| Status | Meaning | Survives landing |
| --- | --- | --- |
| `None found (searched: <where>, <date>)` | A required element with nothing to report, after named searches¹ | yes |
| `Unknown (settled by: <what>)` | A fact nobody has, with what settles it² | yes |

1. Searches that ran and returned, past every list handed over (5.12, Searching).
2. A measurement, an experiment or a question. A fact no route reached adds `; not reached: <routes>, <date>` (5.12, Searching).

A negative claim ("no open process design kit (PDK) has a complete per-rule suite") is a claim like any other: it carries `(as of YYYY-MM)` and names where the writer looked. The search behind it ran past every list handed over, through a route that answered (5.12, Searching).

A broken link is removed or replaced, never left; "unreachable from this sandbox" is a status to record, never a pass. Invented or unverifiable references are a blocker in review.

## Searching

**A finding is only as strong as the search behind it.** So a search is reported as it ran, and no list handed over limits it.

**Every list is a starting point.** None is complete, so the search goes past each one.

- The lists: trackers, seed lists of repositories, the source pack, checklists, briefs and the examples in these files.
- Past them: the forks and dependents of every repository named, newer work by every person named or in a named repository's history, the works that cite each paper, and the searches below.

**The searches every source pack runs.** They are a floor, never a ceiling. Each is a row of the pack's Searches table (PROCESS.md 8, Source pack format).

| Search | Where | What is searched | What is read |
| --- | --- | --- | --- |
| Tim's GitHub account | [mithro](https://github.com/mithro) | Every public repository and fork, newest push first | Each one touching the item¹ |
| Tim's site | [mith.ro](https://mith.ro) | The index of his documents, and its pull requests | Each entry touching the item |
| Tim's Drive | The Drive connector | The item's key terms | Each hit, through 5.1, Link allow-list² |
| The hit-list repository | Every `projects/*.md` and `resources/*.md` | The item's key terms | The related items' resources files, in full |
| The trackers | PROCESS.md 9, Literature: the paper trackers | The item's tabs | Every row, before any search tool³ |

1. Each repository the item names is also checked for a fork there.
2. Drive titles stay in the private pack.
3. Then searched past, like every list.

**A blocked route is a gap, not an answer.** Reach the same fact another way, or record it as not reached. A route has failed when it gave no answer: refused, rate-limited, timed out or blocked by the sandbox. The other ways:

- the web page for a programming interface, or the other way round;
- a connector, where the session allows it;
- `git ls-remote` or a clone, which also finds a fork by its upstream's name;
- the raw-file host, for a file in a repository;
- the project's account on the code host, for a site that cannot be reached;
- a mirror or an archive.

Where every route fails, the claim is `Unknown (settled by: <the search>; not reached: <routes tried>, <date>)`: never `None found`, and never a negative sentence.

**Another route, never a way past a block.** Each route used is one the session permits. A refusal by policy, such as a proxy's 403 or a permission gate, is recorded with the host and the reason. It is never retried, and nothing is done to get past it.

**A search is reported as it ran.** A list's contents, or a search that failed, is not a search. `None found (searched: …)` names searches that ran and returned, with their dates. A search stopped early says where it stopped ("the first 100 of 1,240 results").

**Every absence names its search where it stands.** A summary sentence carries its search as a table row does. So "nothing newer was found" carries `(searched: …)` on the same line, or is left out. A found candidate set aside unread ("a mirror", "inactive") is an absence about what it holds. It needs a route that reached it, or `Unknown (settled by: …; not reached: …)`.

**Why no shortcut.** A missed source costs more than any search. Effort is not rationed (the working assumption of section 2), and a false "none exists" misleads every reader and every agent that plans from the document.

## The source pack: inputs

**Source pack.** The writer assembles `sources.md` before writing a word. Its format is in section 8, Source pack format. Every input is a starting point and none is complete (GUIDELINES.md hard rule 17, Search past every list). Inputs, in this order:

1. The current `projects/<id>.md`, `resources/<id>.md`, `resources/misc.md`, and this item's rows in `items.json` (`related`, in both directions).
2. The rest of the hit-list repository: every `projects/*.md` and `resources/*.md` searched for the item's key terms, and the related items' resources files read in full; another item's file often holds what this one lacks.
3. The project's working notes for the item (the staging notes), with their sensitivity flags, which decide the sensitivity of every document (GUIDELINES.md 5.2, Material outside the allow-list, and the private workflow notes).
4. Tim's documents and talks for the item, read through the Drive connector. For each: the sharing check with its date, what was read (in full or summary), and its sensitivity. A document that cannot be read is not in the pack.
    - Found three ways: named in the staging notes, listed in the index on [mith.ro](https://mith.ro), and returned by a search of his Drive for the item's key terms.
    - Tim's documents are sources with their own failure modes (a design written before the experiment, a number never re-measured, a conclusion overtaken by a later tool) and get the same cross-check as any other; nothing is taken as true because he wrote it.
5. Tim's GitHub account, [mithro](https://github.com/mithro): every public repository and fork, newest push first, each one touching the item read; each repository the item names, checked for a fork there. A private repository is neither opened nor named.
6. The project's paper trackers (section 9, Literature: the paper trackers), filtered to the item's tabs, before any search tool is used.
7. Search tools, past every list above (GUIDELINES.md 5.12, Searching). The private workflow notes list the hosts the writing sandbox can and cannot reach; a host it cannot reach is reached by another route, or recorded as not reached, never as an absence.
    - Papers: the paper-search skill and [OpenAlex](https://openalex.org/), the open index of scholarly works, with the paper-discovery tools listed in the private workflow notes.
    - Repositories: a shallow clone (`git clone --depth 1`), which pins the commit and date that every count and quote from the repository cites; the hosting site's pages and interface are not reachable from every sandbox, and a count made on a fetched page has no commit.
    - Contribution rules, licences and status: the cloned files first; web fetch of the hosting site's page only for what the clone does not carry (the archived marking, a named successor), which is one source, with the clone's last commit date as the second (GUIDELINES.md 5.5, Status of tools and projects).
    - A deep-research run only when the field is wide and the trackers are thin.
8. The neighbours' Goal sections (every id in `related`), so the dependency claims can be checked.
9. `FACTS.md` and `DECISIONS.md`.

**Every search is a row.** The pack's Searches table holds every search, failed routes included. Each row has its route, query, date and result. The searches of GUIDELINES.md 5.12, Searching come first. A failed route's row says how it failed and which route replaced it. Step 5, Revise and audit checks every absence against the table.

## Research

**Research.** Every *research* finding becomes a task. The task: the question, where the search starts (never where it ends), and the evidence that settles it. The writer runs them (paper search, fetching repositories and documentation, re-reading Tim's documents, a deep-research run where justified). Results go into the pack with sources; a result that cannot be found becomes `None found (searched: …)` or `Unknown (settled by: …)` in the draft, with the search recorded; a route that failed is never `None found` (GUIDELINES.md 5.12, Searching).

## The claim audit, its first check

- [ ] Every attribution to Tim and every absence claim ("nobody has", "no open tool does") checked against the live source.
    - An absence is checked against the pack's Searches table as well: its searches ran and returned, went past every list handed over, and include those of GUIDELINES.md 5.12, Searching.
    - An absence is unsupported when it rests on a list, on the item's own files alone or on a route that failed. So is an absence in a summary sentence with no search named, and a found candidate set aside unread.
