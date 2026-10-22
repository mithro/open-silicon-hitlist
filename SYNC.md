# Keeping the repository and the living docs in sync

Every markdown file in this repository has a Claude Doc twin, listed in [docs.json](docs.json). The doc is where people read, edit and comment. The repository is the reviewable, versioned history.

## Rules

1. **The doc is the editing surface.** People make changes in the doc. Claude makes changes in the doc too, then exports it to the matching file and commits.
2. **Commit small and often.** Every coherent change is committed and pushed as it is made; nothing waits to be complete. A change lands in both places in the same session: the doc is re-synced from the file at the end of each piece of work, and at once when a commit changes a section people are reading.
3. **A change made in git goes back to the doc.** If someone edits a file directly (a PR, a local commit), the next Claude session that touches it applies that change to the doc before doing anything else.
4. **Conflicts:** if both sides changed since the last sync, keep both edits where they don't overlap; where they do, the doc wins and the git version is noted as a doc comment for a human to settle.
5. **Commit messages** name the file and say what changed, e.g. `projects/distributed-drc: add KLayout tiling benchmarks`.

## docs.json

Maps each repository path to its doc:

```json
{ "README.md": { "doc_id": "...", "body_node_id": "...", "url": "https://claude.ai/code/artifact/...", "last_synced": "YYYY-MM-DD" } }
```

A new file gets its entry in the same commit that adds it.

## Shared copy for Claude threads

Claude threads in the project also keep a read-only mirror of this repository at `/mnt/project-files/hitlist/` so every thread can read the current list without cloning. Refresh it after each commit.

## How a Claude session syncs

1. Read the doc (its `body_node_id` from docs.json) and compare it with the file.
2. Make the edit in the doc, then write the same content to the file. Doc-only furniture (the date and author line under the title, the "Mirrored in git as FILE." footer that ends every doc) is not copied to git, and doc links in the README table point at the docs.
3. Update `last_synced` in docs.json, commit and push.

## Generated sections

The README list, the "How the items connect" grids and each project's "Where it sits", "Resources" and "Related items" sections are generated from `items.json` by `tools/build.py`. Change tags or relationships in `items.json`, rerun the script, and copy the regenerated sections into the matching docs (`python3 tools/build.py --doc-sections out.json` writes doc-ready versions with doc links). Do not hand-edit those sections in git. The `title` in `items.json` is the short title used in tables and links; a file's H1 is `<id>: <its own title>`, and build.py keeps that title, so it may be longer than the short one.

## Item documents

The item documents under `projects/` follow [TEMPLATE.md](TEMPLATE.md) and [GUIDELINES.md](GUIDELINES.md), and are written through the iterations described in [PROCESS.md](PROCESS.md). They are drafted and reviewed with AI agents; human review is recorded in each document's status line ([GUIDELINES.md 4.1](GUIDELINES.md) gives its grammar, which `tools/check.py` reads).

**Status line.** The summary paragraph of every item document is followed by exactly one status line in this grammar:

```
*Status: <draft N | stable draft | reviewed>, YYYY-MM-DD. AI review panel: <...>. Human review: <none | Tim, YYYY-MM-DD>. Questions for Tim: <N>. This document was drafted and reviewed with AI agents; the AI review panel is not a human review, and the Human review entry is the only record of one.*
```

The question count matches the entries under "Questions for Tim". A document becomes `reviewed` only when Tim has approved it.

**Commit as you go.** Each coherent change to an item document is committed and pushed when it is made, with `tools/build.py` run and `docs.json` updated in the same commit. The living doc is re-synced from the file at the end of each iteration, and sooner when a commit changes a section people are reading.

**Working folder.** Drafts, source packs, reviews, findings and questions live in the project's shared folder under `hitlist-work/`, outside this repository. Only the finished document lands; nothing in `hitlist-work/` is copied into the repository.

**Lint.** Run `python3 tools/check.py projects/<id>.md` before landing; it checks the document against TEMPLATE.md and GUIDELINES.md and exits non-zero on any failure. `--deny FILE` and `--signoff FILE` take a private deny list and the list of unpublished-notes sentences Tim has signed off. Neither file is ever committed.

**Status line for other files.** GUIDELINES.md, PROCESS.md and other files that are not item documents carry one line directly under their opening paragraph:

```
*Status of this file: <draft N | stable | superseded>, YYYY-MM-DD. <what changed or what is being checked, in a sentence or two>.*
```

## Links and anchors

A link to a heading uses GitHub's anchor (`#4-section-requirements`: lower case, punctuation removed, spaces to hyphens). In the living docs, a link to another mirrored file goes to that file's doc URL from docs.json with the anchor kept; a same-file `#anchor` link becomes the file's own doc URL plus the anchor, because the docs engine refuses a single fill that carries many in-page links and splitting the fill breaks them; a link to any other repository path goes to the file on GitHub's main branch. `tools/check.py` (L24) fails a link whose anchor is not a heading of its target file.

## Diagrams

A diagram lives in the file as a ```` ```mermaid ```` block followed by an italic caption line (`*Figure N: ...*`). The Mermaid in the file is the source of truth. The living doc carries the same diagram and caption; a diagram edited in the doc is carried back to the file by hand.

A slide or other picture is a PNG under `images/<file-stem>/` (for example `images/readme/`, `images/drc-forge/`), named `<source>-<what>.png`. In the file it is a markdown image with alt text that says what the picture shows, followed by the same `*Figure N: ...*` caption line, ending with a link to its source. Only public or anyone-with-link material is embedded. In the living doc the same PNG is uploaded to the doc's artifact (`Artifact` publish with `asset: true`), recorded as a blob, and embedded with the same alt text and caption. Google Slides pages export at 1,600 pixels wide through the Slides thumbnail API, or at 960 pixels from `https://docs.google.com/presentation/d/<deck id>/export/png?pageid=<page id>` for an anyone-with-link deck.
