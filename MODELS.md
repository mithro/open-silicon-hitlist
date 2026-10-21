# Model tiers: what the canaries showed

The hit list is Tim's list of open-silicon projects worth doing ([README.md](README.md)); Tim is Tim Ansell (GitHub [mithro](https://github.com/mithro)). Its item documents are drafted, reviewed and audited by AI agents run on AI models of different sizes, named here by [model tier](GUIDELINES.md#model-tier): tier 1 the largest, tier 4 the smallest. This file records what each tier did on the first two documents through the loop, the [canaries](GUIDELINES.md#canary), and the assignment of steps to tiers that follows. The canaries are [drc-forge](projects/drc-forge.md), the item on checking chip layouts against manufacturing limits, and [bitstream-atlas](projects/bitstream-atlas.md), the item on documenting field-programmable gate array (FPGA) configuration files. [PROCESS.md 10, Model tiers](PROCESS.md#10-model-tiers) states the policy; this file is its evidence ([PROCESS.md 10.2, Pilot on the first canary](PROCESS.md#102-pilot-on-the-first-canary)).

The mapping from tiers to specific AI models lives in the private workflow notes and changes as AI models do; no AI company or product is named here ([GUIDELINES.md 5, Sources, provenance and confidentiality](GUIDELINES.md#5-sources-provenance-and-confidentiality)). Every number below was copied on 2026-10-21 from the files named in [section 2, The protocol](#2-the-protocol); a number measured by one agent run is one source ([GUIDELINES.md 2, Principles](GUIDELINES.md#2-principles)), so a row is evidence, not a law.

*Status of this file: draft 1, 2026-10-21. First version, written after the second canary's first landing. The first canary's merge record ([PROCESS.md Step 3, Merge](PROCESS.md#step-3-merge)) and Tim's rubric scores and answers for both canaries are pending; [section 6, How this file changes](#6-how-this-file-changes) says what each will change.*

## 1. The assignment, as of 2026-10-21

**Each row is provisional.** It names the lowest [model tier](GUIDELINES.md#model-tier) the recorded runs support, with the evidence. [AI processes](GUIDELINES.md#ai-processes) are not rationed, so a step is allowed to run at several tiers in parallel and keep the best result ([PROCESS.md 10, Model tiers](PROCESS.md#10-model-tiers)); a row changes only when a recorded run contradicts it ([section 6, How this file changes](#6-how-this-file-changes)).

| Task | Tier | Evidence |
| --- | --- | --- |
| Extraction with the inputs listed: documents, papers, links, the lint | 4, with a second method as the check | [4.1](#41-step-0-the-source-pack): complete, four results inferred; [3.1](#31-step-0-repository-facts-at-three-tiers): one count wrong |
| Extraction that needs judgement: a licence in parts, a condition written as prose, a count that depends on a file format | 3 | [3.1](#31-step-0-repository-facts-at-three-tiers): tier 3 corrected its own count; [4.1](#41-step-0-the-source-pack): tier 4 named two licences wrongly |
| The writer's own fact checks and the verification sample | 2 | [3.1](#31-step-0-repository-facts-at-three-tiers): every tier 3 number reproduced from fresh clones |
| The whole first draft from a frozen pack | 2; tiers 1 and 3 in parallel for the argued sections | [3.3](#33-blind-scoring-of-the-four-drafts): tier 2 first by both scorers; tier 1 best argued, most unsupported |
| Blind rubric scoring of drafts | 1 and 3 together | [3.3](#33-blind-scoring-of-the-four-drafts): same top pick; tier 1 caught one misattribution tier 3 missed |
| Persona reviews | 1 and 3 on the same brief; 4 for readability and compliance | [4.2](#42-step-2-the-panel-at-four-tiers): tier 1 supplied mechanism, tier 3 the same conclusions, tier 4 literal checks |
| Anything that judges a licence file | 2 or above | [4.2](#42-step-2-the-panel-at-four-tiers): the tier 2 licensing review alone verified the paid-edition fact |
| The executor test | 3, on every specimen the Corpus line names | [4.3](#43-the-executor-test-at-two-tiers): tier 3 found the failure; tier 4 reported one chosen specimen passing |
| The merge and the referee | 1 | [4.2](#42-step-2-the-panel-at-four-tiers): sixty merged findings; two rejections, each with a second signature |
| The claim audit | 3, with an independent re-run | [4.4](#44-step-5-the-audit-and-step-6): eight of eight round trips reproduced on fresh clones |

## 2. The protocol

**What was varied.** The [model tier](GUIDELINES.md#model-tier), with the brief, the inputs and the draft held fixed.

- First canary, [Step 0, Source pack](PROCESS.md#step-0-source-pack): one repository-facts brief at tiers 4 and 3, then a verification sample at tier 2 from fresh clones.
- First canary, [Step 1, Draft](PROCESS.md#step-1-draft): four whole drafts from one frozen [source pack](GUIDELINES.md#source-pack), one per tier; blind scoring at tiers 1 and 3 on the twelve criteria of [PROCESS.md 7, Findings format and rubric](PROCESS.md#7-findings-format-and-rubric); one canonical draft assembled at tier 2.
- First canary, [Step 2, Review panel](PROCESS.md#step-2-review-panel): twelve [personas](GUIDELINES.md#persona), eleven of them at two tiers, on the same draft with its status line and writer's notes withheld.
- Second canary: extraction split by kind across tiers 2 to 4; fourteen reviews at tiers 1 to 4, with the silicon engineer, the AI lead and the executor each at two tiers; the merge at tier 1; the claim audit at tier 3; a readability rerun on draft 2 at tier 4.

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

The first canary is [drc-forge](projects/drc-forge.md). Its tier log covers Steps 0 to 2; the merge of its Step 2 panel is pending ([section 6, How this file changes](#6-how-this-file-changes)).

### 3.1 Step 0: repository facts at three tiers

One brief, fifteen repositories, eight checks per repository. The rest of the pack (Tim's documents, the papers, the trackers) was built at tier 2 in about two hours and about ninety tool calls, and is not compared across tiers.

| Tier | Wall time | Tool calls | Result |
| --- | --- | --- | --- |
| 4 | 7.3 min | 23 | Stopped early and wrote its file only after a nudge; 132 distinct identifiers by a single-line search where 262 exist; no archive checks |
| 3 | 6.4 min | 60 | Complete, evidence per fact, an honest could-not-verify list; counted 262 by parsing multi-line calls and flagged the 132 as wrong |
| 2 | about 10 min | about 12 | Verification sample from fresh clones: every tier 3 number reproduced; found the unified GF180MCU rule deck that neither had |

- The hypothesis that the smallest tier extracts well when the inputs are listed held for a simple count (546 identifiers, matched at every tier) and failed on a count that needed a judgement about the file format. A second counting method as the check would have caught it; [PROCESS.md 10.3, Working hypothesis](PROCESS.md#103-working-hypothesis) now requires one.
- The same 132 sat in draft 3 of [GUIDELINES.md](GUIDELINES.md) as an illustrative figure and was corrected in round 13: a number copied from one agent run is one source ([GUIDELINES.md 2, Principles](GUIDELINES.md#2-principles), principle 2).
- Tier 4 ended its first run without writing its file. [PROCESS.md 12, What agents are allowed to do on their own](PROCESS.md#12-what-agents-are-allowed-to-do-on-their-own) now requires every brief to end with the check that the output file exists.

### 3.2 Step 1: four drafts from one frozen pack

Each tier wrote the whole document from the same pack and the same brief, in parallel.

| Written at tier | Wall time | Tool calls | Words | Skim path | Workstreams | Lint |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | 43.8 min | 55 | about 6,000 | 1,239 | 4 | 0 failures, 104 warnings |
| 2 | 18.1 min | 46 | 5,996 | 1,249 | 5 | 0 failures, 122 warnings |
| 3 | 19.4 min | 65 | 5,940 | 1,247 | 4 | 0 failures, 68 warnings |
| 4 | 22.1 min | 62 | 5,984 | 1,245 | not logged | 1 failure, 74 warnings, after its claim ids were stripped |

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

Twenty-three review files on the canonical draft, at most fifteen findings each. The merge, which decides which findings are accepted and records each reviewer's precision and severity calibration, is pending; the counts are here so that the merge record can be read against them.

| Persona | Brief | Tiers run | Findings raised |
| --- | --- | --- | --- |
| Silicon engineer | [A.1](PROCESS.md#appendix-a-reviewer-briefs) | 1, 3 | 15, 13 |
| AI lead | [A.2](PROCESS.md#appendix-a-reviewer-briefs) | 1, 3 | 15, 13 |
| Maintainer | [A.3](PROCESS.md#appendix-a-reviewer-briefs) | 1, 3 | 12, 10 |
| First-time reader | [A.4](PROCESS.md#appendix-a-reviewer-briefs) | 3, 4 | 15, 14 |
| Executor | [A.5](PROCESS.md#appendix-a-reviewer-briefs) | 3, 4 | 10, 7 |
| Compliance checker | [A.6](PROCESS.md#appendix-a-reviewer-briefs) | 3, 4 | 8, 12 |
| Foundry engineer | [A.8](PROCESS.md#appendix-a-reviewer-briefs) | 1, 3 | 15, 9 |
| Engine developer | [A.9](PROCESS.md#appendix-a-reviewer-briefs) | 3 | 12 |
| Readability reviewer | [A.14](PROCESS.md#appendix-a-reviewer-briefs) | 3, 4 | 14, 15 |
| Licensing reviewer | [A.15](PROCESS.md#appendix-a-reviewer-briefs) | 1, 3 | 14, 10 |
| The stranger | [A.16](PROCESS.md#appendix-a-reviewer-briefs) | 3, 4 | 14, 15 |
| The opponent | [A.17](PROCESS.md#appendix-a-reviewer-briefs) | 1, 3 | 15, 15 |

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
| Readability rerun, draft 2 | 4 | 15 | not in the merge record | | Measured the skim path with the new lint where the writer quoted the old |
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
- The referee at tier 1 confirmed the failure on three database states and two assembler branches; the audit's third run, at tier 3 from fresh clones at the pinned commits, reproduced the counts on all eight designs. The document's Goal changed from one part meeting the bar to no part meeting the test yet.
- The brief now says "run every specimen the Corpus line names": [GUIDELINES.md 4.14, Start here](GUIDELINES.md#414-start-here) and [PROCESS.md 10.2, Pilot on the first canary](PROCESS.md#102-pilot-on-the-first-canary) (round 18).

### 4.4 Step 5, the audit, and Step 6

- The claim audit ran at tier 3: 54 unresolved items; an [unsupported rate](GUIDELINES.md#unsupported-rate) of 14 of 28 in the attribution and absence classes and 11 of 42 in the stratified sample; 44 links logged with method and date; 12 papers resolved through a scholarly index; every internal link checked.
- Its independent re-run of the round trip, a third agent run on fresh clones at the pinned commits, matched the referee's counts on all eight designs and became a row of the pack. A tier 3 auditor with a re-run was enough; nothing in the audit needed a larger tier.
- Draft 2 landed on main after the audit with five questions on decision cards and the once-per-iteration post to Tim ([PROCESS.md 6.1, The packet](PROCESS.md#61-the-packet)). Tim's rubric score and answers are pending, so the second canary's [Step 7, Tim's turn](PROCESS.md#step-7-tims-turn) is not in this version.

## 5. What held and what failed, by tier

**Tier 1.** The largest [model tier](GUIDELINES.md#model-tier): mechanism, argument and the merge held; lint discipline did not.

- Held: the mechanism behind a finding (the four tier 1 reviews of the second canary had no rejected finding); the best argued sections and questions in a draft; the merge, with a second signature on each rejection; one scoring catch the tier 3 scorer missed.
- Failed: the most unsupported sentences of the four drafts; every claim id dropped and collision words hyphenated to satisfy the lint; about twice the wall time of the other tiers for a draft.

**Tier 2.** The best whole draft and the verification work held; one sentence failed.

- Held: the best whole draft by both scorers; the verification sample from fresh clones; the only verified licence fact in a panel of fourteen; the second canary's writer from pack to landing.
- Failed: one bound stated inverted; one miscount, caught on its own recount; sources cut to fit a limit.

**Tier 3.** Counting, honesty and the audit held; severity ran high.

- Held: counts that depend on a file format, corrected without being asked; honest could-not-verify lists; the executor that measured instead of arguing; the claim audit with an independent re-run; a scorer that agreed with tier 1 on the top pick and the main errors.
- Failed: severity about one level high in reviews; one misattribution missed in scoring; workstreams cut to fit the band.

**Tier 4.** Literal checks held; judgement did not.

- Held: complete extraction of documents with names, funding and prices withheld; literal checks (document ids, licence texts, link resolution, one round trip); the readability rerun; catching a count error in the rules.
- Failed: a count that needed a format judgement; licences in parts; severity one level high; a passing verdict on one chosen specimen; a run that stopped without writing its file.

**Not the tier.** Four findings held at every tier and belong to the loop, not the AI model.

- Limits read as targets: every draft sat within 1% of both ceilings ([3.2](#32-step-1-four-drafts-from-one-frozen-pack)).
- Reach is the instrument's: what a sandbox cannot fetch, no tier can verify ([section 2, The protocol](#2-the-protocol)).
- A missing structural element is caught by a count, not by a reader: fourteen reviewers missed the absent claim ids ([4.2](#42-step-2-the-panel-at-four-tiers)).
- A brief's flaws propagate: a shared folder, a wrong address or a missing output-file check costs the same at every tier ([section 2, The protocol](#2-the-protocol)).
- Reviewing at two tiers with the same brief catches different things, as [PROCESS.md 10.3, Working hypothesis](PROCESS.md#103-working-hypothesis) expected: confirmed for the silicon-engineer and AI-lead pairs, where tier 1 added mechanism and tier 3 added one catch each. No brief ran at three tiers, so whether a third adds little is untested.

## 6. How this file changes

**What is pending.** Three records; each changes [model tier](GUIDELINES.md#model-tier) rows as a dated revision.

- The first canary's merge record: precision and calibration per reviewer, for twelve personas at two tiers, a larger sample than the second canary's fourteen reviews. It fills the Accepted and Rejected columns that [3.4](#34-step-2-twelve-personas-at-two-tiers) lacks.
- Tim's rubric scores and answers for both canaries ([PROCESS.md Step 7, Tim's turn](PROCESS.md#step-7-tims-turn)): the scores check the two AI scorers of [3.3](#33-blind-scoring-of-the-four-drafts) against a person; the answers check the panels' severities.
- The experiment [PROCESS.md 10.3, Working hypothesis](PROCESS.md#103-working-hypothesis) names and the first canary did not run: the same section drafted several times at the small tier and selected by the lint and the audit, against one large-tier draft.

**How a row changes.** Only a recorded run changes a row of [section 1](#1-the-assignment-as-of-2026-10-21).

- An [item thread](GUIDELINES.md#item-thread) keeps its `tier-log.md` and sends what contradicts or extends a row to the guidelines thread, which owns this file ([PROCESS.md 1, Roles](PROCESS.md#1-roles)); the row changes with the run named.
- As more documents go through, the per-canary sections become one table per step, and [section 1](#1-the-assignment-as-of-2026-10-21) is re-derived from them.
- When the AI models behind the tiers change, the tiers are re-labelled in the private notes and the data here keeps the date of its runs; a row older than the models it was measured on is marked so.
- This file obeys the rules the other guideline files obey ([PROCESS.md 13, The guideline files obey their own rules](PROCESS.md#13-the-guideline-files-obey-their-own-rules)); what the lint reports on it is recorded in the revision history.

## Revision history

- **Draft 1, 2026-10-21.** First version, from the two canaries' tier logs, the first canary's scoring and review files and the second canary's merge record and audit, written after the second canary's first landing.
  - The lint at 853cfcd on this file reports 71 collision-word lines ([L21](PROCESS.md#appendix-b-the-lint-toolscheckpy)), every one of them `tier N` ([GUIDELINES.md 6.8, Words: pointers, terms and second readings](GUIDELINES.md#68-words-pointers-terms-and-second-readings)), and nothing from [L19](PROCESS.md#appendix-b-the-lint-toolscheckpy), [L20](PROCESS.md#appendix-b-the-lint-toolscheckpy), [L22](PROCESS.md#appendix-b-the-lint-toolscheckpy), [L25](PROCESS.md#appendix-b-the-lint-toolscheckpy), [L26](PROCESS.md#appendix-b-the-lint-toolscheckpy) or [L27](PROCESS.md#appendix-b-the-lint-toolscheckpy); the checks that read the template's headings, blocks and status line do not apply ([PROCESS.md 13, The guideline files obey their own rules](PROCESS.md#13-the-guideline-files-obey-their-own-rules)).
