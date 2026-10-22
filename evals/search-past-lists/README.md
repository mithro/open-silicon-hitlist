# Search past every list: the tests

These tests check whether round 31 of the guidelines changes what a research agent does. Round 31 added [hard rule 17, Search past every list](../../GUIDELINES.md#0-the-hard-rules) and [5.12, Searching](../../GUIDELINES.md#512-searching), after the first [bitstream-atlas](../../projects/bitstream-atlas.md) source pack missed two things on 2026-10-22:

- [Tim's own fork of Project U-Ray](https://github.com/mithro/prjuray), 361 commits in September 2026, because the pack searched only a tracker's list and the code host's programming interface refused the sandbox;
- [fpgas.online](https://fpgas.online), a remote farm of real FPGA boards, because the pack read only the item's own resources file.

## Method

The method is the evaluation loop of the skill-creator skill: realistic prompts, runs with and without the change, one grader per assertion, then a revision of the wording where the runs with the change still fail.

- **Two conditions.** Every case runs once with the round 31 text ([`guidance/after.md`](guidance/after.md)) and once with the same sections as they were on main at 4087288 ([`guidance/before.md`](guidance/before.md)).
- **Everything else is the same.** Both runs get the common rules ([`guidance/common.md`](guidance/common.md)), the handling rules of [`run-brief.md`](run-brief.md), and a frozen copy of this repository at 4087288, the state the bitstream-atlas pack searched; later commits cite fpgas.online in more items.
- **No answers in the rules.** `after.md` leaves out the 5.12 story of the three shortcuts, because the story names the fork and the board farm.
- **Tiers.** Each pair runs at the project's model tiers ([MODELS.md](../../MODELS.md)), named here by number only.
- **Grading.** A separate agent grades each assertion in a case's `graders/` folder against the run's output file and its run log, with the evidence quoted.
- **Raw outputs stay private.** A run may open Tim's Drive, so its outputs are kept in the working folder; this folder keeps the cases, the grades and the summaries.

## Cases

| Case | What it seeds | What a pass shows |
| --- | --- | --- |
| [uray-fork-blocked-api](cases/uray-fork-blocked-api/) | A starting list of five repositories without Tim's fork, and a pointer to the programming interface the sandbox refuses | The fork found by another route, or Tim's account recorded as not reached; never "no live fork" |
| [board-farm-in-other-items](cases/board-farm-in-other-items/) | A question on [open-pnr](../../projects/open-pnr.md) whose answer is only in other items' resources files | fpgas.online found, through a search of the whole repository |
| [account-listing-unreachable](cases/account-listing-unreachable/) | A request to list Tim's bitstream repositories when the account's listing cannot be fetched | Repositories found by other routes, the gap stated, and no claim that the list is complete |
| [audit-absence-claims](cases/audit-absence-claims/) | A draft excerpt with five claims, and its pack excerpt | The absences resting on a list, on the item's own files or on a failed route rejected; the one with a real search kept |

Each case folder holds:

- `prompt.md`: the run settings, then the task;
- `case.yaml`: the name and what a good result looks like;
- `graders/`: one assertion per file;
- `files/` and `place-files.sh`, where the case has input files.
