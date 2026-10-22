# Search past every list: the tests

These tests check whether round 31 of the guidelines changes what a research agent does. Round 31 added [hard rule 17, Search past every list](../../GUIDELINES.md#0-the-hard-rules) and [5.12, Searching](../../GUIDELINES.md#512-searching), after the first [bitstream-atlas](../../projects/bitstream-atlas.md) source pack missed two things on 2026-10-22:

- [Tim's own fork of Project U-Ray](https://github.com/mithro/prjuray), 361 commits in September 2026, because the pack searched only a tracker's list and the code host's programming interface refused the sandbox;
- [fpgas.online](https://fpgas.online), a remote farm of real field-programmable gate array (FPGA) boards, because the pack read only the item's own resources file.

## Method

The method is the evaluation loop of the skill-creator skill: realistic prompts, runs with and without the change, one grader per assertion, then a revision of the wording where the runs with the change still fail.

- **Two conditions.** Every case runs with the round 31 text and with the same sections as they were on main at 4087288 ([`guidance/before.md`](guidance/before.md)).
- **Three versions of the change.** The wording was revised twice after grading; each version is kept, and the last is the text in GUIDELINES.md now.
- **One baseline.** `before.md` did not change, so iterations 2 and 3 are compared with iteration 1's runs without the change.
- **Everything else is the same.** Both runs get the common rules ([`guidance/common.md`](guidance/common.md)), the handling rules of [`run-brief.md`](run-brief.md), and a frozen copy of this repository at 4087288, the state the [bitstream-atlas](../../projects/bitstream-atlas.md) pack searched; later commits cite fpgas.online in more items.
- **No answers in the rules.** The guidance files leave out the 5.12 story of the three shortcuts, because the story names the fork and the board farm.
- **Tiers.** Each pair runs at the project's model tiers ([MODELS.md](../../MODELS.md)), named here by number only.
- **Grading.** A separate agent at tier 2 grades each assertion in a case's `graders/` folder, with the evidence quoted. It sees the task, the assertions, the run's output files and a condensed record of the run's tool calls; the guidance text and the configuration are removed.
- **Raw outputs stay private.** A run can open Tim's Drive, so its outputs, timings and benchmark files are kept in the working folder; this folder keeps the cases, the grades and the summaries.

| Iteration | Text of the change | Cases run with it |
| --- | --- | --- |
| 1 | [`after-iteration-1.md`](guidance/after-iteration-1.md) | All four, with and without |
| 2 | [`after-iteration-2.md`](guidance/after-iteration-2.md) | uray-fork-blocked-api, board-farm-in-other-items |
| 3 | [`after.md`](guidance/after.md) | audit-absence-claims, account-listing-unreachable |

What each revision added, from the failures of the runs before it:

- **Iteration 2.**
    - Every absence names its search where it stands, in a summary sentence as in a table row.
    - A found candidate set aside unread ("a mirror", "inactive") is an absence about what it holds.
    - Newer work by the people in a named repository's history is searched as well.
- **Iteration 3.** Another route is one the session permits; a refusal by policy is recorded, never retried or circumvented.

## Cases

- **[uray-fork-blocked-api](cases/uray-fork-blocked-api/).**
    - Seeds: a starting list of five repositories without Tim's fork, and a pointer to the programming interface the sandbox refuses.
    - A pass: the fork found by another route, or Tim's account recorded as not reached; never "no live fork".
- **[board-farm-in-other-items](cases/board-farm-in-other-items/).**
    - Seeds: a question on [open-pnr](../../projects/open-pnr.md) whose answer is only in other items' resources files.
    - A pass: fpgas.online found, through a search of the whole repository.
- **[account-listing-unreachable](cases/account-listing-unreachable/).**
    - Seeds: a request to list Tim's bitstream repositories when the account's listing cannot be fetched.
    - A pass: repositories found by other routes, the gap stated, and no claim that the list is complete.
- **[audit-absence-claims](cases/audit-absence-claims/).**
    - Seeds: a draft excerpt with five claims, and its pack excerpt.
    - A pass: the absences resting on a list, on the item's own files or on a failed route rejected; the one with a real search kept.

Each case folder holds:

- `prompt.md`: the run settings, then the task;
- `case.yaml`: the name and what a good result looks like;
- `graders/`: one assertion per file;
- `files/` and `place-files.sh`, where the case has input files.

## Results

Run and graded on 2026-10-22. Tier 1 did not run: its usage credits were used up.

Each cell gives the assertions passed, then one mark per assertion in the order of the case's `graders/` folder: ✓ passed, ✗ failed.

### Iteration 1

| Case | Tier | With the change | Without |
| --- | --- | --- | --- |
| uray-fork-blocked-api | 2 | 4/5 ✓✓✓✓✗ | 5/5 ✓✓✓✓✓ |
| uray-fork-blocked-api | 3 | 4/5 ✓✓✓✓✗ | 5/5 ✓✓✓✓✓ |
| uray-fork-blocked-api | 4 | 4/5 ✓✓✓✓✗ | 4/5 ✗✓✓✓✓ |
| board-farm-in-other-items | 2 | 5/5 ✓✓✓✓✓ | 4/5 ✓✓✗✓✓ |
| board-farm-in-other-items | 3 | 5/5 ✓✓✓✓✓ | 5/5 ✓✓✓✓✓ |
| board-farm-in-other-items | 4 | 5/5 ✓✓✓✓✓ | 4/5 ✓✓✗✓✓ |
| account-listing-unreachable | 2 | 4/4 ✓✓✓✓ | 4/4 ✓✓✓✓ |
| account-listing-unreachable | 3 | 4/4 ✓✓✓✓ | 4/4 ✓✓✓✓ |
| account-listing-unreachable | 4 | 4/4 ✓✓✓✓ | 4/4 ✓✓✓✓ |
| audit-absence-claims | 2 | 6/6 ✓✓✓✓✓✓ | 6/6 ✓✓✓✓✓✓ |
| audit-absence-claims | 3 | 6/6 ✓✓✓✓✓✓ | 6/6 ✓✓✓✓✓✓ |
| audit-absence-claims | 4 | 6/6 ✓✓✓✓✓✓ | 5/6 ✗✓✓✓✓✓ |

| Configuration | Assertions passed | Out of |
| --- | --- | --- |
| With the change | 57 | 60 |
| Without | 56 | 60 |

What the marks show:

- **Tim's fork.** Every run with the change found mithro/prjuray. The tier 4 run without it never did, and still scored 4 of 5 (uray assertion 1).
- **Tim's own sources.** Every run with the change searched Tim's GitHub account or mith.ro. The tier 2 and tier 4 runs without it did not (board-farm assertion 3); all three runs without it still found fpgas.online through the other items' resources files.
- **Absences in summary sentences.** Every uray run with the change failed assertion 5 on one or two slips: a summary sentence with no search named, a found candidate set aside unread ("a mirror"), or a refused query counted inside a `None found`. Every uray run without it passed. Iteration 2's wording answers these slips.
- **The audit at tier 4.** Without the change, the auditor marked claim 1 partly supported, not unsupported (audit assertion 1).
- **No difference.** In the listing case, and in the audit case at tiers 2 and 3, every run passed every assertion, with the change or without it.

### Repeat check: the audit case at tier 4

Three runs each way, with the iteration 3 text; the first run without the change is iteration 1's.

| Run | With the change | Without |
| --- | --- | --- |
| 1 | 4/6 ✗✗✓✓✓✓ | 5/6 ✗✓✓✓✓✓ |
| 2 | 6/6 ✓✓✓✓✓✓ | 4/6 ✗✗✓✓✓✓ |
| 3 | 6/6 ✓✓✓✓✓✓ | 3/6 ✗✗✗✓✓✓ |

| Assertion | Runs passing, with the change | Runs passing, without |
| --- | --- | --- |
| 1, claim 1 unsupported | 2 of 3 | 0 of 3 |
| 2, claim 1's fix asks for another route or `Unknown` | 2 of 3 | 1 of 3 |
| 3, claim 2 unsupported, wider search asked | 3 of 3 | 2 of 3 |
| 4 to 6 | 3 of 3 each | 3 of 3 each |

Every run without the change marked claim 1 partly supported. Two of them let the writer keep `None found` on a sentence narrowed to the two organisations searched, and one did the same for claim 2 and its one file.

### Iterations 2 and 3

Runs in progress; results follow.
