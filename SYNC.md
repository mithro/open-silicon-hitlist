# Keeping the repository and the living docs in sync

Every markdown file in this repository has a Claude Doc twin, listed in [docs.json](docs.json). The doc is where people read, edit and comment. The repository is the reviewable, versioned history.

## Rules

1. **The doc is the editing surface.** People make changes in the doc. Claude makes changes in the doc too, then exports it to the matching file and commits.
2. **One change lands in both places in the same session.** Never leave a doc edit uncommitted or a commit unmirrored.
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
2. Make the edit in the doc, then write the same content to the file. Doc-only furniture (the date and author line under the title, the "Mirrored in git as ..." footer) is not copied to git, and doc links in the README table point at the docs.
3. Update `last_synced` in docs.json, commit and push.

## Generated sections

The README list, the "How the items connect" grids and each project's "Where it sits", "Resources" and "Related items" sections are generated from `items.json` by `tools/build.py`. Change tags or relationships in `items.json`, rerun the script, and copy the regenerated sections into the matching docs (`python3 tools/build.py --doc-sections out.json` writes doc-ready versions with doc links). Do not hand-edit those sections in git.
