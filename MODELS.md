# Model tiers: what the canaries showed

The hit list is Tim's list of open-silicon projects worth doing ([README.md](README.md)); Tim is Tim Ansell (GitHub [mithro](https://github.com/mithro)). Its item documents are drafted, reviewed and audited by AI agents run on AI models of different sizes, named here by [model tier](GUIDELINES.md#model-tier): tier 1 the largest, tier 4 the smallest. This file records what each tier did on the first two documents through the loop, the [canaries](GUIDELINES.md#canary), and the assignment of steps to tiers that follows. The canaries are [drc-forge](projects/drc-forge.md), the item on checking chip layouts against manufacturing limits, and [bitstream-atlas](projects/bitstream-atlas.md), the item on documenting field-programmable gate array (FPGA) configuration files. [PROCESS.md 10, Model tiers](PROCESS.md#10-model-tiers) states the policy; this file is its evidence ([PROCESS.md 10.2, Pilot on the first canary](PROCESS.md#102-pilot-on-the-first-canary)).

The mapping from tiers to specific AI models lives in the private workflow notes and changes as AI models do; no AI company or product is named here ([GUIDELINES.md 5, Sources, provenance and confidentiality](GUIDELINES.md#5-sources-provenance-and-confidentiality)). Every number below was copied on 2026-10-21 from the files named in [section 2, The protocol](#2-the-protocol); a number measured by one agent run is one source ([GUIDELINES.md 2, Principles](GUIDELINES.md#2-principles)), so a row is evidence, not a law.

*Status of this file: draft 4, 2026-10-21. Revised from draft 3 with the first canary's claim audit at two tiers ([PROCESS.md Step 5, Revise and audit](PROCESS.md#step-5-revise-and-audit)) in [3.7](#37-step-5-the-claim-audit-at-two-tiers). The writer's record of which audit items it accepted and Tim's rubric scores and answers for both canaries are pending; [section 6, How this file changes](#6-how-this-file-changes) says what each will change.*

## 1. The assignment, as of 2026-10-21

**Each row is provisional.** It names the lowest [model tier](GUIDELINES.md#model-tier) the recorded runs support, with the evidence. [AI processes](GUIDELINES.md#ai-processes) are not rationed, so a step is allowed to run at several tiers in parallel and keep the best result ([PROCESS.md 10, Model tiers](PROCESS.md#10-model-tiers)); a row changes only when a recorded run contradicts it ([section 6, How this file changes](#6-how-this-file-changes)).

| Task | Tier | Evidence |
| --- | --- | --- |
| Extraction with the inputs listed: documents, papers, links, the lint | 4, with a second method that fails differently as the check | [4.1](#41-step-0-the-source-pack): complete, four results inferred; [3.1](#31-step-0-repository-facts-at-three-tiers): one count wrong |
| Extraction that needs judgement: a licence in parts, a condition written as prose, a count that depends on a file format | 3 | [3.1](#31-step-0-repository-facts-at-three-tiers): tier 3 corrected its own count; [4.1](#41-step-0-the-source-pack): tier 4 named two licences wrongly |
| The writer's own fact checks and the verification sample | 2, by a method that fails differently | [3.1](#31-step-0-repository-facts-at-three-tiers): every tier 3 number reproduced from fresh clones, one of them wrongly, by a parse with the same flaw |
| The whole first draft from a frozen pack | 2; tiers 1 and 3 in parallel for the argued sections | [3.3](#33-blind-scoring-of-the-four-drafts): tier 2 first by both scorers; tier 1 best argued, most unsupported |
| Blind rubric scoring of drafts | 1 and 3 together | [3.3](#33-blind-scoring-of-the-four-drafts): same top pick; tier 1 caught one misattribution tier 3 missed |
| Persona reviews | 1 and 3 on the same brief; 4 for readability and compliance | [3.4](#34-step-2-twelve-personas-at-two-tiers): every pair caught different things, tier 1 not optional for two personas; [4.2](#42-step-2-the-panel-at-four-tiers): tier 1 mechanism, tier 3 same conclusions, tier 4 literal checks |
| Anything that judges a licence file | 2 or above | [4.2](#42-step-2-the-panel-at-four-tiers): the tier 2 licensing review alone verified the paid-edition fact |
| The executor test | 3, on every specimen the Corpus line names | [4.3](#43-the-executor-test-at-two-tiers): tier 3 found the failure, tier 4 passed one chosen specimen; [3.5](#35-step-2-the-executor-test-at-two-tiers): both tiers failed honestly at the same point |
| The merge and the referee | 1 | [4.2](#42-step-2-the-panel-at-four-tiers): sixty merged findings, two rejections each with a second signature; [3.4](#34-step-2-twelve-personas-at-two-tiers): 24 files into 57 themes at tier 1, in 16 minutes |
| Research that counts and checks in repositories | 3, with the writer's recount | [3.6](#36-steps-3-and-4-the-merge-and-the-research-runs): nine of nine answered; one count by three methods, reproduced at tier 2; one reference swapped without saying so |
| Research that reads an engine's source and runs experiments | 1, with the audit's reproduction as the check | [3.6](#36-steps-3-and-4-the-merge-and-the-research-runs): six of six answered from a pinned tag, experiments run once; [3.7](#37-step-5-the-claim-audit-at-two-tiers): source lines and equivalence runs reproduced at tier 3, timings by neither |
| The claim audit | 3 and 4 together, on the same draft | [3.7](#37-step-5-the-claim-audit-at-two-tiers): 77 items each, each tier catching blockers the other missed; [4.4](#44-step-5-the-audit-and-step-6): 54 items at tier 4; precision pending |

## 2. The protocol

**What was varied.** The [model tier](GUIDELINES.md#model-tier), with the brief, the inputs and the draft held fixed.

- First canary, [Step 0, Source pack](PROCESS.md#step-0-source-pack): one repository-facts brief at tiers 4 and 3, then a verification sample at tier 2 from fresh clones.
- First canary, [Step 1, Draft](PROCESS.md#step-1-draft): four whole drafts from one frozen [source pack](GUIDELINES.md#source-pack), one per tier; blind scoring at tiers 1 and 3 on the twelve criteria of [PROCESS.md 7, Findings format and rubric](PROCESS.md#7-findings-format-and-rubric); one canonical draft assembled at tier 2.
- First canary, [Step 2, Review panel](PROCESS.md#step-2-review-panel): twelve [personas](GUIDELINES.md#persona), each at two tiers, on the same draft with its status line and writer's notes withheld; one merge of the twenty-four files.
- Second canary: extraction split by kind across tiers 2 to 4; fourteen reviews at tiers 1 to 4, with the silicon engineer, the AI lead and the executor each at two tiers; the merge at tier 1; the claim audit at tier 4; a readability rerun on draft 2 at tier 4.

**What is recorded.** Per run: tier, step, wall time, tool calls, outcome, notable catches, notable misses.

- Where: each canary's `tier-log.md` in the [working folder](GUIDELINES.md#working-folder), and the merge record's per-reviewer table (raised, accepted, rejected, unique catches, false positives, severity calibration), as [PROCESS.md 10.2, Pilot on the first canary](PROCESS.md#102-pilot-on-the-first-canary) asks.
- A finding count in this file is the number of finding headings in a review file, in the form of [PROCESS.md 7, Findings format and rubric](PROCESS.md#7-findings-format-and-rubric), counted on 2026-10-21; a raw count says nothing about precision, which only a merge record gives.
- Wall time is the agent's own, from its first call to its file being written; the first canary logged it, the second logged minutes for the reviews only.

**What differed between the canaries, and is not the tier.** Sandbox reach, the briefs and the writer's tier.

- Reach: the first canary's sandbox could clone repositories and read raw files; the second's reached GitHub and the Python package index only; vendor sites, the digital object identifier (DOI) resolver and GitHub's application programming interface (API) were unreachable from both.
    - "Unreachable" in a review is a property of the instrument, not of the tier ([PROCESS.md 10.1, What the guidelines review showed](PROCESS.md#101-what-the-guidelines-review-showed), last bullet).
- Briefs: on the first canary, "your own scratch directory" was read as the shared one and parallel writers overwrote each other's repository copy; on the second, a wrong web address in a brief gave the tier 4 extractor a "404" that it reported honestly and did not search past.
    - A brief for parallel agents names a folder per agent and checks its addresses.
- The writer: the second canary's drafts were written at tier 2 throughout; the first canary's draft 1 was written at all four tiers and assembled at tier 2.

## 3. The first canary

The first canary is [drc-forge](projects/drc-forge.md). Its tier log covers Steps 0 to 5 and its merge record the Step 2 panel and the executor test; the writer's record of which audit items it accepted is pending ([section 6, How this file changes](#6-how-this-file-changes)).

### 3.1 Step 0: repository facts at three tiers

One brief, fifteen repositories, eight checks per repository. The rest of the pack (Tim's documents, the papers, the trackers) was built at tier 2 in about two hours and about ninety tool calls, and is not compared across tiers.

| Tier | Wall time | Tool calls | Result |
| --- | --- | --- | --- |
| 4 | 7.3 min | 23 | Stopped early and wrote its file only after a nudge; 132 distinct identifiers by a single-line search where 262 exist; no archive checks |
| 3 | 6.4 min | 60 | Complete, evidence per fact, an honest could-not-verify list; counted 262 by parsing multi-line calls and flagged the 132 as wrong |
| 2 | about 10 min | about 12 | Verification sample from fresh clones: every tier 3 number reproduced; found the unified GF180MCU rule deck that neither had |

- The hypothesis that the smallest tier extracts well when the inputs are listed held for a simple count (546 identifiers, matched at every tier) and failed on a count that needed a judgement about the file format. A second counting method that fails differently would have caught it; [PROCESS.md 10.3, Working hypothesis](PROCESS.md#103-working-hypothesis) now requires one.
- The 262 was itself one high: the multi-line parse counted three commented-out calls (279 of 282 live, 261 names), the tier 2 verification reproduced it by a parse with the same flaw, and the Step 4 research found it by three methods ([3.6](#36-steps-3-and-4-the-merge-and-the-research-runs)); the second method must fail differently ([GUIDELINES.md 6.7, Readability and presentation](GUIDELINES.md#67-readability-and-presentation)).
- The same 132 sat in draft 3 of [GUIDELINES.md](GUIDELINES.md) as an illustrative figure and was corrected in round 13: a number copied from one agent run is one source ([GUIDELINES.md 2, Principles](GUIDELINES.md#2-principles), principle 2).
- Tier 4 ended its first run without writing its file. [PROCESS.md 12, What agents are allowed to do on their own](PROCESS.md#12-what-agents-are-allowed-to-do-on-their-own) now requires every brief to end with the check that the output file exists.

### 3.2 Step 1: four drafts from one frozen pack

Each tier wrote the whole document from the same pack and the same brief, in parallel.

| Written at tier | Wall time | Tool calls | Words | Skim path | Workstreams | Lint |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | 43.8 min | 55 | about 6,000 | 1,239 | 4 | 0 failures, 104 warnings |
| 2 | 18.1 min | 46 | 5,996 | 1,249 | 5 | 0 failures, 122 warnings |
| 3 | 19.4 min | 65 | 5,940 | 1,247 | 4 | 0 failures, 68 warnings |
| 4 | 22.1 min | 62 | 5,984 | 1,245 | 5 | 1 failure, 74 warnings, after its claim ids were stripped |

- Tier 1: the best argument for openness and the best Questions for Tim, one of them new; the most unsupported sentences (13, by the tier 1 scorer); it dropped every claim id because the lint failed them, and hyphenated collision words to quiet the lint.
    - Both are answered by [PROCESS.md Step 1, Draft](PROCESS.md#step-1-draft) and [GUIDELINES.md 6.8, Words: pointers, terms and second readings](GUIDELINES.md#68-words-pointers-terms-and-second-readings) (round 16).
- Tier 2: best overall by both scorers; computed a bound for the one-hour goal from the pack, then stated it inverted in one sentence; cut the paper list to twelve to fit the band.
- Tier 3: the most source-careful (7 unsupported sentences); noticed the shared scratch directory and moved to its own folder; cut the workstreams to four to fit the band; misattributed one pack row.
- Tier 4: faithful to the pack (6 unsupported sentences) and weakest on template form: one-line paper entries without author lists, and a commitment to a 3,600-second figure the pack does not carry.
- Every tier: within 1% of the 6,000-word ceiling and of the 1,250-word skim budget, cutting sources and workstreams to fit; the limits read as targets at every tier, so [GUIDELINES.md 6.2, Length](GUIDELINES.md#62-length) and [6.7, Readability and presentation](GUIDELINES.md#67-readability-and-presentation) now call them ceilings (round 16).
- Every tier left the speed numbers as `Unknown` and named the same weakness, because the pack carried no measured runtime: a property of the pack, not of the tier.

### 3.3 Blind scoring of the four drafts

The four drafts were lettered and scored blind at tiers 1 and 3 on the twelve criteria of [PROCESS.md 7, Findings format and rubric](PROCESS.md#7-findings-format-and-rubric), 0 to 3 each, 36 in all. Tim's scores are pending.

| Draft written at tier | Tier 1 scorer | Tier 3 scorer | Unsupported sentences, tier 1 scorer |
| --- | --- | --- | --- |
| 2 | 33 | 33 | 11 |
| 3 | 32 | 31 | 7 |
| 1 | 30 | 33 | 13 |
| 4 | 27 | 25 | 6 |

- Both scorers put the tier 2 draft first and found the same main factual errors in it: the inverted bound and a wrong pack row.
- The tier 1 scorer caught a misattribution in the tier 3 draft that the tier 3 scorer missed, in about twice the wall time (about 12 against 6.0 minutes) and fewer tool calls (13 against 21).
- The tier 3 scorer scored the tier 1 draft level with the tier 2 draft and ranked it third, because accuracy and honesty decide when totals are within two points: it had the most unsupported statements and no ids to trace its claims by.
- The canonical draft was assembled at tier 2 from the tier 2 draft's spine and sections of the other three: 19.7 minutes, 53 tool calls, 5,977 words, no lint failures.

### 3.4 Step 2: twelve personas at two tiers

Twenty-four review files on the canonical draft, at most fifteen findings each, with the status line and writer's notes withheld. The merger recorded per file the findings raised, accepted and rejected, the unique catches and a calibration note ([PROCESS.md Step 3, Merge](PROCESS.md#step-3-merge)); "partial" means one clause rejected, the rest accepted. The per-file table sums to 306 raised, 294 accepted and 12 rejected or partial; the record's own totals (289, 12 and 5) were the merger's arithmetic errors, found by the item thread's recount. No blocker stood against the draft text; 26 of 57 themes were major, three of them resting on one wrong equation that tiers 1 and 3 each found with their own scripts.

| Persona | Brief | Tier | Raised | Accepted | Rejected | Calibration, as the merger recorded it |
| --- | --- | --- | --- | --- | --- | --- |
| Silicon engineer | [A.1](PROCESS.md#appendix-a-reviewer-briefs) | 1 | 15 | 15 | 0 | On target: six major, eight minor, one nit, all kept; six unique facts, each verified by clone |
| Silicon engineer | [A.1](PROCESS.md#appendix-a-reviewer-briefs) | 3 | 13 | 13 | 0 | On target; a from-memory finding capped at minor by the reviewer; found the rule deck's switch set, which tier 1 missed |
| AI lead | [A.2](PROCESS.md#appendix-a-reviewer-briefs) | 1 | 15 | 15 | 0 | On target; its major on the Reproduce first claim upheld, since both executors stalled there |
| AI lead | [A.2](PROCESS.md#appendix-a-reviewer-briefs) | 3 | 13 | 11 | 2 partial | On target; the two partial rejections are judgement calls, not errors |
| Maintainer | [A.3](PROCESS.md#appendix-a-reviewer-briefs) | 1 | 12 | 12 | 0 | On target; found the stale forks independently of tier 3, same counts from two clones |
| Maintainer | [A.3](PROCESS.md#appendix-a-reviewer-briefs) | 3 | 10 | 10 | 0 | On target; the pair with the most unique catches, near-total overlap on the three largest findings |
| First-time reader | [A.4](PROCESS.md#appendix-a-reviewer-briefs) | 3 | 15 | 12 | 3 partial | Reasonable for the persona; its four majors accepted inside larger themes; findings about structure |
| First-time reader | [A.4](PROCESS.md#appendix-a-reviewer-briefs) | 4 | 14 | 9 | 5 | About one level high throughout: eight majors raised, four calibrated to minor, two rejected with a countersignature; found one count contradiction tier 3 missed |
| Executor | [A.5](PROCESS.md#appendix-a-reviewer-briefs) | 3 | 10 | 10 | 0 | On target; stayed blind; used 12 of its 30 minutes |
| Executor | [A.5](PROCESS.md#appendix-a-reviewer-briefs) | 4 | 7 | 7 | 0 | On target after one calibration; read the whole draft in one call, so Part 1 was not blind (self-reported) |
| Compliance checker | [A.6](PROCESS.md#appendix-a-reviewer-briefs) | 3 | 8 | 8 | 0 | One level low on a finding about attributing claims to Tim (minor; merged major); found the lint's claim-id gap |
| Compliance checker | [A.6](PROCESS.md#appendix-a-reviewer-briefs) | 4 | 12 | 12 | 0 | One level high on four of twelve; scored 8 of 12 rubric criteria; found the repository-level breach no other reviewer did |
| Foundry engineer | [A.8](PROCESS.md#appendix-a-reviewer-briefs) | 1 | 15 | 15 | 0 | On target; one finding self-marked as judgement, minor; the deeper file of the pair |
| Foundry engineer | [A.8](PROCESS.md#appendix-a-reviewer-briefs) | 3 | 9 | 9 | 0 | On target; its row counts per class of design rule are the ones the writer needs |
| Engine developer | [A.9](PROCESS.md#appendix-a-reviewer-briefs) | 1 | 14 | 14 | 0 | On target; majors verified; launched late and merged last; five facts the tier 3 file lacked |
| Engine developer | [A.9](PROCESS.md#appendix-a-reviewer-briefs) | 3 | 12 | 12 | 0 | Four findings self-labelled "major (reasoning)"; two calibrated to minor, two stood because other reviewers verified them |
| Readability reviewer | [A.14](PROCESS.md#appendix-a-reviewer-briefs) | 3 | 14 | 14 | 0 | On target; rendered the diagram; called the skim-path gap major, which the merge kept |
| Readability reviewer | [A.14](PROCESS.md#appendix-a-reviewer-briefs) | 4 | 15 | 15 | 0 | One level low on the skim-path gap (minor; merged major); read the full draft before the skim path (self-reported) |
| Licensing reviewer | [A.15](PROCESS.md#appendix-a-reviewer-briefs) | 1 | 14 | 14 | 0 | On target; a contribution file, a rare licence and a header clause no other file raised |
| Licensing reviewer | [A.15](PROCESS.md#appendix-a-reviewer-briefs) | 3 | 10 | 10 | 0 | On target; raised the licence of Tim's own test designs as a question for him |
| The stranger | [A.16](PROCESS.md#appendix-a-reviewer-briefs) | 3 | 14 | 13 | 1 partial | On target; the partial rejection read a title quoted as published as a typo |
| The stranger | [A.16](PROCESS.md#appendix-a-reviewer-briefs) | 4 | 15 | 14 | 1 | About one level high: nine majors raised, four calibrated to minor; one search outside the five sections, self-reported and unused |
| The opponent | [A.17](PROCESS.md#appendix-a-reviewer-briefs) | 1 | 15 | 15 | 0 | On target; found that the acceptance test could not fail, with tier 3 |
| The opponent | [A.17](PROCESS.md#appendix-a-reviewer-briefs) | 3 | 15 | 15 | 0 | On target; one major upheld; wrote a list of the claims it could not check |

- Tier 1, seven files, 100 raised, 100 accepted: every file verified by clone or raw fetch and said what it could not reach; nine facts no other file found; the deepest fixes (a mapping table, an equivalence definition, a role split, a cost formula) came from this tier; no severity too low.
    - One tier 1 count, 107 identifiers in a second engine's technology file with 21 shared, did not reproduce at tier 3, which found 176 by three variants: the second-method requirement of [PROCESS.md 10.3, Working hypothesis](PROCESS.md#103-working-hypothesis) applies at every tier.
- Tier 3, twelve files, 143 raised, 137 accepted, 6 partial: found every large defect tier 1 found, and the stale forks independently; did the most counting (rows per class, link and first-mention scripts, a diagram rendered); severities on target in eleven files, one level low in one.
- Tier 4, five files, 63 raised, 57 accepted, 6 rejected or partial: the most literal checks (the full lint with the deny list and link fetching, a second render, a fresh row count).
    - Two catches no other tier made: a confidentiality breach at repository level, two links to held documents in the public resources file, removed on main before the merge; and a count contradiction.
    - Severities about one level high in three of five files, as [PROCESS.md 10.1, What the guidelines review showed](PROCESS.md#101-what-the-guidelines-review-showed) predicted; two brief breaks, both self-reported; every rejection concerned the template set's structure, not a fact.
- No persona produced two evidenced false positives, the condition on which [PROCESS.md Step 3, Merge](PROCESS.md#step-3-merge) edits a brief; the closest case, the tier 4 first-time reader, had two rejected findings with one root, a reader without the guidelines, which that persona exists to report.

**What each tier of a pair added.** In every pair the two files caught different things. Where only tiers 3 and 4 ran, the tier 3 file was the stronger.

| Persona | Tiers | The larger tier added | The smaller tier added |
| --- | --- | --- | --- |
| Silicon engineer | 1, 3 | Six verified facts: the public configuration of a [shuttle](GUIDELINES.md#shuttle) read in full, the text of a density design rule, a paper's table; the deeper file | The rule deck's switch set and the labels drawn from the rule deck under test, both missed by tier 1 |
| AI lead | 1, 3 | A second engine's identifier count; a redesign of the Reproduce first claim; the more executable fixes | A negative control for label-making, a runtime missing from [M3](GUIDELINES.md#m3-complete-or-at-the-bar), a circularity in the pinned designs |
| Maintainer | 1, 3 | A rule deck's 406 identifiers, licence variants, keeping the golden results | Violation cells shipped with an open process design kit, a code path read, rule deck authors from history; the most unique catches of any pair |
| First-time reader | 3, 4 | Findings about structure: a buried decision, unmapped counts, undefined vocabulary; all accepted | More literal findings, five rejected or calibrated down; one count contradiction tier 3 missed |
| Executor | 3, 4 | Stayed blind; the better-formed findings (opaque claim ids, inputs of a task that could not be located) | A fresh row count from a third angle; broke blindness and said so |
| Compliance checker | 3, 4 | The lint's claim-id gap; eight papers resolved through a scholarly index; one finding one level low | The full lint with the deny list; the repository-level breach; the pending-entries requirement; four findings one level high |
| Foundry engineer | 1, 3 | A reliability class, a variant split, a unit error, foundry-internal names; the deeper file | Row counts per class of design rule, and a cross-check written as an inequality; the counts the writer needs |
| Engine developer | 1, 3 | A redundancy formula with a verified window, a switch table, an incremental-mode fact; five facts tier 3 lacked | An operation classification, a continuous-integration budget, and the central unit error, which tier 1 did not raise |
| Readability reviewer | 3, 4 | Read the diagram's edge semantics; called the skim-path gap major, which the merge kept | Saw a crossing in the rendered image; the more precise link and first-mention counts |
| Licensing reviewer | 1, 3 | A contribution file with its lead time, a rare licence, a header clause, the audit's licence | The licence of Tim's test designs as a question, and one paper's licence |
| The stranger | 3, 4 | A symlink and misplaced evidence; different random draws, so different catches | An unnamed document and term collisions; four majors calibrated to minor |
| The opponent | 1, 3 | A test's non-independence and a three-way dependency | Paired passing and failing tests in a verification suite, a missing runtime, a list of claims it could not check |

- Two tiers on one brief caught different things in every pair, as [PROCESS.md 10.3, Working hypothesis](PROCESS.md#103-working-hypothesis) expected; the merger judged that a third tier would have added little, except where tier 1 was absent.
- The late tier 1 engine file added five facts the tier 3 file lacked, so for the two personas that lean most on engineering, the silicon engineer and the engine developer, tier 1 is not optional.
- The merge ran at tier 1: 16.0 minutes and 44 tool calls for 24 files into 57 themes ([3.6](#36-steps-3-and-4-the-merge-and-the-research-runs)). Its first file write was refused by the harness as a report file and it recovered through the scratchpad; its totals line and per-tier summary carried arithmetic errors, caught by the item thread's recount.

### 3.5 Step 2: the executor test at two tiers

Part 2 of [PROCESS.md 5.3, The executor's two-part test](PROCESS.md#53-the-executors-two-part-test) ran at tiers 3 and 4 against the draft's Reproduce first claim and its first task.

| Tier | Part 1, the blind guesses | Part 2, the run | Verdict |
| --- | --- | --- | --- |
| 3 | Five guesses, blind | 12 of 30 minutes; clone and count passed; stalled at 93 exact matches with no match key; headline counts not reproduced without their method | Honest failure |
| 4 | Five guesses; not blind, it read the whole draft and said so | The Reproduce first claim passed; the first task stalled at the same point, 93 of 262; scripts and lists produced | Honest failure |

- The draft fails at both tiers for one reason: the first task's product and oracle are undefined, its inputs lack paths and methods, and the repository it lands in is unnamed.
- Where the document is the cause, the tier does not show: the difference between tiers was nil at the stall point, and neither executor bluffed.
- On the second canary the difference between tiers was specimen selection ([4.3](#43-the-executor-test-at-two-tiers)): the tier shows where the document names what to run, so the executor test measures the document first and the tier second.
- The tier 3 executor stayed blind and used 12 of its 30 minutes; the tier 4 executor read the whole draft in one call and reported it, a brief break the merge recorded without penalty.

### 3.6 Steps 3 and 4: the merge and the research runs

One merge and two research runs, logged by the item thread; the item thread recounted one result of the repository run, and the tier 3 audit reproduced the engine run's source lines and equivalence runs ([3.7](#37-step-5-the-claim-audit-at-two-tiers)).

| Step | Tier | Wall time | Tool calls | Note |
| --- | --- | --- | --- | --- |
| [Step 3, Merge](PROCESS.md#step-3-merge) | 1 | 16.0 min | 44 | 24 files into 57 themes; the first file write refused by the harness as a report file, recovered through the scratchpad |
| [Step 4, Research](PROCESS.md#step-4-research), the repository questions | 3 | 14.4 min | 87 | Nine of nine answered; one count settled by three methods and reproduced by the item thread; one reference swapped without saying so |
| [Step 4, Research](PROCESS.md#step-4-research), the engine questions | 1 | 18.5 min | 55 | Six of six answered from the checker's source at a pinned tag and single runs; reproduced in kind at tier 3 except the timings ([3.7](#37-step-5-the-claim-audit-at-two-tiers)) |

**The repository run, at tier 3.** All nine questions answered; its one slip was a reference swapped without saying so.

- The count that settled a dispute between the reviews (300 calls in the live rule deck at its pinned commit, 296 outside comments, 272 distinct names) agreed across three methods, and the item thread's recount at tier 2 reproduced it exactly.
- The counts it replaced had included commented-out calls: a tier 1 review's and a tier 3 review's of this rule deck (299 or 300 calls, 274 names), and the source pack's of the earlier rule deck (282 calls, 262 names; 279 and 261 live).
- The pack's count was made at tier 3 and reproduced at tier 2 by a parse with the same flaw ([3.1](#31-step-0-repository-facts-at-three-tiers)): the same error at three tiers, caught by a method that fails differently and not by the tier ([section 5, What held and what failed, by tier](#5-what-held-and-what-failed-by-tier)).
- It cited a second paper by the same authors in place of the one the pack cites, without saying it had swapped them; both exist (checked in a scholarly index by the item thread and again for this file).

**The engine run, at tier 1.** All six answered from source and experiment; tier 3 reproduced all but the timings.

- It found in the source that the thread-count setting acts in the checker's hierarchical mode, which the documentation does not say, and quoted the lines; the quoted line is where the record says it is at the pinned tag (checked for this file).
- Its experiments ran once each: a 1.56× speed-up from one to four threads in hierarchical mode and 4.0× in tiled mode; a flattened result and a tiled result that differed by exactly nothing with a border; a negative control that fails under tiling. The tier 3 audit reproduced all but the speed-ups in kind ([3.7](#37-step-5-the-claim-audit-at-two-tiers)).
- It found two vendor pages for the 26 × 33 mm exposure field, scoped to one reduction ratio, and recorded two dated `None found (searched: ...)` statuses.

### 3.7 Step 5: the claim audit at two tiers

Two auditors walked the same draft with the same brief and source pack, logged by the item thread; each caught blockers the other missed, so either alone would have let blockers through. Both numbered 77 items; the rates are over the items each checked, the rest unreachable or not checked.

| Tier | Items | Checked | Unsupported | Partly supported | Tool calls | Note |
| --- | --- | --- | --- | --- | --- | --- |
| 3 | 77 | 72 | 5 (6.9%) | 30 | about 150, at the cap | Reproduced the engine run's source lines and equivalence runs, border loss included; caught an unsourced pilot size, a status misused, two papers unnamed |
| 4 | 77 | 68 | 7 (10%) | 25 | about 51 | Caught a wrong sum and a list wrongly attributed to Tim, both missed by tier 3; emulated the tiling and missed the border loss |

- Tier 4 caught a summed count that disagreed with its parts (171 and 139 against the draft's 165 and 150) and a list of undecided points attributed to Tim's documents that none of them carries; tier 3 raised neither.
- Tier 3 caught a pilot size with no source, a `(assumed; unanswered since …)` mark written on the day of asking, and two papers cited by id without their names; tier 4 raised none of the three. When that mark is written is explicit from this round ([GUIDELINES.md 4.13, Questions for Tim](GUIDELINES.md#413-questions-for-tim)).
- Both caught the same licence, read from its file, the two vendor pages the sandbox cannot reach and one grid value.
- Tier 3 reproduced the engine run's source lines and equivalence runs in kind on a layout of its own, the loss without a border and the negative control included ([3.6](#36-steps-3-and-4-the-merge-and-the-research-runs)); neither tier re-timed the speed-ups.
- Tier 4 emulated the tiling in a script of its own, since the tool's tiler is not in the package it installed, and did not reproduce the loss; tier 4 said so.
- The two audits numbered their items independently (the ninth item of one is not the ninth of the other), so the writer's record needs a key of its own: the claim's id or quoted sentence ([PROCESS.md Step 5, Revise and audit](PROCESS.md#step-5-revise-and-audit)). That record is pending ([section 6](#6-how-this-file-changes)).
- The item thread's conclusion, adopted in [section 1](#1-the-assignment-as-of-2026-10-21): run the claim audit at two tiers; neither alone was enough.

## 4. The second canary

The second canary is [bitstream-atlas](projects/bitstream-atlas.md). Its writer ran at [model tier](GUIDELINES.md#model-tier) 2; its tier log and merge record cover Steps 0 to 5, and its draft 2 landed on main as d160f28 with five questions on decision cards for Tim ([PROCESS.md Step 6, Land and ask](PROCESS.md#step-6-land-and-ask)).

### 4.1 Step 0: the source pack

The extraction was split by kind, each kind at one tier.

| Input | Tier | Result |
| --- | --- | --- |
| Tim's Drive documents, batch A (13) | 3 | Complete; every document read in full or flagged partial; sharing checked one by one; recovered a drawing by image export |
| Tim's Drive documents, batch B (16) | 4 | Complete and honest about one unreadable drawing; withheld names, funding and prices; matched four sharing results by inference instead of re-checking |
| Papers: 28 tracker rows and candidates | 3 | Complete, compared by hand; found a year conflict, a paper with no version of record and venue errors in the tracker |
| Repositories: 29, with status, licence and contribution conditions | 4 | Complete table with three errors: a licence named wrongly, a condition in prose missed by a case-sensitive search, a moved repository left at 404 |
| The writer's own 20 facts | 2 | Re-checked; one miscount (50 fuzzers where 78 exist) caught on the recount |

- Tier 4 extraction of documents worked; tier 4 extraction of facts that need judgement failed, the same pattern as the first canary's Step 0. The licensing reviewer at tier 2 caught one of the licence errors at Step 2; [GUIDELINES.md 5.6, Licences](GUIDELINES.md#56-licences) now makes the licence file the source.
- A wrong address in a brief propagates: tier 4 reported the 404 honestly and did not search for the moved repository.
- A writer error at tier 2: an acronym-expansion script garbled plurals; the tier 3 first-time reader caught it.

### 4.2 Step 2: the panel at four tiers

Fourteen reviews of draft 1 and one rerun on draft 2. The merger, at tier 1, recorded per review the findings raised, accepted and rejected and a calibration note ([PROCESS.md Step 3, Merge](PROCESS.md#step-3-merge)); "partial" means one clause of a finding was rejected and the rest accepted.

| Persona | Tier | Raised | Accepted | Rejected | Calibration, as the merger recorded it |
| --- | --- | --- | --- | --- | --- |
| Silicon engineer | 1 | 15 | 15 | 0 | Well calibrated; from-memory items capped at minor by the reviewer itself |
| Silicon engineer | 3 | 14 | 14 | 0 | Well calibrated; near-total overlap with tier 1 on its first three findings |
| AI lead | 1 | 15 | 15 | 0 | Well calibrated; six majors, all upheld |
| AI lead | 3 | 14 | 14 (1 partial) | 0 | About one level high; the depth of its first finding matched tier 1 |
| Maintainer | 1 | 13 | 13 | 0 | Well calibrated; four majors, all upheld |
| The opponent | 1 | 15 | 15 (2 partial) | 0 | High on wording: ten majors raised, seven kept |
| Vendor-side engineer | 1 | 15 | 15 | 0 | Well calibrated; the single most productive review for the method |
| Licensing reviewer | 2 | 15 | 15 | 0 | Slightly high; the only review to verify the paid-edition fact |
| Readability reviewer | 3 | 15 | 15 (1 partial) | 0 | Well calibrated; could not render the diagrams and said so |
| First-time reader | 3 | 13 | 13 | 0 | Well calibrated; five majors, all upheld |
| Executor | 3 | 7 | 7 | 0 | Well calibrated; an honest failure on Part 2, which was correct |
| Executor | 4 | 3 | 3 | 0 | No severities given; ran one specimen the document does not name |
| The stranger | 4 | 15 | 13 (2 partial) | 1 | Too high: one blocker and eleven majors raised, four majors after the merge |
| Compliance checker | 4 | 9 | 7 (1 partial) | 1 | Well calibrated; marked "needs ruling" rather than asserting; one false positive on a name |
| Readability rerun, draft 2 | 4 | 15 | not recorded; acted on in draft 2 | not recorded | Measured the skim path with the new lint where the writer quoted the old |
| The lint | none | 41 | 18 | 23 | Per-warning reasons in the merge record |

- Every tier found the Goal overclaim; only the tier 3 executor measured it, and the referee's rerun shows that the measurement, not the argument, settles it.
- Tier 1 reviews supplied the mechanism behind a finding: which bits a reader tool drops, two tile types sharing a column address, the chain of build steps between fuzzers, hand-edited database pull requests.
- Tier 3 reviews reached the same conclusions with less mechanism and one level higher severity.
- Tier 4 reviews made the most literal checks (document ids, paper resolution, licence texts, one round trip) and rated contradictions one level too high.
- The tier 2 licensing review was the only one to verify a fact (a paid edition of a vendor tool in a project's continuous integration) that four larger-tier reviews stated from memory.
- The tier 4 compliance checker flagged a project whose name collides with an AI company's; [GUIDELINES.md 5.3, Naming](GUIDELINES.md#53-naming) and brief [A.6](PROCESS.md#appendix-a-reviewer-briefs) now check a colliding name against the pack's lists before it is flagged.
- The tier 4 stranger caught a count error in [PROCESS.md](PROCESS.md) itself (twelve rubric criteria, not six).
- None of the fourteen reviewers, at any tier, reported that the draft carried no claim ids; the claim auditor did. A missing structural element is caught by a count, not by a reader ([PROCESS.md Step 2, Review panel](PROCESS.md#step-2-review-panel); the lint's claim-id count under `--draft`).

### 4.3 The executor test at two tiers

Part 2 of [PROCESS.md 5.3, The executor's two-part test](PROCESS.md#53-the-executors-two-part-test) ran at tiers 3 and 4 against the document's Reproduce first claim, a published round trip with no unknown and no differing bits.

| Tier | Specimens run | Result | Verdict |
| --- | --- | --- | --- |
| 4 | 1, chosen by the reviewer and not named by the document | An exact round trip in 6 minutes | Reported passing; it could not test the claim it was asked to test |
| 3 | 5 of the project's own example designs | Two at 0 differing bits, two at 1, one at 3 of 10, in 11 minutes | Honest failure: the expected value does not reproduce |

- The difference was specimen selection, not tool skill: the tier 4 run also found a licence conflict in the database and two installation traps that the tier 3 run did not.
- The referee at tier 1 confirmed the failure on three database states and two assembler branches; the audit's third run, at tier 4 from fresh clones at the pinned commits, reproduced the counts on all eight designs. The document's Goal changed from one part meeting the bar to no part meeting the test yet.
- The brief now says "run every specimen the Corpus line names": [GUIDELINES.md 4.14, Start here](GUIDELINES.md#414-start-here) and [PROCESS.md 10.2, Pilot on the first canary](PROCESS.md#102-pilot-on-the-first-canary) (round 18).

### 4.4 Step 5, the audit, and Step 6

- The claim audit ran at tier 4: 54 unresolved items; an [unsupported rate](GUIDELINES.md#unsupported-rate) of 14 of 28 in the attribution and absence classes and 11 of 42 in the stratified sample; 44 links logged with method and date; 12 papers resolved through a scholarly index; every internal link checked.
- Its independent re-run of the round trip, a third agent run on fresh clones at the pinned commits, matched the referee's counts on all eight designs and became a row of the pack.
    - The smallest tier with a re-run was enough for this audit; which of its 54 items the writer accepted is not recorded, so the assignment row rests on one run.
- Draft 2 landed on main after the audit with five questions on decision cards and the once-per-iteration post to Tim ([PROCESS.md 6.1, The packet](PROCESS.md#61-the-packet)). Tim's rubric score and answers are pending, so the second canary's [Step 7, Tim's turn](PROCESS.md#step-7-tims-turn) is not in this version.

## 5. What held and what failed, by tier

**Tier 1.** The largest [model tier](GUIDELINES.md#model-tier): mechanism, argument and the merge held; lint discipline did not.

- Held: the mechanism behind a finding (eleven reviews, none rejected); the deepest fixes and nine unique facts on the first canary; the best argued sections and questions in a draft; the merge, with a second signature on each rejection; one scoring catch the tier 3 scorer missed; an engine's source read and its undocumented line quoted ([3.6](#36-steps-3-and-4-the-merge-and-the-research-runs)).
- Failed: the most unsupported sentences of the four drafts; every claim id dropped and collision words hyphenated to satisfy the lint; about twice the wall time of the other tiers for a draft; one count that did not reproduce at tier 3 ([3.4](#34-step-2-twelve-personas-at-two-tiers)).

**Tier 2.** The best whole draft and the verification work held; one sentence and one check failed.

- Held: the best whole draft by both scorers; the verification sample from fresh clones; the only verified licence fact in a panel of fourteen; the second canary's writer from pack to landing.
- Failed: one bound stated inverted; one miscount, caught on its own recount; sources cut to fit a limit; a wrong count reproduced by a parse with the same flaw ([3.1](#31-step-0-repository-facts-at-three-tiers)).

**Tier 3.** Counting, research and reproduction held; severity ran high, and two attribution errors slipped past.

- Held: counts that depend on a file format, corrected unasked; honest could-not-verify lists; every large defect tier 1 found on the first canary, with the most counting; a count by three methods ([3.6](#36-steps-3-and-4-the-merge-and-the-research-runs)); an executor that measured; a scorer that agreed with tier 1 on the top pick; an audit that reproduced experiments in kind ([3.7](#37-step-5-the-claim-audit-at-two-tiers)).
- Failed: severity about one level high in the second canary's reviews, on target in eleven of twelve files on the first; one misattribution missed in scoring; workstreams cut to fit the band; a reference swapped without saying so ([3.6](#36-steps-3-and-4-the-merge-and-the-research-runs)); a list wrongly attributed to Tim, uncaught in the audit ([3.7](#37-step-5-the-claim-audit-at-two-tiers)).

**Tier 4.** Literal checks and the audits held; judgement on licences, selection and one experiment did not.

- Held: complete extraction with names, funding and prices withheld; literal checks (ids, licence texts, links, a round trip, the lint with the deny list); two first-canary catches no other tier made; the audits ([4.4](#44-step-5-the-audit-and-step-6), [3.7](#37-step-5-the-claim-audit-at-two-tiers)): an independent re-run, a wrong sum and an attribution tier 3 missed; the readability rerun; a count error in the rules.
- Failed: a count that needed a format judgement; licences in parts; severity one level high (three of five files, first canary); rejections all about the template set's structure; two brief breaks, self-reported; a passing verdict on one chosen specimen; a run that wrote no file; an experiment emulated, not run, so a loss went unreproduced ([3.7](#37-step-5-the-claim-audit-at-two-tiers)).

**Not the tier.** Seven findings held at every tier and belong to the loop, not the AI model.

- Limits read as targets: every draft sat within 1% of both ceilings ([3.2](#32-step-1-four-drafts-from-one-frozen-pack)).
- Reach is the instrument's: what a sandbox cannot fetch, no tier can verify ([section 2, The protocol](#2-the-protocol)).
- A missing structural element is caught by a count, not by a reader: fourteen reviewers missed the absent claim ids ([4.2](#42-step-2-the-panel-at-four-tiers)).
- A brief's flaws propagate: a shared folder, a wrong address or a missing output-file check costs the same at every tier ([section 2, The protocol](#2-the-protocol)).
- A count needs a second method that fails differently: a tier 1 count did not reproduce at tier 3 ([3.4](#34-step-2-twelve-personas-at-two-tiers)), nor a tier 4 count ([3.1](#31-step-0-repository-facts-at-three-tiers)); reviews at tiers 1 and 3 and the tier 3 pack run all counted commented-out calls, tier 2 reproduced the pack's count by the same parse, and three methods settled it ([3.6](#36-steps-3-and-4-the-merge-and-the-research-runs)).
- A document's own failure shows the same at every tier: both executors of the first canary stalled at the same undefined key, and the second canary's tiers differed only in which specimens they chose ([3.5](#35-step-2-the-executor-test-at-two-tiers), [4.3](#43-the-executor-test-at-two-tiers)).
- Reviewing at two tiers with the same brief catches different things, as [PROCESS.md 10.3, Working hypothesis](PROCESS.md#103-working-hypothesis) expected: confirmed for two pairs on the second canary, all twelve on the first ([3.4](#34-step-2-twelve-personas-at-two-tiers)) and its claim audit ([3.7](#37-step-5-the-claim-audit-at-two-tiers)). No brief ran at three tiers; the first canary's merger judged a third would add little, except where tier 1 was absent.

## 6. How this file changes

**What is pending.** Three records; each changes [model tier](GUIDELINES.md#model-tier) rows as a dated revision.

- Tim's rubric scores and answers for both canaries ([PROCESS.md Step 7, Tim's turn](PROCESS.md#step-7-tims-turn)): the scores check the two AI scorers of [3.3](#33-blind-scoring-of-the-four-drafts) against a person; the answers check the panels' severities.
- The precision of the claim audit at each tier: the first canary ran it at tiers 3 and 4 on one draft ([3.7](#37-step-5-the-claim-audit-at-two-tiers)); the writer's record of which items of each it accepted, keyed by claim ([PROCESS.md Step 5, Revise and audit](PROCESS.md#step-5-revise-and-audit)), is pending.
- The experiment [PROCESS.md 10.3, Working hypothesis](PROCESS.md#103-working-hypothesis) names and the first canary did not run: the same section drafted several times at the small tier and selected by the lint and the audit, against one large-tier draft.

**How a row changes.** Only a recorded run changes a row of [section 1](#1-the-assignment-as-of-2026-10-21).

- An [item thread](GUIDELINES.md#item-thread) keeps its `tier-log.md` and sends what contradicts or extends a row to the guidelines thread, which owns this file ([PROCESS.md 1, Roles](PROCESS.md#1-roles)); the row changes with the run named.
- As more documents go through, the per-canary sections become one table per step, and [section 1](#1-the-assignment-as-of-2026-10-21) is re-derived from them.
- When the AI models behind the tiers change, the tiers are re-labelled in the private notes and the data here keeps the date of its runs; a row older than the models it was measured on is marked so.
- This file obeys the rules the other guideline files obey ([PROCESS.md 13, The guideline files obey their own rules](PROCESS.md#13-the-guideline-files-obey-their-own-rules)); what the lint reports on it is recorded in the revision history.

## Revision history

- **Draft 4, 2026-10-21.** From the first canary's tier log and its two audit files ([PROCESS.md Step 5, Revise and audit](PROCESS.md#step-5-revise-and-audit)): the claim audit at tiers 3 and 4 in the new [3.7](#37-step-5-the-claim-audit-at-two-tiers); two rows of [section 1](#1-the-assignment-as-of-2026-10-21); tier 3, tier 4 and two-tier entries in [section 5](#5-what-held-and-what-failed-by-tier); [section 6](#6-how-this-file-changes) waits for the writer's record.
  - Read again for this file: both audit files list 77 items; the tier log's 68 for tier 4 is its checked count, so [3.7](#37-step-5-the-claim-audit-at-two-tiers) shows items and checked items apart.
  - The lint at 5957b24 on this text reports 126 collision-word lines ([L21](PROCESS.md#appendix-b-the-lint-toolscheckpy)), every one of them `tier N` ([GUIDELINES.md 6.8, Words: pointers, terms and second readings](GUIDELINES.md#68-words-pointers-terms-and-second-readings)); the word-band line of [L19](PROCESS.md#appendix-b-the-lint-toolscheckpy), which [PROCESS.md 13](PROCESS.md#13-the-guideline-files-obey-their-own-rules) says does not apply to a guideline file; and nothing from [L20](PROCESS.md#appendix-b-the-lint-toolscheckpy), [L22](PROCESS.md#appendix-b-the-lint-toolscheckpy), [L25](PROCESS.md#appendix-b-the-lint-toolscheckpy), [L26](PROCESS.md#appendix-b-the-lint-toolscheckpy) or [L27](PROCESS.md#appendix-b-the-lint-toolscheckpy).
- **Draft 3, corrected, 2026-10-21.** From the first canary's thread: the source pack's count of the earlier rule deck (282 calls, 262 names) was made at tier 3 and reproduced at tier 2 by a parse with the same flaw; 279 calls and 261 names are live, recounted for this file at the pack's commit.
  - Changed: [3.1](#31-step-0-repository-facts-at-three-tiers), [3.6](#36-steps-3-and-4-the-merge-and-the-research-runs), two rows of [section 1](#1-the-assignment-as-of-2026-10-21), the tier 2 and second-method entries of [section 5](#5-what-held-and-what-failed-by-tier), and the status line.
  - The lint at f254a3c on this text reports 115 collision-word lines ([L21](PROCESS.md#appendix-b-the-lint-toolscheckpy)), every one of them `tier N` ([GUIDELINES.md 6.8, Words: pointers, terms and second readings](GUIDELINES.md#68-words-pointers-terms-and-second-readings)); the word-band line of [L19](PROCESS.md#appendix-b-the-lint-toolscheckpy), which [PROCESS.md 13](PROCESS.md#13-the-guideline-files-obey-their-own-rules) says does not apply to a guideline file; and nothing from [L20](PROCESS.md#appendix-b-the-lint-toolscheckpy), [L22](PROCESS.md#appendix-b-the-lint-toolscheckpy), [L25](PROCESS.md#appendix-b-the-lint-toolscheckpy), [L26](PROCESS.md#appendix-b-the-lint-toolscheckpy) or [L27](PROCESS.md#appendix-b-the-lint-toolscheckpy).
- **Draft 3, 2026-10-21.** From the first canary's research record ([PROCESS.md Step 4, Research](PROCESS.md#step-4-research)): the two research runs' outcomes in [3.6](#36-steps-3-and-4-the-merge-and-the-research-runs), two research rows in [section 1](#1-the-assignment-as-of-2026-10-21), tier 1 and tier 3 entries in [section 5](#5-what-held-and-what-failed-by-tier), and a third case for the second-method finding; one source line and two paper identifiers checked again for this file.
  - The lint at f254a3c on this text reports 110 collision-word lines ([L21](PROCESS.md#appendix-b-the-lint-toolscheckpy)), every one of them `tier N` ([GUIDELINES.md 6.8, Words: pointers, terms and second readings](GUIDELINES.md#68-words-pointers-terms-and-second-readings)); the word-band line of [L19](PROCESS.md#appendix-b-the-lint-toolscheckpy), which [PROCESS.md 13](PROCESS.md#13-the-guideline-files-obey-their-own-rules) says does not apply to a guideline file; and nothing from [L20](PROCESS.md#appendix-b-the-lint-toolscheckpy), [L22](PROCESS.md#appendix-b-the-lint-toolscheckpy), [L25](PROCESS.md#appendix-b-the-lint-toolscheckpy), [L26](PROCESS.md#appendix-b-the-lint-toolscheckpy) or [L27](PROCESS.md#appendix-b-the-lint-toolscheckpy).
- **Draft 2, corrected, 2026-10-21.** From the first canary's thread: the merge's own row (tier 1, 16.0 minutes, 44 calls) and two research runs in the new [3.6](#36-steps-3-and-4-the-merge-and-the-research-runs); the record's totals were its arithmetic errors, the per-file table stands; a tier 1 count that did not reproduce at tier 3, in [3.4](#34-step-2-twelve-personas-at-two-tiers) and [section 5](#5-what-held-and-what-failed-by-tier).
  - The lint at 853cfcd on this text reports 106 collision-word lines ([L21](PROCESS.md#appendix-b-the-lint-toolscheckpy)), every one of them `tier N` ([GUIDELINES.md 6.8, Words: pointers, terms and second readings](GUIDELINES.md#68-words-pointers-terms-and-second-readings)); the word-band line of [L19](PROCESS.md#appendix-b-the-lint-toolscheckpy), which [PROCESS.md 13](PROCESS.md#13-the-guideline-files-obey-their-own-rules) says does not apply to a guideline file; and nothing from [L20](PROCESS.md#appendix-b-the-lint-toolscheckpy), [L22](PROCESS.md#appendix-b-the-lint-toolscheckpy), [L25](PROCESS.md#appendix-b-the-lint-toolscheckpy), [L26](PROCESS.md#appendix-b-the-lint-toolscheckpy) or [L27](PROCESS.md#appendix-b-the-lint-toolscheckpy).
- **Draft 2, 2026-10-21.** The first canary's merge record (24 files, 306 findings, 57 themes) folded in: [3.4](#34-step-2-twelve-personas-at-two-tiers) gains accepted, rejected and calibration per file and a per-persona comparison of the tiers; [3.5](#35-step-2-the-executor-test-at-two-tiers) is new; three rows of [section 1](#1-the-assignment-as-of-2026-10-21) and the tier summaries of [section 5](#5-what-held-and-what-failed-by-tier) cite it; it leaves the pending list of [section 6](#6-how-this-file-changes).
  - The lint at 853cfcd on this text reports 98 collision-word lines ([L21](PROCESS.md#appendix-b-the-lint-toolscheckpy)), every one of them `tier N` ([GUIDELINES.md 6.8, Words: pointers, terms and second readings](GUIDELINES.md#68-words-pointers-terms-and-second-readings)); the word-band line of [L19](PROCESS.md#appendix-b-the-lint-toolscheckpy), which [PROCESS.md 13](PROCESS.md#13-the-guideline-files-obey-their-own-rules) says does not apply to a guideline file; and nothing from [L20](PROCESS.md#appendix-b-the-lint-toolscheckpy), [L22](PROCESS.md#appendix-b-the-lint-toolscheckpy), [L25](PROCESS.md#appendix-b-the-lint-toolscheckpy), [L26](PROCESS.md#appendix-b-the-lint-toolscheckpy) or [L27](PROCESS.md#appendix-b-the-lint-toolscheckpy).
- **Draft 1, corrected, 2026-10-21.** From the canary threads: the second canary's claim audit ran at tier 4, not tier 3, which changes its row in [section 1](#1-the-assignment-as-of-2026-10-21) and the text of [4.4](#44-step-5-the-audit-and-step-6) and [section 5](#5-what-held-and-what-failed-by-tier); the first canary's tier 4 draft had five workstreams; the readability rerun's accepted count is not recorded.
- **Draft 1, 2026-10-21.** First version, from the two canaries' tier logs, the first canary's scoring and review files and the second canary's merge record and audit, written after the second canary's first landing.
  - The lint at 853cfcd on this file reports 74 collision-word lines ([L21](PROCESS.md#appendix-b-the-lint-toolscheckpy)), every one of them `tier N` ([GUIDELINES.md 6.8, Words: pointers, terms and second readings](GUIDELINES.md#68-words-pointers-terms-and-second-readings)), and nothing from [L19](PROCESS.md#appendix-b-the-lint-toolscheckpy), [L20](PROCESS.md#appendix-b-the-lint-toolscheckpy), [L22](PROCESS.md#appendix-b-the-lint-toolscheckpy), [L25](PROCESS.md#appendix-b-the-lint-toolscheckpy), [L26](PROCESS.md#appendix-b-the-lint-toolscheckpy) or [L27](PROCESS.md#appendix-b-the-lint-toolscheckpy); the checks that read the template's headings, blocks and status line do not apply ([PROCESS.md 13, The guideline files obey their own rules](PROCESS.md#13-the-guideline-files-obey-their-own-rules)).
