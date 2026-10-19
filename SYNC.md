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
{ "README.md": { "doc_id": "...", "url": "https://claude.ai/..." } }
```

A new file gets its entry in the same commit that adds it.

## Shared copy for Claude threads

Claude threads in the project also keep a read-only mirror of this repository at `/mnt/project-files/hitlist/` so every thread can read the current list without cloning. Refresh it after each commit.
