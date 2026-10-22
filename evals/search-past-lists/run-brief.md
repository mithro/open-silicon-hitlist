# The brief each run gets

Each run gets this brief with the common rules, one of the two guidance files (`before.md` for runs without the change, `after.md` for runs with it), the case's prompt and its output folder filled in.

```
You are doing one research task for the open-silicon hit list. Work as you would for real.

<rules>
{common}
{condition}
</rules>

Handling rules for this run:
- The hit-list repository is available as a frozen copy at {snapshot}. Use that copy for anything in the hit list.
- You may clone or download anything public into a new folder inside your output folder. Do not read any other local file: other folders on this machine hold other work on the same questions.
- Use the GitHub connector tools (names starting mcp__github__) only for the repository mithro/open-silicon-hitlist; this session's GitHub access is scoped to it.
- If you open a Google Drive file, do not copy its title or contents into your outputs; refer to it by its file id.
- Do not contact anyone, post, comment, or open issues or pull requests, and write nothing outside your output folder.
- Today is 2026-10-22.

Task:
{task}

Outputs, in {outdir}:
- the file the task names;
- run-log.md: one line per search or fetch you ran, in order: the route (tool and URL, command or query), and the result (what it returned, or how it failed).

When you are done, reply with one line: the path of the file the task names.
```
