# Guidelines for item documents

The hit list is Tim's list of open-silicon projects worth doing, described in [README.md](README.md); Tim is Tim Ansell (GitHub [mithro](https://github.com/mithro)), whose idea the list is and whose design documents, talks and experiments are the record most items rest on. Every item on the list has a document at `projects/<id>.md`, mirrored as a [living doc](#8-glossary) (see [SYNC.md](SYNC.md)). This file is the contract for those documents: what each must contain, how claims are sourced, what is allowed to be published, and when a document is done. [TEMPLATE.md](TEMPLATE.md), beside this file at the repository root, is the skeleton to fill in. [PROCESS.md](PROCESS.md) is how a document is written, reviewed and iterated with AI agents and with Tim.

The documents are public. They are written for frontier AI models and for people, in that order. Their job is to turn a one-paragraph idea into a brief an agent can plan and start executing from, without first having to ask the person who had the idea, and to distil what Tim has already worked out so nobody rediscovers it. Every part of a document is written for a stranger who has only that part, little time, no one to ask, and no reason to take anyone's word for anything, Tim's included ([section 1, One principle](#1-one-principle)). A writer starts with the fifteen hard rules ([section 0, The fifteen hard rules](#0-the-fifteen-hard-rules)) and the [source pack](#8-glossary) ([PROCESS.md Step 0, Source pack](PROCESS.md#step-0-source-pack)).

*Status of this file: draft 4, 2026-10-21, in progress. Draft 1 was reviewed by an AI [panel](#8-glossary) of eleven [persona](#8-glossary) reviews and two template dry runs; draft 2 applied their findings; draft 3 rewrote the file around one principle ([section 1, One principle](#1-one-principle)) in the writer's own words. Draft 3 was reviewed by five readers who read it from the reader's situation (the stranger, the readability and clarity reviewer, the self-application auditor, the opponent and the claim verifier); draft 4 applies their findings in committed rounds, listed at the end. What still breaks the file's own rules is recorded in the self-application audit ([PROCESS.md section 13, The guideline files obey their own rules](PROCESS.md#13-the-guideline-files-obey-their-own-rules)).*

## 0. The fifteen hard rules

Given to every writer with the template. Sections [1, One principle](#1-one-principle), [2, Principles](#2-principles) and [9, References](#9-references) explain them; sections [3, Structure of an item document](#3-structure-of-an-item-document) to [7, Definition of done](#7-definition-of-done) are the rules in full, and the glossary ([8, Glossary](#8-glossary)) defines the words.

1. **Pack only.** Write from the [source pack](#8-glossary) only; a claim not in the pack goes into the pack, with its source, before it is used.
2. **Source or status.** Every claim links to its source, or carries one sanctioned status ([5.4, Claim statuses](#54-claim-statuses)), or both where the status is `(as of YYYY-MM)` on a linked state-of-the-art claim; a bare `Unknown` or `estimate` is not a status. Never invent: write `None found (searched: …)`, `Unknown (settled by: …)` or `Not applicable (…)`.
3. **Nothing from memory.** Never cite a paper, repository or document from memory; resolve it with a tool and copy the identifier.
4. **Tim's material through the allow-list.** Link Tim's material only through the allow-list ([5.1, Link allow-list](#51-link-allow-list)). A document flagged internal or confidential, or listed as held back, is not linked until Tim clears it, and the clearance date is recorded in the resources entry. Internal material gives technical ideas only, marked, with no title or fragment. Confidential material gives nothing.
5. **Nothing private.** From private material, nothing about partners, funding, customers, contacts, contractors, grant or contract terms, internal programme names or prices, and no quotation; a price comes only from a public price list ([4.10, Needs beyond AI processes](#410-needs-beyond-ai-processes)), never from a vendor's quote; public facts about public partners and quotations of public documents are allowed ([5.3, Naming](#53-naming), [4.7, What Tim has already worked out](#47-what-tim-has-already-worked-out)). No AI company, product or sponsor. Never which organisation asked for the list.
6. **Tim's claims checked.** Attribute to Tim only what you read in his documents, and say what you read. Invent no position for him, and check his claims as you would anyone else's: a claim of his, from a document, a thread answer or a doc comment, carries the status `(Tim's claim, YYYY-MM; checked: <how> | not checked)` ([5.4, Claim statuses](#54-claim-statuses)) and never stands as fact.
7. **An oracle per workstream.** Every workstream has an [oracle](#8-glossary) with a [negative control](#8-glossary) and stated blind spots; fit is derived from the [binding constraint](#8-glossary) (none, oracle, access, compute, knowledge or decision), never asserted.
8. **M1 on public resources.** [M1, First checkable result](#49-work-plan-and-milestones) needs only public resources, no-cost vendor editions and at most one board sold to the public at a listed price, the only paid item, and nothing under a non-disclosure agreement (NDA); every Needs line names only what exists at the time of writing or is produced by an earlier rung.
9. **Dated and classed.** Every state-of-the-art claim carries `(as of YYYY-MM)`; every tool carries a status word from [5.5, Status of tools and projects](#55-status-of-tools-and-projects) and its [licence class](#8-glossary) ([open-source](#8-glossary), [source-available](#8-glossary) or [proprietary](#8-glossary)) from [5.6, Licences](#56-licences).
10. **Numbers from a source.** Dates, numbers and counts come from a named source, or are marked `(estimate)` with what will replace them.
11. **The template's form.** Use the template's headings, order and bold [lead-ins](#8-glossary) exactly; after each lead-in the first sentence is the conclusion; three or more parallel things are a list, things with the same attributes a table, a structure a diagram with a caption ([6.7, Readability and presentation](#67-readability-and-presentation)); delete every [guidance line](#8-glossary); write no generated section.
12. **One entry, full names, links.** Each paper and each repository has one reference entry (identifier, licence, status, contents), under Start here (Key papers, Projects and code); every other mention names it in full, as every pointer does, for a reader who lands mid-document, and links to the same target ([6.8, Words: pointers, terms and second readings](#68-words-pointers-terms-and-second-readings)); coin no term; replace or pin every word with a second meaning; link every section, id, item, tool, paper, term and file that can be linked ([6.9, Links](#69-links)).
13. **Within the band.** Keep the document within 3,000 to 6,000 words, counted as [6.2, Length](#62-length) says (the hand-written part, link addresses and table separator rows removed; the [lint](#8-glossary) warns outside the band and fails above 7,000), and the summary within 60 to 120 words.
14. **No outside contact.** Never, from an [item thread](#8-glossary), open an issue or pull request in another project, write to Tim's files, or contact anyone outside the project; a person named in `DECISIONS.md` owns and opens any upstream contribution ([5.8, Upstream contributions](#58-upstream-contributions)).
15. **Unsure is not published.** When unsure whether something is allowed to be published, it is not: ask in the private [packet](#8-glossary) ([PROCESS.md 6.1, The packet](PROCESS.md#61-the-packet)), never in the document, which carries at most `Unknown (settled by: a question to Tim, YYYY-MM-DD)` and no description of the material.

## 1. One principle

**The principle.** Every part of an item document is written for a stranger who has only that part, little time, no one to ask, and no reason to take anyone's word for anything, Tim's included.

The stranger is one of three readers: an AI agent handed the document as its brief; a person deciding whether to point people, compute or money at the item; or a domain expert who wants to check the claims, contribute, or disagree. All three arrive through a link to a heading as often as from the top. None can reach the person who had the idea, and no document depends on their doing so. So whatever a reader needs to understand a sentence, to find the next thing, and to check a claim has to be in that sentence, in its section, or one link away.

Everything else in this file follows from that:

| Corollary | What it requires of a document | Where the rules are |
| --- | --- | --- |
| Each part stands alone | A term is defined where it is used | [6.8, Words: pointers, terms and second readings](#68-words-pointers-terms-and-second-readings) |
| Each part stands alone | A pointer names what it points to | [6.8, Words: pointers, terms and second readings](#68-words-pointers-terms-and-second-readings), [6.9, Links](#69-links) |
| Each part stands alone | Everything that can be linked is linked | [6.9, Links](#69-links) |
| Each part stands alone | A sentence has one reading | [6.8, Words: pointers, terms and second readings](#68-words-pointers-terms-and-second-readings) |
| Claims are checked, not believed | Every claim carries a source or a status | [5.4, Claim statuses](#54-claim-statuses) |
| Claims are checked, not believed | No single source, person or tool is trusted alone | [2, Principles](#2-principles); [4.9, Work plan and milestones](#49-work-plan-and-milestones) (Cross-checks) |
| Claims are checked, not believed | A key result climbs a [verification ladder](#8-glossary) | [4.9, Work plan and milestones](#49-work-plan-and-milestones) (Cross-checks) |
| Claims are checked, not believed | A claim that breaks physics is wrong until shown otherwise | [2, Principles](#2-principles) |
| The reader's time is respected | A reader who stops after the summary, or after the [skim path](#8-glossary), still has the gist | [6.7, Readability and presentation](#67-readability-and-presentation) |
| The reader's time is respected | The first sentence after each [lead-in](#8-glossary) is the conclusion | [6.7, Readability and presentation](#67-readability-and-presentation) |
| The reader's time is respected | The form of each element shows the shape of its content | [6.7, Readability and presentation](#67-readability-and-presentation) |
| An agent can start | The goal is written as acceptance criteria | [4.2, Goal](#42-goal) |
| An agent can start | Every workstream has an [oracle](#8-glossary) | [4.9, Work plan and milestones](#49-work-plan-and-milestones) |
| An agent can start | Start here names the first task, its check and the access to ask for | [4.14, Start here](#414-start-here) |
| Open is argued, not assumed | Each document says, for its own item, why doing the work closed would not produce the breakthrough | [4.5, Why it must be open](#45-why-it-must-be-open) |
| Open is argued, not assumed | Open means anyone can reproduce and replicate the result and change what produced it | [4.5, Why it must be open](#45-why-it-must-be-open) |
| Open is argued, not assumed | A licence that only looks open is named as such | [4.5, Why it must be open](#45-why-it-must-be-open), [4.6, State of the art](#46-state-of-the-art) |
| This file obeys its own rules | The guidelines, the template and the process file are held to every check they set | [7, Definition of done](#7-definition-of-done); [PROCESS.md 13, The guideline files obey their own rules](PROCESS.md#13-the-guideline-files-obey-their-own-rules) |
| This file obeys its own rules | They are reviewed from the reader's situation, not the writer's | [PROCESS.md 13, The guideline files obey their own rules](PROCESS.md#13-the-guideline-files-obey-their-own-rules) |
| This file obeys its own rules | What still breaks is recorded in the self-application audit until the count is zero | [PROCESS.md 13, The guideline files obey their own rules](PROCESS.md#13-the-guideline-files-obey-their-own-rules) |

**What a document is for.** It turns a one-paragraph idea into a brief an agent can plan and start executing from without asking the person who had the idea; it makes the case for the item to a person who decides; and it distils what Tim has already worked out, in design documents, talks, experiments and dead ends, so that nobody rediscovers it. Tim's record is the richest source most items have, and it is a source: mined in full, attributed exactly, and checked like any other ([principle 7, Distil Tim's record, and check it](#21-checking)). Where the record runs out, the document asks him targeted questions and folds the answers in as his claims, with what was done to check them.

**The tests of a finished document.** Four readers, four tests: the agent, the five-minute reader, the stranger in the middle and the opponent; [PROCESS.md 5.1, Core panel for the canaries](PROCESS.md#51-core-panel-for-the-canaries) runs each.

1. *The agent.* Having read nothing else, it can state the goal as acceptance criteria, name the first task with its oracle and where the result lands, list the access it needs and the role that holds it, name the items upstream and downstream, and say why the work must be open. The [agent digest](#8-glossary) at the top of [4.14 Start here](#414-start-here) carries the first four; [4.5 Why it must be open](#45-why-it-must-be-open) carries the fifth.
2. *The five-minute reader.* Reading only the skim path defined in [6.7, Readability and presentation](#67-readability-and-presentation), they can say what the item produces, why it matters, what it unlocks, how the work is cut up and checked, what it needs, the biggest risk and where to start.
3. *The stranger in the middle.* Arriving at any section from a link, they can resolve every term, id and pointer in it from that section and the [glossary](#8-glossary), and reach each thing it refers to in one click.
4. *The opponent.* Reading each sentence that states a number, a capability, a requirement or a prohibition as uncharitably as possible, they find no second reading, and they can check every claim from what it links to, or see from its status why it cannot yet be checked.

## 2. Principles

The principles are the reasons behind the rules of sections [4, Section requirements](#4-section-requirements) to [6, Style and mechanics](#6-style-and-mechanics). Each gives the claim, the reason behind it, and where a document applies it. Several rest on claims about the world (that published results often fail to reproduce; that the open tools are slow). Those are claims like any other: their evidence is in [section 9, References](#9-references), and each item's document re-checks them for its own tools and sources rather than inheriting them.

**Working assumption.** The work is done by an organisation with effectively unlimited [AI processes](#8-glossary). No document costs tokens, rations agent runs or picks a smaller AI model to save money; what a document accounts for is everything else that can bind: the [oracle](#8-glossary), access to hardware and foundries, other compute (simulation hours, GPUs), knowledge, decisions and people.

### 2.1 Checking

1. **Every claim has a source or a status.**
    - *Reason:* A reader who cannot see where a number, a date, "nobody has done X" or "tool Y cannot Z" comes from cannot check it, and the writer's own memory is the least reliable source there is.
    - *In the document:* Each such claim links to where it comes from or carries exactly one of the statuses in [5.4, Claim statuses](#54-claim-statuses); nothing is cited from memory; a paper, repository or document is resolved with a tool and its identifier copied. The claim audit in [PROCESS.md Step 5, Revise and audit](PROCESS.md#step-5-revise-and-audit) samples it.
2. **No single source is trusted, and no single person.**
    - *Reason:* Simulators have bugs. Published results fail to reproduce, highly cited ones included. Reports get details wrong. Companies have lied. What was impossible one year might be routine the next, so even a correct claim carries a date. Tim's documents, answers and rulings are sources with the same standing as any other: attributed exactly and checked.
    - *In the document:* Every decision number (a number in the Acceptance test, a Done when line, Metric and baseline or Shots on goal) has two independent sources (produced by different people with different tools or data) or a bound the writer computed; every tool result that matters has a second route to it; the sources a key result rests on are listed with their known failure modes ([4.9, Cross-checks](#49-work-plan-and-milestones)); what Tim worked out is reported with what was read and what was checked ([4.7, What Tim has already worked out](#47-what-tim-has-already-worked-out)).
3. **Physics bounds everything.**
    - *Reason:* A claim that breaks a fundamental limit is wrong until shown otherwise, and a result that contradicts an established one or beats the best published result is an extraordinary claim that needs extraordinary proof.
    - *In the document:* A headline figure is checked against a fundamental limit and a back-of-the-envelope estimate before it is believed; the [verification ladder](#8-glossary) names the bound and the limit for each key result ([4.9, Cross-checks](#49-work-plan-and-milestones)); an extraordinary claim needs [proof level](#8-glossary) [P3, agrees with an independent reference](#491-proof-levels) plus the first-principles rebuild rung of the ladder ([4.9.1, Proof levels](#491-proof-levels)).
4. **Every check is a proxy for physics, and every rule has a reason.**
    - *Reason:* A design-rule check, a SPICE circuit-simulation model, a timing check or a layout-versus-schematic comparison is a fast stand-in (fast in intent, even when slow in practice) for a question about manufacturing, manufacturing yield (the share of working dies), device physics or non-ideal conditions. Each design rule in such a check exists for a reason, and the reason might or might not matter for a given use; without it nobody can say when the design rule is allowed to be relaxed, and with a simulator accurate and fast enough the proxy would not be needed at all.
    - *In the document:* Every oracle names the physical question it stands in for (or what it checks directly, where it is not a proxy) and where the reason for each of its rules is recorded, or `Unknown (settled by: …)` ([4.9, Work plan and milestones](#49-work-plan-and-milestones), the Oracle lines); the [PDK](#8-glossary) audit workstream of PDK items records the reason behind each rule ([4.9, Work plan and milestones](#49-work-plan-and-milestones)); the fundamental-limit rung of the verification ladder is the direct check the proxy approximates ([4.9, Cross-checks](#49-work-plan-and-milestones)).
5. **Rebuild and compare.**
    - *Reason:* The strongest check on a result is an independent reconstruction from first principles, compared against the existing result, with a layer of abstraction added or removed where that separates or combines concerns more cleanly.
    - *In the document:* The verification ladder names the rebuild for each key result ([4.9, Cross-checks](#49-work-plan-and-milestones)).
6. **Rough first, accurate when it matters, effort in proportion.**
    - *Reason:* A fast answer settles most questions in minutes, and the verification a result gets is in proportion to the cost of its being wrong.
    - *In the document:* Each key quantity has a fast path and an accurate path used when the answer carries weight: Fast and accurate paths and the Effort rule ([4.9, Cross-checks](#49-work-plan-and-milestones)).
7. **Distil Tim's record, and check it.**
    - *Reason:* A reader learns what was worked out without opening the links; nothing is attributed to a document the writer has not read, no position is invented for Tim, and his claims are checked like anyone else's.
    - *In the document:* Design documents, talks, experiments and dead ends are paraphrased or briefly quoted in the body with attribution, not only listed at the end, and each of his claims carries what was done to check it, or the status that says it could not be ([4.7, What Tim has already worked out](#47-what-tim-has-already-worked-out), [4.13, Questions for Tim](#413-questions-for-tim)).

### 2.2 Working

8. **Oracles first.**
    - *Reason:* Work suits AI agents when the result can be checked without a person: a design-rule check, a layout-versus-schematic comparison, a circuit simulation, formal equivalence checking (a proof that two designs behave the same), a reference tool, hardware. Work with no oracle is where agents are weakest.
    - *In the document:* Every workstream names its oracle and what the oracle cannot see, and work with no oracle is flagged ([4.9, Work plan and milestones](#49-work-plan-and-milestones); [hard rule 7, An oracle per workstream](#0-the-fifteen-hard-rules)).
9. **Harness and benchmarks before the tool.**
    - *Reason:* The open tools in this field are mostly slow, often poorly written, and have few users despite their complexity; a simulator with excellent fundamentals can spend most of its time recomputing values whose inputs have not changed. A test suite and a benchmark let a tool be replaced with confidence, and replacement is often the only way to reach the iteration speed agents allow.
    - *In the document:* Speed and quality per tool and the replace-or-build-on decision ([4.6, State of the art](#46-state-of-the-art)); the "[Harness](#8-glossary), benchmarks and tool speed" workstream, with its share of the work stated, because keeping up with the iteration speed AI allows and verifying what it produces costs real effort in every item ([4.9, Work plan and milestones](#49-work-plan-and-milestones)).
10. **More attempts beat better guesses.**
    - *Reason:* Learning comes from the number of attempts and from lower barriers to trying, not from deciding in advance what is worth trying: a thousand times more attempts at a tenth of the success rate is a hundred times more results.
    - *In the document:* Where an oracle exists, the plan gates attempts on it rather than on judgement; where none exists, building one comes first ([principle 8, Oracles first](#22-working)); [Shots on goal](#8-glossary) ([4.3, Why it is high value](#43-why-it-is-high-value)); universal access argued in [4.5, Why it must be open](#45-why-it-must-be-open).
11. **If it were easy it would be done, and bad solutions outlive their reasons.**
    - *Reason:* Every item has a reason it has not already happened (a missing oracle, closed data, no money, no developer time, or nobody's job), and inertia and sunk cost keep worse solutions alive long after better ones exist. A past attempt that stopped is not a failed idea until the record shows the idea failed. Tim's claim (2026-10; checked per dead end in [4.7, What Tim has already worked out](#47-what-tim-has-already-worked-out)) is that most of his stopped for resources, software developer time above all; whether agents supply that time depends on an oracle gating the work ([principle 8, Oracles first](#22-working); the evidence is in [section 9, References](#9-references)).
    - *In the document:* The real reason is named under Why not already done and Why now ([4.3, Why it is high value](#43-why-it-is-high-value)); Past and parallel efforts ([4.6, State of the art](#46-state-of-the-art)); each dead end classed as the idea or the resources, with the evidence ([4.7, What Tim has already worked out](#47-what-tim-has-already-worked-out)).
12. **Honest about limits.**
    - *Reason:* An AI case that hides what agents cannot do for this item (physical access, legal judgement, tacit foundry knowledge, decisions, getting changes merged) sends agents where they will fail.
    - *In the document:* What agents cannot do and what has to be true for the AI case to hold ([4.8, What frontier models change](#48-what-frontier-models-change), [4.11, Unknowns, blockers and risks](#411-unknowns-blockers-and-risks)).
13. **The bar is physics and what agent-scale work needs, never the proprietary result.**
    - *Reason:* [Proprietary](#8-glossary) tools and results are what the old world built: slow to change, closed to the debugging and optimisation agents could do, licensed per seat, and so unable to serve work in which agents write code, debug, optimise and use compute at scale.
    - *In the document:* Proprietary tools and results appear as dated context, in a line each, never as the target; the bar an item sets itself is the physical limit, the first-principles bound, and what agent-scale work needs (iteration time, cost per attempt, reproducibility, no licence gate, the freedom to change the tool): The bar to clear ([4.6, State of the art](#46-state-of-the-art)); Metric and baseline ([4.9, Work plan and milestones](#49-work-plan-and-milestones)).

### 2.3 Writing

14. **Specific beats general.**
    - *Reason:* "Large, mechanical, checkable work that suits agents" is the thesis of the whole list; a sentence that would survive unchanged in another item's document adds nothing to it.
    - *In the document:* Name the tool, the family, the process node, the pull request, the number; each document shows which work, checked by which oracle, at what scale ([6.1, Voice](#61-voice) carries the rule).
15. **Open is a requirement, argued per item.**
    - *Reason:* Before anything can be changed it has to be understood, and before it can be understood it has to be reproduced from what is published and replicated independently. So open means that every input, tool and step needed to reproduce and replicate a result is available to anyone, under a licence that allows it to be studied, changed and redistributed. A [source-available](#8-glossary) licence (the Business Source License and its relatives), a delayed or partial release, or data and models (AI or device) published without what generated them is not open.
    - *In the document:* Each document explains, for its own item, why doing the work closed does not produce the breakthrough and what open has to mean for it, and says so wherever it meets a licence that only looks open ([4.5, Why it must be open](#45-why-it-must-be-open)); the [licence class](#8-glossary) of every tool in [4.6, State of the art](#46-state-of-the-art).
16. **Write so an agent can start.**
    - *Reason:* An agent that has to ask the person who had the idea before it can begin has not been given a brief.
    - *In the document:* The document ends with a Start here section an agent can act on at once: what to read, what to reproduce, the first tasks with oracles, the access to request, the known dead ends ([4.14, Start here](#414-start-here)).
17. **Dated and checked.**
    - *Reason:* A stale fact is worse than a missing one, and a link that has rotted takes its evidence with it.
    - *In the document:* State-of-the-art claims carry `(as of YYYY-MM)`; every link is fetched before [landing](#8-glossary); a missing fact is written as `None found (searched: …)` or `Unknown (settled by: …)`, never papered over ([5.4, Claim statuses](#54-claim-statuses), [5.10, Citations and links](#510-citations-and-links)).
18. **Public and safe.**
    - *Reason:* The repository is public, some of Tim's material is confidential or belongs to others, and nothing published can be unpublished.
    - *In the document:* Only links that pass [5.1, Link allow-list](#51-link-allow-list); technical ideas only, with no partners, funding, customers, contacts or prices from private material; AI described generically, with no AI company, product or sponsor named, and never who asked for the list ([5, Sources, provenance and confidentiality](#5-sources-provenance-and-confidentiality)).
19. **One home per fact.**
    - *Reason:* A fact with one home can be found and corrected; a restated one drifts.
    - *In the document:* Each required element has exactly one section ([3, Structure of an item document](#3-structure-of-an-item-document)); other sections point to it, with a link, and never restate it.
20. **Generated sections are generated.**
    - *Reason:* A hand-written copy of generated text drifts from [`items.json`](items.json) and is overwritten at the next build.
    - *In the document:* The id prefix of the title, "Where it sits", "Resources" and "Related items" come from [`items.json`](items.json) through [`tools/build.py`](tools/build.py); relationship changes are proposed for [`items.json`](items.json), never written into the document ([6.4, Title and the generated tail](#64-title-and-the-generated-tail)).
21. **Words that cannot be misread.**
    - *Reason:* A stranger who lands in the middle has no one to ask, and a word with two readings will be read the wrong way by someone.
    - *In the document:* Terms of the field are defined where they are used or replaced by plain words; no term is coined; a word with a second meaning is replaced or pinned; every pointer names what it points to; everything that can be linked is linked ([6.8, Words: pointers, terms and second readings](#68-words-pointers-terms-and-second-readings), [6.9, Links](#69-links)).

## 3. Structure of an item document

The hand-written sections sit between the title and the [generated tail](#8-glossary). [`tools/build.py`](tools/build.py) keeps the file's own title, adds the `<id>: ` prefix, strips the three generated sections wherever they are and re-appends them at the end. The template therefore ends with "Start here" and no generated headings ([section 6.4, Title and the generated tail](#64-title-and-the-generated-tail)).

| Order | Section | Home of |
| --- | --- | --- |
| 0 | `# <item id>: <item title>` | The stable id (generated) and the title (hand-written, kept by build.py). |
| 1 | Summary and status line (no heading) | What the item is in three to five sentences; which draft this is and who has reviewed it. |
| 2 | Goal | The end state as deliverables, the acceptance test, the [two-ways framing](#8-glossary), out of scope. |
| 3 | Why it is high value | The pain today, why not already done, who is waiting, why now, [shots on goal](#8-glossary). |
| 4 | What success unlocks | Needs first, unlocks on the list, cross-checks with other items, shared [harness](#8-glossary), beyond the list, compounding effects. |
| 5 | Why it must be open | The counterfactual, the strongest case against open, why closed does not deliver, what open must mean here. |
| 6 | State of the art | Open tools with [licence class](#8-glossary), speed and quality; the bar to clear; research results; past and parallel efforts; what is missing and what to replace or build on. |
| 7 | What Tim has already worked out | His proposals, numbers, experiments, dead ends and framing, per document read; where the record runs out. |
| 8 | What frontier models change | Why faster, why better, what has to be true, and in two sentences what people still do. |
| 9 | Work plan and milestones | Workstreams, the summary table, milestones, the dependency diagram, the metric and baseline, lead times, cross-checks; the parts are in [4.9, Work plan and milestones](#49-work-plan-and-milestones). |
| 10 | Needs beyond AI processes | Compute, licences, hardware, data, access, people, money, time: cost, lead time, who could provide it. |
| 11 | Unknowns, blockers and risks | Expertise barriers, hard blockers, and the risks of the approach (the [plausible-but-wrong risk](#8-glossary) first), each with its check. |
| 12 | Unanswered technical questions | Every technical question and known unknown anyone could take up, each with how to settle it, which workstream it blocks and who could take it. |
| 13 | Questions for Tim | Where the written record runs out. Transient. |
| 14 | Start here | The [agent digest](#8-glossary), then the brief: read, reproduce, first tasks, access to request, dead ends, key papers, projects and code. |
| 15 to 17 | Where it sits; Resources; Related items | Generated from [`items.json`](items.json). |

What happens to the sections the existing documents have (as of 2026-10, before any is rewritten to these guidelines):

| Section (as of 2026-10) | What happens | Where |
| --- | --- | --- |
| Goal | Stays; gains "Out of scope" | [4.2, Goal](#42-goal) |
| Why it is high value | Stays, restructured | [4.3, Why it is high value](#43-why-it-is-high-value) |
| State of the art | Stays; gains The bar to clear and the "Past and parallel efforts" table | [4.6, State of the art](#46-state-of-the-art) |
| PDK consistency audit and generated docs ([PDK](#8-glossary), process design kit; in [shadow-pdks](projects/shadow-pdks.md), [drc-forge](projects/drc-forge.md), [tcad-twin](projects/tcad-twin.md), [cell-foundry](projects/cell-foundry.md), [cloud-fab](projects/cloud-fab.md)) | Becomes a workstream in "Work plan and milestones" | [4.9, Work plan and milestones](#49-work-plan-and-milestones) |
| Open questions | Becomes "Unanswered technical questions"; questions only Tim can answer move to "Questions for Tim" | [4.12, Unanswered technical questions](#412-unanswered-technical-questions), [4.13, Questions for Tim](#413-questions-for-tim) |
| Sources | Dissolves: its links are cited where they are used | [5.10, Citations and links](#510-citations-and-links) |
| Where it sits; Resources; Related items | Unchanged (generated) | [6.4, Title and the generated tail](#64-title-and-the-generated-tail) |

`resources/<id>.md` keeps its role as the raw link collection. "Start here" is the curated subset with a reason for each entry. A new link found while writing goes into the resources file first, with the sharing check of [section 5.1, Link allow-list](#51-link-allow-list), through the [routed change](#8-glossary) ([PROCESS.md 12, What agents are allowed to do on their own](PROCESS.md#12-what-agents-are-allowed-to-do-on-their-own)); the document links it only after that.

## 4. Section requirements

Each block gives the purpose, the required elements, what to avoid, and where it helps an illustrative example. Required elements are written as **bold lead-ins** at the start of the paragraph or list that carries them, with the exact words shown, so a reader and the [lint](#8-glossary) can find them. Where a block says "as sub-headings", the bold names in its list are `###` sub-headings, as the template shows, and the [lead-ins](#8-glossary) inside them are the ones the template shows in bold. An element with nothing to say is not omitted: it carries one of the [sanctioned empty values](#8-glossary) of [section 5.4, Claim statuses](#54-claim-statuses). An item listed under **Avoid.**, when found, is a finding of severity minor unless a rule elsewhere sets a higher one ([PROCESS.md 5.4, Severity](PROCESS.md#54-severity)).

Length is governed by one document band ([section 6.2, Length](#62-length)), not by per-section bands. After each lead-in the first sentence states the element's conclusion, and the form of each element (prose, list, table, block or diagram) follows the shape of its content ([section 6.7, Readability and presentation](#67-readability-and-presentation)); pointers and terms follow [section 6.8, Words: pointers, terms and second readings](#68-words-pointers-terms-and-second-readings).

All examples in this section are **illustrative**. Their figures were verified on 2026-10-21 against the sources named; a writer re-verifies before reuse and never copies the sentences.

### 4.1 Summary and status line

**Purpose.** Let a skimming reader decide in one minute whether to read on. It is the first depth of reading ([6.7, Readability and presentation](#67-readability-and-presentation)) and stands alone.

**Required.** One paragraph of three to five sentences, 60 to 120 words, directly under the title: what the item produces, who uses it, what is broken (as of the date in the status line), and the one-line case for AI agents. Then the status line, in exactly this grammar:

`*Status: <draft N | stable draft | reviewed>, YYYY-MM-DD. AI review panel: <personas, comma-separated, or none yet>. Human review: <none | Tim, YYYY-MM-DD>. Questions for Tim: <N>. This document was drafted and reviewed with AI agents; human review is recorded here.*`

*draft N* means the document is still in the loop; *stable draft* means the loop's exit condition holds but Tim has not approved; *reviewed* is written only after Tim has approved the document ([PROCESS.md 4, Exit condition](PROCESS.md#4-exit-condition)). The last sentence is fixed text so that no reader mistakes an AI [persona](#8-glossary) for a human reviewer.

**Avoid.** Repeating the title. Adjectives in place of facts.

### 4.2 Goal

**Purpose.** Define "done" so precisely that two people would agree whether it has been reached.

**Required.** Four lead-ins, in this order.
- **Deliverables.** The artefacts that will exist (a database, a cell library or a software library, a tool, a corpus, a chip) with their essential properties (coverage, accuracy, speed, licence).
- **Acceptance test.** How someone would check the goal is met, with numbers where they exist. Where the number is not yet known, `Unknown (settled by: <the M0 measurement or decision>)`.
- **Framing.** The [two-ways framing](#8-glossary) in the writer's own words: which layer ([PDK](#8-glossary), tooling, IP blocks, proof in silicon), which function (interface, computation, storage) and which manual-to-generator shift this item performs. The generated "Where it sits" line carries the tags; the Goal explains them.
- **Out of scope.** Three to six things this item deliberately does not do, each with the item or candidate that does.

**Avoid.** Goals that are activities ("improve [DRC](#8-glossary)") instead of end states. Goals with no way to check them.

**Example (illustrative).** "Open DRC that checks a reticle-sized layout (about 26 x 33 mm) at a stated process node in under one hour on a stated cluster; for every open PDK, one test layout per design rule with a passing and a failing case; and a record per design rule stating the reason it exists with a public source. Acceptance: the engine's violation list matches a reference checker's on a pinned set of public [shuttle](#8-glossary) designs with every difference explained, and the per-rule suite covers every design rule in the [SKY130](https://github.com/google/skywater-pdk) (SkyWater's open 130 nm process design kit), [GF180MCU](https://github.com/google/gf180mcu-pdk) (GlobalFoundries' open 180 nm kit) and [IHP SG13G2](https://github.com/IHP-GmbH/IHP-Open-PDK) (IHP's open 130 nm BiCMOS kit) rule decks, where 'every rule' is the count taken from each rule deck's files at [M0, Baseline and harness](#49-work-plan-and-milestones) (baseline and [harness](#8-glossary))."

**Example (weak).** "Make open DRC fast and reliable enough for real designs."

### 4.3 Why it is high value

**Purpose.** Make the case before any work is done.

**Required.** Five lead-ins, in this order.
- **The pain today.** What takes how long, what is missing, what people do instead (pay for a licence, give up, use a closed tool), with sources or statuses.
- **Why not already done.** The real obstacle, since an obvious solution would already be in use: cost, access, a missing [oracle](#8-glossary), the scale of the tedium, software developer time, inertia, or the sunk cost that keeps a worse solution alive. Name it; "nobody thought of it" is not an answer.
- **Who is waiting.** The users and projects blocked by this, on this list and outside it.
- **Why now.** One or two sentences naming which of the three framings applies: *easy now with AI*, *unlocks other tasks*, *accelerates a kind of work or iteration*, with a clause on the manual-to-generator shift the Goal's Framing describes, and what changed (AI-model capability, compute price, a new open PDK, a licence) so that the obstacle above no longer holds. The mechanisms belong to [section 4.8, What frontier models change](#48-what-frontier-models-change); do not argue them here.
- **Shots on goal.** How many attempts (designs, runs, [tapeouts](#8-glossary), tests) per month the item makes possible against the number as of the status-line date, and the cost of one attempt before and after, with sources or `(estimate)` with what replaces it. A thousand times the attempts at a tenth of the success rate is a hundred times the results; say which side of that trade this item is on.

The dependency order of the list (what this item needs first, what it is a prerequisite for) lives in [section 4.4, What success unlocks](#44-what-success-unlocks) and the [agent digest](#8-glossary), not here; the manual-to-generator shift is owned by the Goal's **Framing**.

**Avoid.** Hype. Claims about [proprietary](#8-glossary) tools without a public source. Restating the Goal.

### 4.4 What success unlocks

**Purpose.** Show where the item sits in the list's dependency order and how success compounds.

**Required.** Six lead-ins, in this order.
- **Needs first.** The items this one depends on, each with what it must deliver first. Each must be listed under this item in [`items.json`](items.json)'s `related` map.
- **Unlocks on this list.** The items that become possible, cheaper or faster, each with the mechanism in a sentence. Each must be in `related` for this item; a missing relationship is proposed for [`items.json`](items.json) through the [routed change](#8-glossary) ([PROCESS.md 12, What agents are allowed to do on their own](PROCESS.md#12-what-agents-are-allowed-to-do-on-their-own)), never added to the document first.
- **Cross-checks with.** The items whose results check this item's results and vice versa (a simulated value against a measured one, an open tool's output against a [scoreboard](#8-glossary) run, a generated rule against a shuttle result), each with the quantity compared and the agreement expected. Each must be in `related`.
- **Shared harness.** The test suites and benchmarks this item shares with other items, and which item owns each.
- **Beyond the list.** Products, research, education, communities this enables.
- **Compounding.** Corpora and test suites that grow, data that future AI models learn from, work that becomes continuous (re-run on every tool change) instead of one-off.

**Avoid.** Repeating "Why it is high value". "Enables innovation".

### 4.5 Why it must be open

**Purpose.** Make clear that keeping this work open and universally accessible is a requirement for the breakthrough, not a preference, and argue it for this item specifically.

**Required.** Five lead-ins, in this order, and the mechanism table.
- **The closed version.** One or two sentences naming the closed tools or results that exist for this goal as dated context (the one line each under The bar to clear in [4.6, State of the art](#46-state-of-the-art) owns the description) and stating that their existence has not closed the gap: they cannot be reproduced, changed or run at agent scale.
- **The counterfactual.** Two sentences: what happens if this work is done closed, or not at all.
- **The strongest case against open.** The best argument that a closed or proprietary route would serve better here, and why it fails for this item.
- **Why closed does not deliver.** At least two of the mechanisms in the table below, applied with the item's specifics, each labelled *empirical* (with a citation), *contractual* (with the clause and its date, stated as a question per [5.9, Vendor terms](#59-vendor-terms)) or *normative* (said so).
- **What open means here.** What has to be true for this item to count as open, as a list:
  - the licence per artefact ([5.6, Licences](#56-licences) gives the defaults);
  - what has to be published for anyone to reproduce the result (inputs, tools, versions, steps) and to replicate it (enough of the method to rebuild it independently);
  - the public test suite;
  - whose consent any vendor or foundry data needs;
  - the [clean-room](#8-glossary) rule where the item touches a PDK ([5.7, Clean-room rule for PDK items](#57-clean-room-rule-for-pdk-items));
  - the licences that only look open, which this item must not build on or be mistaken for ([source-available](#8-glossary) and business-source licences, delayed or partial releases, models (AI or device) or data without their generating inputs), each named with the tool or project that carries it.

| Mechanism | What closed breaks | Usual label |
| --- | --- | --- |
| Reproducibility | A result on closed tools cannot be re-run or checked by others | empirical |
| Replicability | Nobody outside can rebuild the method independently and compare | empirical |
| Composability | Agents and people can only fix, extend and chain tools whose source they can change | empirical or normative |
| Legal scale | Per-seat licences and EULAs do not allow thousands of agents to run the work | contractual |
| Universal access | Any student, company or country can use an open result; a closed one is rationed | normative |
| Accumulation | Open material survives when it is copied and archived under persistent identifiers; closed material vanishes with its owner | empirical |
| AI itself | AI models learn from and act on open data and tools, so open work is what future AI models will be good at | empirical |
| Supportability | Users can fix what they depend on | normative |

The usual label is the kind of support each mechanism most often has; the label in a document is given per use, from the evidence the document actually has.

**Avoid.** A paragraph that could be pasted into another item unchanged. Arguing that open is nicer; argue that it is necessary.

**Example (illustrative, FPGA, field-programmable gate array).** "The vendor's tools know every bit of every FPGA part; the gap exists because that knowledge is sealed inside them. A closed documentation effort would recreate the seal. The [Project X-Ray](https://github.com/f4pga/prjxray) database (the open documentation of the Xilinx 7-series [bitstream](#8-glossary) format) is published under CC0 (the Creative Commons public-domain dedication), which is why [nextpnr-xilinx](https://github.com/gatecat/nextpnr-xilinx) (the nextpnr place-and-route port for Xilinx parts) could build its 7-series [FASM](#8-glossary) path on it without a per-tool deal, and why the data outlived the toolchain branches that first used it."

### 4.6 State of the art

**Purpose.** Tell the reader exactly where the field stands, so the work starts from the frontier and not from a blank page.

**Required.** Five sub-headings, in this order:
- **Open-source tools and projects.** Each named and linked, as a bullet whose first line is `- **<Tool>**: <status>, as of <YYYY-MM>` (the [5.5, Status of tools and projects](#55-status-of-tools-and-projects) vocabulary, so the lint can read it), followed by one nested line per attribute:
  - its [licence class](#8-glossary) and licence name ([5.6, Licences](#56-licences));
  - what it can do for this goal, and what it cannot;
  - its speed: runtime on a stated input, or `Unknown (settled by: …)`, and whether it recomputes values whose inputs have not changed;
  - its quality: tests, continuous integration, releases, user base;
  - whether the item builds on it or replaces it;
  - its reference entry (status, licence, contents) lives under "Projects and code" in [4.14, Start here](#414-start-here), and the link here points at the same target.
- **The bar to clear.** What the item measures itself against, in three parts. First, the physical limit and the first-principles bound for the key quantity (the [Verification ladder](#8-glossary) in [4.9, Work plan and milestones](#49-work-plan-and-milestones) carries the working). Second, what agent-scale work needs from a tool or result (iteration time, cost per attempt, reproducibility, no licence gate, the freedom to change it), as numbers where the Metric and baseline of [4.9, Work plan and milestones](#49-work-plan-and-milestones) has them. Third, as dated context in one line each, the proprietary tools or results that exist for this goal and the licence terms that keep them from agent-scale use; they are what the old world built, never the target, and the document does not dwell on them. A part with no public figure: `None found (searched: <where>, <date>)`.
- **Research results.** The papers or theses that established the methods, each resolved through a search tool with a one-line statement of what it showed. The project's paper trackers are the first place to look ([PROCESS.md Step 0, Source pack](PROCESS.md#step-0-source-pack)).
- **Past and parallel efforts.** A table: `| Effort | Years | What it did | Why it stopped, or where it stands | Link |`. Earlier open efforts at this goal and parallel efforts under way, with links (repositories, pull requests, branches, threads) and the reason they stopped as far as it is known: funding ended, maintainers left, the approach was too heavy, a vendor changed its tools, the result was never merged. Name projects and decisions, not people's failings. Where the reason is not known, `Unknown (settled by: asking <role> or reading <link>)`.
- **What is missing.** One list: the specific gaps between the open state and the Goal. Then the lead-in **Replace or build on.** Which existing tools the item builds on and which it replaces, with the reason (speed, quality, licence, maintainability) and the test suite or benchmark that makes the replacement safe.

**Avoid.** Undated claims. Tools listed without what they lack or without their licence class. Praise. A proprietary result treated as the goal. A citation that was not resolved with a search tool.

**Example (illustrative, status entry).** "SKY130 rule documentation: the `periphery-rules.rst` file in the [SkyWater PDK](https://github.com/google/skywater-pdk) repository carries 546 distinct `layer.N` design-rule identifiers when counted by regular expression (as of 2026-10; the count depends on the grouping rule and must be re-done per rule deck). The shuttle precheck deck `sky130A_mr.drc` (the [rule deck](#8-glossary) a shuttle runs before accepting a design) carries 282 output statements for 132 distinct design-rule identifiers under the same counting rule. Neither ships a per-rule test; the [IHP SG13G2 PDK](https://github.com/IHP-GmbH/IHP-Open-PDK) does ship a regression-test harness with [golden results](#8-glossary) (reference outputs taken as correct), marked for developers only, and notes that some rules have not been verified or tested."

### 4.7 What Tim has already worked out

**Purpose.** Capture the knowledge in Tim's design docs, talks, experiments and notes so it is not lost and not rediscovered. This is the section that distinguishes these documents from a survey, and the one Tim signs off before a document is called reviewed.

**Required.** Six lead-ins, in this order.
- **Documents.** For each relevant public document or talk of his (from `resources/<id>.md` and the mith.ro design-doc index): its title linked, what the writer read (`read in full` or `summary only`), and the **specific proposals, decisions and numbers** it contains, paraphrased or briefly quoted. A document the writer has not read at least in summary does not appear. A `summary only` entry carries only what the summary says.
- **Experiments and results.** What was tried, what was measured, what it showed.
- **Dead ends.** Approaches he tried or considered and why they were dropped, with the reason classed as *resources* (developer time, money, hardware, access) or *the idea* (it did not work, and what showed that). Tim's claim (2026-10; checked per dead end in this section): most of his dead ends stopped for lack of resources, mostly software developer time, not because the idea failed; AI changes that, so a resource-stopped dead end is a candidate first task where it is fit A and is cross-referenced from Start here. These are his; community dead ends belong in [4.6, State of the art](#46-state-of-the-art) and practical traps in [4.14, Start here](#414-start-here).
- **Framing inherited.** The choices the item inherits (the [two-ways framing](#8-glossary), the [manual-to-generator axis](#8-glossary), the "[stepping stones](#8-glossary)" view).
- **From unpublished notes.** Technical ideas from material that cannot be linked ([section 5.2, Material outside the allow-list](#52-material-outside-the-allow-list)), each sentence marked `(from Tim's unpublished notes)`, with no link, title, title fragment, partner, figure or name. These sentences are approved by Tim before the [landing](#8-glossary) that first carries them, and every landing runs [L18, the approval list](PROCESS.md#appendix-b-the-lint-toolscheckpy) against the list of sentences he has approved (a private file, given to the lint as `--signoff FILE`) ([PROCESS.md Step 5, Revise and audit](PROCESS.md#step-5-revise-and-audit)).
- **Where the written record runs out.** The specific points the documents do not settle. These become the "Questions for Tim" entries.

**Avoid.** Inventing positions for Tim. Attributing community results to him or his to the community. Listing links without content. Carrying content from a title.

**Example (illustrative, document entry).** "Tim's [Design Rule Check (DRC) Testing](https://docs.google.com/document/d/18z-FBJHni6qt1WR_tF6bbRHfQydKcFMAVnuj4Ixbj90/edit) (read in full; work in progress, last updated early 2023) proposes one test per [GDS](#8-glossary) file, each rule with pass and fail cases, and defines the verdicts: a pass case that fails DRC is a false positive, a fail case that passes is a false negative. It says interacting rules need specific tests around them, gives a density rule as its worked example, and leaves its fuzz, torture and performance headings empty, which is where the written record runs out."

### 4.8 What frontier models change

**Purpose.** Explain why frontier models could do this work faster and better than people, what has to be true for that to hold, and what people still do.

**Required.** Four lead-ins, in this order; no table.
- **Why faster.** The mechanisms that apply, each justified with the item's specifics: parallel execution of skilled-but-mechanical units (how many units, from a counted source or `(estimate)` with what replaces it); closed-loop iteration against an automated oracle (which oracle, the latency of one iteration); design-space search where evaluation is automated (how big the space is); reading the entire record (which record); cheap re-execution whenever a tool changes.
- **Why better.** Where people fail on this item: the work spans silos few people combine (name them); the work is too tedious to finish (what has been left unfinished); expertise is scarce in the open community (which); people sample the literature, an AI model can cross-reference all of it.
- **What has to be true.** The preconditions for the AI case: an oracle exists or must be built first; the inputs are public; the work decomposes into independent units; a person can supply X; and which of these rest on current AI-model capability or price, with the month, so the plan is re-checked when they change.
- **What people still do.** Two sentences on the parts of this item that stay with people (physical access, decisions, merges, legal judgement) and how an agent supports them, then a pointer to [section 4.11, Unknowns, blockers and risks](#411-unknowns-blockers-and-risks), which owns the itemised blockers and the [plausible-but-wrong risk](#8-glossary).

No human baseline, agent rate or duration is estimated: what is stated is the structural difference (how many units can run in parallel, the oracle's latency per iteration, the absence of a licence gate), each from a counted or sourced number or `Unknown (settled by: …)`. There is no table in this section. The per-workstream oracle, access, knowledge and fit live in the workstream blocks and the summary table of [section 4.9, Work plan and milestones](#49-work-plan-and-milestones); this section argues from them.

**Avoid.** "Agents can do this" with no mechanism. Capability claims not tied to an oracle. Hiding the work that stays with people.

**Example (illustrative).** "The SKY130 periphery rule document lists 546 design-rule identifiers (as of 2026-10, counted by regular expression). Each needs a passing and a failing layout; [KLayout](https://github.com/KLayout/klayout), the open-source layout editor and design-rule checker, decides whether one small layout violates a rule in a single run (seconds `(estimate)`, measured at [M0](#49-work-plan-and-milestones) for the pinned rule deck and machine), so each case is an independent unit that an agent can propose, run and fix with no person in the loop. People stopped early: the task is skilled but repetitive, and nobody is paid to finish it. The oracle is weaker for the design-rule *reasons*: an AI model can read the lithography and device literature and propose why a spacing rule exists, but the proposal needs a public source or measured data, which makes it a partial oracle until [tcad-twin](projects/tcad-twin.md) exists."

**Example (weak).** "This is well-specified, repetitive work that suits AI agents."

### 4.9 Work plan and milestones

**Purpose.** Name the core pieces of work and define how progress and success are measured. This is not a project plan; it is enough for an agent to build one.

**Required.** Six sub-headings, in this order: Workstreams, Summary table, Milestones (with Dependencies as a lead-in inside it), Metric and baseline, Lead times, Cross-checks; the [proof levels](#8-glossary) of [4.9.1, Proof levels](#491-proof-levels) serve the Milestones.

**Workstreams.** Three to eight, numbered W1 upward, one block each in this form:

```
**W1 <name>.** Produces: <artefact>. Needed because: <why the Goal needs it>.
- Oracle: <what decides>.
  - Stands in for: <the physical or manufacturing question this check is a proxy for, or "not a proxy: <what it checks directly>"; where the reason for each of its rules is recorded, or Unknown (settled by: …)>.
  - Reference: <where the expected answer comes from>.
  - Pass: <criterion>.
  - Latency: <per unit>.
  - Negative control: <a case that must fail, showing the oracle can fail>.
  - Blind spots: <what it cannot catch>.
- Access: <public | no-cost EULA | paid licence | NDA | membership | remote hardware | on-site hardware or lab | money | partner>, with what exactly.
- Knowledge: <public record | spread across silos | tacit | unknown>, with what exactly.
- Units: <how many independent units; the cap and what sets it>.
- Binding constraint: <none | oracle | access | compute | knowledge | decision>, because <reason>.
- Lands in: <repository or project>.
  - Contribution rules: <link or "this project's repository">.
  - Contribution gate: <what its maintainers require>.
- Fit: <A | B | C | D>, because <the binding constraint, from the line above>.
- Lead time: <none, or the name of the wait listed under Lead times>.
- Depends on: <workstreams, items, resources>.
- Suite quality (required for a workstream that produces a checker or a test suite; omitted otherwise): <share of deliberately broken inputs it catches, measured from M1>.
```

Fit is derived from the lines above it, never asserted:

| Fit | Derived when the Binding constraint line says | Who does what (as of 2026-10) |
| --- | --- | --- |
| A | none, or compute (the oracle is automated, access is public, units are many) | Agents do it; compute is requested under Needs beyond AI processes |
| B | access | Agents do it once the access is granted |
| C | knowledge, or decision | An agent drafts, a person decides |
| D | oracle, where the oracle is a person's judgement or a physical measurement | A person does it, an agent supports |

A workstream whose oracle does not exist yet is split: building the oracle is its own workstream, with its own fit. A workstream whose parts would take different fit values is split into workstreams that each take one value. A workstream whose product is a checker or a test suite also fills the `Suite quality:` line, required for it and omitted otherwise, with the quality metric of the suite itself: the share of deliberately broken inputs it catches (its mutation score), measured from [M1, First checkable result](#49-work-plan-and-milestones) on.

For PDK-layer items ([shadow-pdks](projects/shadow-pdks.md), [drc-forge](projects/drc-forge.md), [tcad-twin](projects/tcad-twin.md), [cell-foundry](projects/cell-foundry.md), [cloud-fab](projects/cloud-fab.md)) one workstream is **PDK consistency audit and generated docs**. Its clauses are: every view of every standard cell agrees; rule decks match the layer maps and the written rules; the reason for each design rule is recorded with its source, or marked `Unknown (settled by: …)`; documentation is generated from the PDK data. The block states which clauses apply to this item and why the others do not.

Every item has a workstream **Harness, benchmarks and tool speed**, or says in one line why it does not need one. It builds the [M0](#49-work-plan-and-milestones) harness; owns the benchmarks and test suites that let a tool be replaced with confidence; profiles where the existing tools spend their time, which is often recomputing values whose inputs have not changed; and carries the replace-or-build-on decisions of [4.6, State of the art](#46-state-of-the-art). Its share of the work is stated honestly: keeping up with the iteration speed AI allows, and verifying what it produces, costs real effort in every item.

**Summary table.** One row per workstream, derived from the blocks: `| # | Workstream | Oracle | Access | Units | Binding constraint | Fit |`. This is the only table of its kind in the document.

**Milestones.** A ladder of at least four rungs, each a block in the template's form, with these lines:
- *Done when*: measurable: a number, a passing suite, a public artefact.
- *Evidence*: what will exist and where.
- *Proof*: the level required ([section 4.9.1, Proof levels](#491-proof-levels)).
- *Needs*: only things that exist at the time of writing or are produced by an earlier rung, by name.
- *Completes*: the W-ids the rung finishes or advances.
- *Fit*: the least favourable fit among the workstreams the rung needs.
- *Gate*: who or what decides the rung is reached.

M4 applies exactly when some workstream has a silicon or physical oracle, a hardware access value, or a money value for a shuttle run or a lab. The rungs:
- **M0 Baseline and harness.** Reproduce the current open state and build the oracle: the harness, the benchmark, the reference results, the counts.
- **M1 First checkable result.** A narrow but real end-to-end win. Its *Needs* are public resources, no-cost vendor editions and at most one named board sold to the public at a listed price, which is the only paid item; nothing under a non-disclosure agreement (NDA).
- **M2 Usable.** Someone outside the project uses it for real work.
- **M3 Complete or at the bar.** The Goal's coverage target, or the bar to clear of [4.6, State of the art](#46-state-of-the-art), met.
- **M4 Proven in hardware or silicon.** Where it applies, with three extra lines: *Hardware* (board, shuttle, lab), *Test plan* (what is measured, how, against what), *What silicon returns and when* (the data, the turnaround, what a failure would mean). Where it does not apply: `Not applicable (<why>)`.

```mermaid
flowchart LR
  M0["M0 Baseline and harness<br/>Proof: P2"] --> M1["M1 First checkable result<br/>Proof: P2<br/>Needs: public, no-cost, at most one board"]
  M1 --> M2["M2 Usable<br/>Proof: P4"]
  M2 --> M3["M3 Complete or at the bar<br/>Proof: P3"]
  M3 -.-> M4["M4 Proven in hardware or silicon<br/>Proof: P5<br/>only where a workstream touches hardware"]
```

*Figure 1: The milestone ladder with the default [proof level](#8-glossary) of each rung; an arrow means "reached before"; the dashed arrow marks [M4, Proven in hardware or silicon](#49-work-plan-and-milestones) as conditional. Each rung is a state, never an activity.*

Where a rung touches silicon or hardware before [M4](#49-work-plan-and-milestones), the *Needs* line says so.

**Dependencies.** One diagram, drawn from the blocks: a diagram node per workstream and per milestone, and an arrow from each node to what depends on it, taken from the `Depends on` and `Completes` lines and from nothing else. The caption names the longest chain to [M3, Complete or at the bar](#49-work-plan-and-milestones) and any lead time on it. A proposed lint check will verify that the node ids are exactly the document's W and M ids ([L23, diagram ids](PROCESS.md#appendix-b-the-lint-toolscheckpy), proposed); the form of the diagram and of its caption follow [6.7, Readability and presentation](#67-readability-and-presentation).

**Metric and baseline.** For each number that tracks progress (several when the Goal has several deliverables), these parts, each on its own line in the template's form:
- its name, formula and unit, with the population and denominator ("design rules with both cases, over the design-rule count taken from the rule deck's files");
- the tolerance that counts as success, written before anything is measured;
- one *guardrail* metric that fails if the primary is gamed (coverage without a mutation score is gamed by trivial tests; speed without a violation-list match is gamed by skipping rules);
- the *baseline* as of the status-line date, as a median and range over a stated number of runs with pinned versions (tool commit, PDK release, benchmark tag, machine), or `Unknown (settled by: M0)`;
- where it is measured (the scoreboard item that scores it, otherwise a script committed at M0);
- the target.

Measurement items also state the instrument's coverage, repeatability and agreement with a reference.

**Lead times.** The waits that no effort shortens between the start of the work and [M3](#49-work-plan-and-milestones), and for [M4](#49-work-plan-and-milestones) where it applies (a shuttle cycle, a lab queue, a licence approval), each from a named source or `Unknown (settled by: …)`; each workstream's Lead time line names one of these waits, or none. No estimate of how long the work itself takes or how much code it needs: such numbers are guesses the reader cannot check, and nothing in the plan turns on them.

**Cross-checks.** The verification behind the plan, as four lead-ins.
- **Sources and failure modes.** A table `| Source | Trusted for | Known failure mode | Independent check |` for the sources the item's key results rest on (a simulator, a vendor datasheet, a paper, a tracker row, a measurement). No single source is trusted ([2.1, Checking](#21-checking)); the table says what would catch each one being wrong.
- **Verification ladder.** For each key result or headline number: the back-of-the-envelope bound the writer computed; the fundamental limit it must respect; the independent second source; the first-principles rebuild that would reproduce it, with the layer of abstraction added or removed to make the comparison clean; and the measurement that settles it. Say which rungs are in place and which milestone builds the rest.
- **Fast and accurate paths.** For each key quantity, the rough method that answers in minutes and the accurate method used when it matters, with the cost of each and when each is used.
- **Effort rule.** How much verification each class of result gets, in proportion to the consequence of its being wrong.

```mermaid
flowchart BT
  R1["Back-of-the-envelope bound<br/>minutes of arithmetic"] --> R2["Fundamental limit<br/>the physics the result must respect"]
  R2 --> R3["Independent second source<br/>a different tool, paper or measurement"]
  R3 --> R4["First-principles rebuild<br/>an abstraction layer added or removed"]
  R4 --> R5["Measurement<br/>hardware or silicon settles it"]
```

*Figure 2: The verification ladder every key result climbs, bottom to top; a document says which rungs are in place and which milestone builds the rest.*

#### 4.9.1 Proof levels

Each milestone's *Proof* line names the level its evidence must reach.

| Level | Meaning | Default for |
| --- | --- | --- |
| P0 | Stated; no artefact. | No rung |
| P1 | An artefact exists and its author ran it; logs are in the repository. | No rung |
| P2 | Reproduced from a clean checkout by continuous integration or by a second agent, with versions pinned. | M0, M1 |
| P3 | Agrees with an independent reference (a second engine, a vendor tool, a published result) with every difference explained. | M3 |
| P4 | Used or accepted outside the project: merged upstream, used by another project, or cited. | M2 |
| P5 | Proven in hardware or silicon: a board test or a shuttle result. | M4 |

The levels are kinds of evidence, not a scale: [P4, used outside the project](#491-proof-levels) does not imply [P3, agrees with an independent reference](#491-proof-levels), and a Proof line names every level the rung needs. The *Default for* column gives the level each rung needs by default; a document that departs from a default says why. A result that contradicts an established one, or a headline figure that beats the best published result, open or proprietary, is an extraordinary claim: it needs [P3](#491-proof-levels) with an independent reference and the first-principles rung of the verification ladder before it is stated as a result.

**Avoid.** Milestones that are activities ("investigate X") rather than states. Milestones with no evidence. *Needs* lines naming things that neither exist at the time of writing nor come from an earlier rung. A plan so detailed it will be wrong next month.

**Example (illustrative, M1 for an FPGA item).** "M1: one open [bitstream](#8-glossary) for a part of the 7-series FPGA family. Done when a small system on chip (SoC) with integrated main RAM, built with [Yosys](https://github.com/YosysHQ/yosys) (the open-source logic synthesis suite), [nextpnr-xilinx](https://github.com/gatecat/nextpnr-xilinx) and the [Project X-Ray](https://github.com/f4pga/prjxray) FASM path, boots on a named commodity board and passes its self-test. Evidence: bitstream, build log and board log in the repository, rebuilt by continuous integration. Proof: P2. Needs: the board; the [Project X-Ray](https://github.com/f4pga/prjxray) database (CC0); the no-cost vendor edition that covers the part, for reference bitstreams only. Fit: B. Gate: the self-test passes on the continuous-integration hardware a second time." An UltraScale+ rung is a later milestone, because as of 2026-10 [nextpnr-xilinx](https://github.com/gatecat/nextpnr-xilinx)'s UltraScale+ support goes through [RapidWright](https://github.com/Xilinx/RapidWright) (AMD's open-source framework over the Vivado device database) for the database and through [RapidWright](https://github.com/Xilinx/RapidWright) plus the vendor tool for the bitstream, and the open FASM path covers 7-series only.

**Example (weak milestone).** "M1: good UltraScale+ coverage."

### 4.10 Needs beyond AI processes

**Purpose.** List everything the work needs other than AI processes, so a sponsor knows the ask and an agent knows what to request.

**Required.** A table, one row per concrete need:

`| Kind | What exactly | Why | Who could provide it | Cost | Lead time | What can proceed without it |`

Kinds (a missing kind is a finding where the item needs it; the reviewer judges):

| Kind | Examples |
| --- | --- |
| Compute, other than AI processes | CPU-hours, memory, a cluster, GPUs for simulation |
| Software licences | Vendor electronic design automation (EDA) and FPGA tools, with the end-user licence agreement (EULA) question stated, not answered |
| Hardware | Boards, test chips, probe stations, oscilloscopes, a board farm |
| Data | Measured silicon, vendor documentation, golden results (reference outputs taken as correct) from reference tools, benchmark designs |
| Access | Foundry PDKs under NDA, shuttle slots, standards-body membership, maintainers willing to merge |
| People | Domain reviewers, a legal opinion, a lab, a person to author upstream contributions |
| Money | Shuttle runs, boards |
| Time | Shuttle cadence, fab turnaround, lab queues |

- *Cost* is an order of magnitude with a public price list linked, or `Unknown (settled by: …)`; never a quote or a figure from private material.
- *Lead time* is the wait no effort shortens, named as under Lead times in [4.9, Work plan and milestones](#49-work-plan-and-milestones).

AI processes are not a need: the work is assumed to be done by an organisation with effectively unlimited AI processes ([section 2, Principles](#2-principles), Working assumption), so nothing in the table costs tokens or rations agent runs.

Then two lead-ins in prose: **Licence questions.** The questions stated, not answered (does this EULA allow benchmarking, redistribution of outputs, thousands of automated runs), per [section 5.9, Vendor terms](#59-vendor-terms). **Clean room.** For PDK-layer items, how the rule of [section 5.7, Clean-room rule for PDK items](#57-clean-room-rule-for-pdk-items) applies to this item, and the declaration each contributor of rule values or device parameters makes that they have not read the confidential equivalent (or the role that collects it); for others, `Not applicable (<why>)`.

**Avoid.** Vendor quotes, prices from private documents, named contacts. Leaving out the licence question for vendor tools.

### 4.11 Unknowns, blockers and risks

**Purpose.** Say what is not known, what could stop the work, and where deep expertise is the barrier.

**Required.** Three sub-headings, in this order (technical unknowns with a path to an answer belong to [4.12, Unanswered technical questions](#412-unanswered-technical-questions), which owns them):
- **Expertise barriers.** The knowledge that defeats people because it is spread across domains, locked inside companies, or held by a few retiring experts; for each, how a frontier model gets through it (reading everything, combining silos, proposing and testing hypotheses) and how its answer is validated.
- **Hard blockers.** Legal (EULAs, the US Digital Millennium Copyright Act (DMCA), NDAs, export control), physical (needs silicon or a lab), economic (needs money), social (needs a vendor, a foundry, a standards body, a maintainer). For each: what an AI cannot do about it, what it can do (prepare, plan, de-risk), and the mitigation or the question to put to a person.
- **Risks of the approach.** How the work could succeed on paper and fail in practice, each with the check that catches it. The first risk is always **the plausible-but-wrong risk**: the specific way this item's AI-produced output could look right and be wrong (an invented rule reason, a parser that passes its own tests, a benchmark that games itself) and the check that catches it. Others, each a finding where it applies to the item: contamination of an open PDK with confidential data, including through an agent's own recall of material it has seen; a benchmark that measures the wrong thing; a result that depends on one tool version; a speed claim measured on an easy input.

**Avoid.** Hiding the hard blockers. Listing risks with no check.

### 4.12 Unanswered technical questions

**Purpose.** List the technical questions and known unknowns anyone could take up. This section owns them; no other section lists unanswered technical questions.

**Required.** Each question as a labelled list (the template shows the form): how it could be settled (an experiment, a measurement, a search, a prototype); which workstream it blocks, if any; and who could take it (an agent with public resources, or a role).

**Avoid.** Questions only Tim can answer (they go in [4.13, Questions for Tim](#413-questions-for-tim)). Questions already answered in the body.

### 4.13 Questions for Tim

**Purpose.** Capture, precisely, where the written record runs out, so Tim's answers can be folded in with the least effort on his side.

**Required.** At most five, most valuable first (the ones whose answer changes the most text), at most 300 words in all. Each: `**Q:** <one line, answerable in a line>. **Context:** <what the record says and does not say>. **Assumed for now:** <the draft's assumption>. **Changes if different:** <which sections move>.`

When Tim answers (in the item's thread in the project chat, or as a comment in the [living doc](#8-glossary)), the answer is written into the body as his claim with the [5.4, Claim statuses](#54-claim-statuses) status ("Tim's claim (2026-10; checked: …): …") and the question is removed. A question Tim parks is moved to [4.12, Unanswered technical questions](#412-unanswered-technical-questions) with that note. A question unanswered for seven days keeps its assumption, marked `(assumed; unanswered since YYYY-MM-DD)`, and the loop continues ([PROCESS.md 6.4, Defaults on silence](PROCESS.md#64-defaults-on-silence)). When the section is empty it is deleted and the status line reads `Questions for Tim: 0`.

**Avoid.** Questions the public record answers. Open-ended questions.

### 4.14 Start here

**Purpose.** The brief an agent (or a new contributor) acts on. The document ends with this, followed only by the generated sections.

**Required.** Eight sub-headings, in this order: the agent digest, then seven.
- **Agent digest.** At most 150 words in seven fixed lines: `Goal:` (as three tests), `First task:`, `Oracle:`, `Lands in:`, `Ask a person for:`, `Upstream / downstream:` (item ids), `Stop rule:` (the cap on one first attempt, in wall-clock minutes of one agent run, and what to report when it is reached; a cap, not an estimate of the work). An executor who reads only these lines must be able to begin.
- **Read first.** Three to six documents in reading order, one line each on why and an approximate size, every one read by the writer and recorded as read in the [source pack](#8-glossary).
- **Reproduce first.** One existing result to reproduce before anything else, so that the harness and the oracle are proven, as the labelled list the template gives (Source, Pin, Environment, Flow, Expected value, Runtime, Time box, Known-good and known-bad cases, Failure report), one line each. The tool flow is linked rather than pasted where it would rot; the time box is a cap on one attempt in wall-clock minutes of one agent run, not an estimate of the work; the known-good and known-bad cases show that the oracle itself was checked. If nothing suitable exists: `None found (searched: <where>, <date>)` and the [M0](#49-work-plan-and-milestones) task that creates it.
- **First tasks.** Three to five tasks an agent can start as of the status-line date, each a numbered entry in the template's form, with the nested lines Produce, Oracle, Inputs, Workstream (`W<n>`), Fit (`A`) and Lands in. All are fit A; a task that needs access is not a first task. The executor's test ([PROCESS.md 5.3, The executor's two-part test](PROCESS.md#53-the-executors-two-part-test)) is the check.
- **Ask a person for.** The access from [section 4.10, Needs beyond AI processes](#410-needs-beyond-ai-processes) an agent must request for the first milestones, and the role that holds it, never a named contact.
- **Known dead ends.** Specific traps from past attempts (a tool version that breaks, a standard-cell definition that is invalid, an approach that does not scale), each with a link. If none are known: `None found (searched: <where>, <date>)`.
- **Key papers.** At most fifteen papers or theses, fewer if fewer resolve, each resolved through a search tool with its DOI (digital object identifier) or arXiv identifier (or its id in [OpenAlex](https://openalex.org/), the open index of scholarly works, where it has neither) and a line on why it matters. Each paper has its one reference entry here; other sections name it by author and year and link to the same identifier ([6.9, Links](#69-links)).
- **Projects and code.** The repositories and branches to start from, including abandoned ones with unmerged work, each with its status ([section 5.5, Status of tools and projects](#55-status-of-tools-and-projects)), its licence, and what is in it. Each repository has its one reference entry here; other sections name it in full and link to the same target ([6.9, Links](#69-links)).

**Avoid.** Commands that will rot (link the project's own instructions). Papers from memory. A reading list without reasons. Duplicating the paper and project lists in other sections.

## 5. Sources, provenance and confidentiality

The repository is public. These rules are not optional; the [lint](#8-glossary) ([`tools/check.py`](tools/check.py), specified in [PROCESS.md Appendix B, The lint, `tools/check.py`](PROCESS.md#appendix-b-the-lint-toolscheckpy)) enforces the ones it can once it lands, and the compliance review checks the rest. The working-folder side of these rules (where the private material lives, how flags are recorded) is in the project's private workflow notes, not here.

### 5.1 Link allow-list

**Three ways in.** A link to Tim's material is allowed in a document only if it is (a) listed on [mith.ro](https://mith.ro) or in that site's pull requests, or (b) a Google Drive file shared with "anyone with the link", checked on a stated date, or (c) public: a repository, a paper, a vendor document, a public web page. Every link to Tim's material enters a document only through `resources/<id>.md` or `resources/misc.md`, where the sharing check is recorded; the lint rejects a Drive link in `projects/` that is not in a resources file ([L9, Drive links](PROCESS.md#appendix-b-the-lint-toolscheckpy)).

**Precedence.** A document flagged internal or confidential in the project's working notes, or listed as held back, is not linked even if a resources file lists it, until Tim clears it; the clearance date is recorded in the resources entry (public) and the ruling in `DECISIONS.md` in the [working folder](#8-glossary). A public document not yet in any resources file is a third status, `public, pending resources entry`: the entry is proposed first, the link follows.

```mermaid
flowchart TD
  A["A source document"] --> B{"Flagged internal or confidential,<br/>or listed as held back?"}
  B -->|yes| N1(["Not linked until Tim clears it<br/>(clearance date in the resources entry);<br/>confidential gives nothing,<br/>internal by Tim gives marked ideas only"])
  B -->|no| C{"Listed on mith.ro or its pull requests?"}
  C -->|yes, and in a resources file| L(["Link"])
  C -->|yes, in no resources file| P
  C -->|no| D{"Drive file shared with anyone with the link,<br/>checked on a date?"}
  D -->|yes, and in a resources file| L
  D -->|yes, in no resources file| P(["Public, pending resources entry:<br/>propose the entry, then link"])
  D -->|no| E{"Public: a repository, paper,<br/>vendor document or web page?"}
  E -->|yes| L
  E -->|no or unsure| N2(["Unsure is confidential: nothing"])
```

*Figure 3: Whether a source is allowed to be linked; diamonds are the tests in the order they are applied, rounded boxes are outcomes; a flag or a held-back listing wins over every later test until Tim clears it.*

### 5.2 Material outside the allow-list

**Three sensitivity classes.** Decided per source before writing:

- **Confidential** (government-marked or limited-sharing material, anything under a non-disclosure agreement (NDA), foundry-derived data, third-party reports, proposals or quotes received under conditions, anything read under conditions): contributes **nothing** to any repository file, not even an idea.
- **Internal and written by Tim**: contributes **technical ideas only**, each sentence marked `(from Tim's unpublished notes)`, with no link, title, title fragment, partner, figure or name, and each sentence approved by Tim before the [landing](#8-glossary) that first carries it; every landing runs [L18, the approval list](PROCESS.md#appendix-b-the-lint-toolscheckpy) against the list of sentences he has approved (a private file, given to the lint as `--signoff FILE`).
- **Unsure** is treated as confidential.

From internal or confidential material, never carry over partners, funding, pricing, quotes, customers, contacts, contractors, grant amounts, contract terms or internal programme names, and never quote it, even as an example. If a public version would be valuable, ask for one in the private [packet](#8-glossary) ([PROCESS.md 6.1, The packet](PROCESS.md#61-the-packet)), never in the document.

### 5.3 Naming

- **AI generically.** Write "frontier AI models" or "AI agents". No AI company, product or sponsor is named, and the document never says who asked for the list.
- **People.** Name public contributors for their public work (a core's author, a tool's maintainer, a paper's authors), by the names they use publicly. Never name contacts, contractors, reviewers or staff from internal documents.
- **Projects.** Use current names, with the former name once where readers might know it ("[F4PGA](https://github.com/chipsalliance/f4pga), the open FPGA toolchain project, formerly SymbiFlow").
- **Credit.** Prior work is credited to the project or paper that did it, in the section where it is used.

### 5.4 Claim statuses

**A link, a status, or both.** Every claim links to its source, or carries exactly one of these statuses, or both where the status is `(as of YYYY-MM)` on a linked state-of-the-art claim. A bare `Unknown` or `estimate`, without its bracket, is not a status. Nothing else is allowed in a landed document.

| Status | Meaning | Survives landing |
| --- | --- | --- |
| `(as of YYYY-MM)` | A state-of-the-art claim, true when checked. Required on every tool status and "nobody has done X". | yes |
| `(estimate)` | The writer's order-of-magnitude figure, with what replaces it ("to be measured at [M0, Baseline and harness](#49-work-plan-and-milestones), once the [harness](#8-glossary) exists"). | yes |
| `None found (searched: <where>, <date>)` | A required element with nothing to report, after a named search. | yes |
| `Unknown (settled by: <what>)` | A fact nobody has, with the measurement, experiment or question that settles it. | yes |
| `Not applicable (<why>)` | A required element that does not apply to this item. | yes |
| `(from Tim's unpublished notes)` | An idea from an internal document of Tim's ([5.2, Material outside the allow-list](#52-material-outside-the-allow-list)), after his approval. | yes, once approved |
| `(Tim's claim, YYYY-MM; checked: <how> \| not checked)` | A statement from Tim's documents, answers or comments, with what was done to check it; `not checked` survives only in [4.7, What Tim has already worked out](#47-what-tim-has-already-worked-out) and in answers folded in from [4.13, Questions for Tim](#413-questions-for-tim). | yes |
| `(assumed; unanswered since YYYY-MM-DD)` | A Questions-for-Tim default applied after seven days without an answer ([4.13, Questions for Tim](#413-questions-for-tim)); in that section and wherever the body uses the assumption. | yes, until answered |
| `(unverified)` | A claim the writer could not check. | no: verified, rewritten as `Unknown (settled by: …)`, or deleted before landing |
| `(staging note; not re-checked)` | A fact taken from the project's working notes rather than a public source. | no: traced to a public source or deleted |
| `[S<n>]` | A claim id pointing into the [source pack](#8-glossary) ([PROCESS.md Step 1, Draft](PROCESS.md#step-1-draft)). | no: stripped at landing |

A negative claim ("no open [PDK](#8-glossary) has a complete per-rule suite") is a claim like any other: it carries `(as of YYYY-MM)` and names where the writer looked.

### 5.5 Status of tools and projects

**One status word per tool.** Each tool, project or repository carries one status word:

| Status | Meaning |
| --- | --- |
| active | A commit or release within the six months before the as-of month |
| quiet | The last commit or release more than six and at most twelve months before the as-of month |
| inactive | More than twelve months |
| archived | Marked read-only by its owners |
| moved | A successor is named, with the link |

The as-of month is stated on each entry, or once at the head of a list when it applies to every entry in it.

### 5.6 Licences

**Defaults per artefact.** The document states, under "What open means here", which licences the work will carry. Defaults, departed from with a reason: contributions to an existing project under that project's licence; new code under Apache-2.0 (this repository's licence) or ISC where the surrounding ecosystem uses it; data and documentation under CC0 or CC-BY-4.0 (the Creative Commons licences); a test suite is software and takes a software licence.

**Licence classes.** Every tool, dataset and result named in a document carries one of three classes:

| Class | Meaning | Examples |
| --- | --- | --- |
| [open-source](#8-glossary) | Anyone is allowed to study, change and redistribute it; for software, a licence on the Open Source Initiative's list | Apache-2.0, ISC, CERN-OHL-P-2.0 for software and hardware; CC0, CC-BY-4.0 for data and documentation |
| [source-available](#8-glossary) | The source can be read, but the licence limits who is allowed to use or change it or for what, or opens only after a delay; also "open core" where the useful part is closed, and models (AI or device) or data released without what produced them | The Business Source License and its relatives |
| [proprietary](#8-glossary) | Closed | Vendor tools and their outputs under an end-user licence agreement (EULA) |

CC0 and CC-BY-4.0 are not on the Open Source Initiative's list ([opensource.org/licenses](https://opensource.org/licenses), as of 2026-10) and count as open here for data and documentation only; CERN-OHL counts in its 2.0 variants (P, S and W). Only open-source counts as open in the sense of [4.5, Why it must be open](#45-why-it-must-be-open). A source-available licence is named as such wherever the document meets it. Nothing the item delivers needs a source-available or proprietary component to be built or run; a proprietary tool is allowed to serve as an [oracle](#8-glossary) or a reference during the work, named as such ([4.9, Work plan and milestones](#49-work-plan-and-milestones), the Reference lines).

### 5.7 Clean-room rule for PDK items

**Public sources only.** Design-rule values and reasons, device parameters and manufacturing-process descriptions in open rule decks and open PDKs come only from public sources, each cited. Nobody writes them from memory of material under NDA. A person who has signed a foundry NDA covering a related manufacturing process reviews open work for plausibility only and contributes no values. A proxy PDK is derived from public papers, public PDKs and measurement, and its document says which. Foundry rule decks under NDA are never read in, copied, used as a reference, or named as the source of a reason.

### 5.8 Upstream contributions

**A person owns every upstream contribution.** An agent working an item never opens an issue or pull request in another project, posts on its lists or chats, or submits to a standards body; a person named in `DECISIONS.md` as the owner of that contribution opens it. The rules per project:
- Each workstream's `Lands in` line names the project and links its contribution rules, and the Contribution gate line names what the maintainers require.
- Where a project forbids AI-authored commits or AI co-author lines ([VTR](https://github.com/verilog-to-routing/vtr-verilog-to-routing), the open-source FPGA architecture and place-and-route flow, does in its [contribution rules](https://github.com/verilog-to-routing/vtr-verilog-to-routing/blob/master/CONTRIBUTING.md), as of 2026-10), the work stays in this project's repositories until a person authors the contribution.
- Where a project requires a Developer Certificate of Origin line on each commit (`git commit -s`; [OpenROAD](https://github.com/The-OpenROAD-Project/OpenROAD), the open-source digital place-and-route flow, does in its [contribution rules](https://github.com/The-OpenROAD-Project/OpenROAD/blob/master/CONTRIBUTING.md), as of 2026-10), only a person gives it.
- Where a project asks that quality-of-results claims be shown on more than one design (OpenROAD's [contribution rules](https://github.com/The-OpenROAD-Project/OpenROAD/blob/master/CONTRIBUTING.md) do, as of 2026-10), the evidence is prepared that way before anything is proposed.

### 5.9 Vendor terms

**The question, not the conclusion.** State the legal question (does this EULA permit reverse engineering, redistribution, benchmarking, automated runs at scale) and the fact of what others have done in public; do not give a legal conclusion.

### 5.10 Citations and links

**Resolved before cited.** A paper is cited only after a search tool returns it; the title, year and DOI (digital object identifier) or arXiv identifier (or the id in [OpenAlex](https://openalex.org/), the open index of scholarly works, where it has neither) are copied from the result. The resolution protocol:

1. Query the exact title.
2. On no result, try a second index.
3. A match is uncertain until the first author, the year and the venue agree.
4. A different title or year is a different work.
5. Cite the version of record where one exists, then the arXiv version.
6. Cite a dataset's DOI separately from its paper.
7. Record any correction, addendum, retraction or published critique.

| Object | Cited or linked only after |
| --- | --- |
| A paper | The protocol above |
| A repository | It is fetched and its status read |
| A design doc of Tim's | It is listed in a resources file ([5.1, Link allow-list](#51-link-allow-list)) |
| Any link | It was fetched on the audit date, and again at landing when a day or more has passed |

A broken link is removed or replaced, never left; "unreachable from this sandbox" is a status to record, never a pass. Invented or unverifiable references are a blocker in review.

### 5.11 Provenance in the text

**Whose claim it is.** The reader must be able to tell what is Tim's prior work, what is the state of the art elsewhere, and what is the writer's synthesis or estimate: "Tim's [doc](link) proposes", "as of 2026-10, [KLayout](https://github.com/KLayout/klayout), the open-source layout editor and design-rule checker, …", "(estimate)". An `(unverified)` claim has three fates before landing ([5.4, Claim statuses](#54-claim-statuses)): verified and linked; rewritten as `Unknown (settled by: …)`, with the question listed under Unanswered technical questions or, where only Tim can settle it, under Questions for Tim; or deleted.

## 6. Style and mechanics

### 6.1 Voice

**Direct and factual.** The rules of voice, with the advice marked:

- Plain English and short sentences (the limits are in [6.7, Readability and presentation](#67-readability-and-presentation); the rest of this list is advice); British spelling (characterise, artefact, licence), which the existing item documents mix and are brought to as they are rewritten.
- The voice of the existing documents: direct, factual, no hype, no first person. Tim is referred to by name, in the third person.
- Numbers with units and sources. "About" for rounded figures.
- Links inline with descriptive text, never bare URLs in prose.
- No marketing adjectives. If a sentence would survive in any other item's document unchanged, it is too general.
- Closed-source tools, data, rule decks and manufacturing processes are *[proprietary](#8-glossary)*, never *commercial*: [open-source](#8-glossary) software is sold too, so "commercial" says nothing about openness; *vendor* names the company that sells them.
- The form of each element (prose, list, table, block or diagram) follows [6.7, Readability and presentation](#67-readability-and-presentation); the choice of words, the definition of terms and the form of pointers follow [6.8, Words: pointers, terms and second readings](#68-words-pointers-terms-and-second-readings).

### 6.2 Length

**One band.** The whole document is 3,000 to 6,000 words; the [lint](#8-glossary) warns outside the band and fails above 7,000. The count is `wc -w` over the hand-written part (from the line after the title to the line before the generated "Where it sits"), after removing the URL part of every link and the separator rows of tables. Lists and table cells count. The summary (60 to 120 words) and "Questions for Tim" (at most 300 words) are the only per-section limits.

### 6.3 Headings and lead-ins

**The template's headings and lead-ins, exactly.** Headings are exactly the ones in the template, in the template's order, as `##`; sub-headings as `###`, also in the template's order. Questions for Tim is the one `##` section that is absent when empty ([4.13, Questions for Tim](#413-questions-for-tim)); every other heading is present. The bold [lead-ins](#8-glossary) named in [section 4, Section requirements](#4-section-requirements) are present with the exact words shown. The lint checks the heading set, the order and the lead-ins.

### 6.4 Title and the generated tail

**The title is kept; the tail is generated.** The rules for the title line, the generated sections and the change log:
- The title line is `# <item id>: <item title>` and is line 1; nothing sits above it, and no heading ends in whitespace.
- For an existing item the title is the current file's first line, unchanged; for a new item it is the [`items.json`](items.json) title after the id prefix.
- [`tools/build.py`](tools/build.py) keeps the file's own title and only re-adds the id prefix, so the title is hand-written and stays as it is in the current file; a title change is made together with the [`items.json`](items.json) title through the [routed change](#8-glossary) ([PROCESS.md 12, What agents are allowed to do on their own](PROCESS.md#12-what-agents-are-allowed-to-do-on-their-own)).
- The document ends with "Start here"; the three generated sections are not written, not even as empty headings, because `build.py` strips and re-appends them and an empty trailing heading survives as a duplicate.
- A change log never goes in an item document; it lives in the [working folder](#8-glossary) as `draft-<n>.changes.md`. The status line of [4.1, Summary and status line](#41-summary-and-status-line) records the draft number and the reviews and is not a change log. The guideline files are the exception: each carries a revision history at its end.

### 6.5 Guidance lines and placeholders

**Guidance lines and placeholders are removed.** Every guidance line in the template starts with `> *` and ends with `*`. Documents never use that form for anything else, so the lint can reject any line matching `^>\s*\*`. Placeholders (`YYYY-MM-DD`, `<id>`, `<Title>`, `<name>`, `…`, `TODO`) are rejected the same way.

### 6.6 Markers that do not survive

**Working-draft markers are removed.** `(unverified)`, `(staging note; not re-checked)`, `(thin: needs research)` and `[S<n>]` claim ids are working-draft markers. The lint fails a [landing](#8-glossary) that contains any of them ([section 5.4, Claim statuses](#54-claim-statuses)).

### 6.7 Readability and presentation

The documents are dense by design: each distils years of work into a few thousand words. Density only pays if a reader can get at it quickly, so:
- a person must be able to skim a document and come away with most of its value and the gist without reading every part;
- every means the medium offers (headings, lead-ins, lists, tables, labelled blocks, diagrams, captions, ids, links, the glossary, the digest) is used to make understanding fast;
- the principles below say what that requires, and the checkable form of each is its box in [section 7, Definition of done](#7-definition-of-done);
- the familiar failures (a paragraph that belongs in a list; a list that belongs in a table; a table cell stuffed with text that belongs in columns; a description that belongs in a diagram; a diagram made unclear by overlap, colour, sizing, missing units or the wrong amount of detail) are instances of these principles, not the whole test;
- the readability and clarity reviewer ([brief A.14, Readability and clarity reviewer](PROCESS.md#appendix-a-reviewer-briefs)) checks every document against the principles, and the mechanical cases will be caught by the proposed lint checks [L20, form limits](PROCESS.md#appendix-b-the-lint-toolscheckpy) to [L23, diagram ids](PROCESS.md#appendix-b-the-lint-toolscheckpy) ([PROCESS.md Appendix B, The lint, `tools/check.py`](PROCESS.md#appendix-b-the-lint-toolscheckpy)) once they land.

**Three depths of reading, each complete.** A reader stops at one of three depths, and each depth must stand on its own.

| Depth | What is read | What the reader comes away with |
| --- | --- | --- |
| One minute | The title and the summary | What the item produces, for whom, what is broken, why agents change it |
| Five minutes | The [skim path](#8-glossary) | The gist: why the item matters and what it unlocks; how the work is cut up and checked; what it needs beyond [AI processes](#8-glossary); the biggest risk; where to start |
| The full read | Everything | The evidence: sources, numbers, open questions |

**The skim path.** The six things a five-minute reader reads, in order:

- the title and the summary;
- every heading;
- every bold lead-in with the first sentence after it;
- every table;
- every diagram with its caption;
- the [agent digest](#8-glossary).

**The gist.** The five things a five-minute reader comes away with:

- why the item matters and what it unlocks;
- how the work is cut up and how each part is checked;
- what it needs beyond AI processes;
- the biggest risk;
- where to start.

The skim path is a defined thing: the proposed `--skim` option of [`tools/check.py`](tools/check.py) will print it ([PROCESS.md Appendix B, The lint, `tools/check.py`](PROCESS.md#appendix-b-the-lint-toolscheckpy)); until it lands, the writer assembles it by hand from the list above. The writer reads it before the [panel](#8-glossary); the reviewer reads it first, alone, and reports what it got wrong (the skim test, [brief A.14](PROCESS.md#appendix-a-reviewer-briefs)). Everything not on the skim path is evidence and detail for the reader who wants it.

**The first sentence is the conclusion.** After each bold lead-in, the first sentence states what the element concludes: the number, the decision, the name, the answer. What follows supports it. A conclusion at the end of a paragraph is invisible to a skimmer; a paragraph that opens with background has buried its point.

**Form follows the shape of the content.** Each kind of content has a form that shows its shape. Prose is the form a writer falls into and the hardest to skim, so the form of each element is chosen on purpose:

| The content is | Its form is | The form to avoid |
| --- | --- | --- |
| An argument, a reason or a judgement | Prose: short paragraphs, one idea each | A list of fragments that hides the reasoning |
| Three or more parallel things | A list, one per line | A paragraph that strings them together with "and" and semicolons |
| Several things that each carry the same attributes | A table: one row per thing, one column per attribute, the unit in the header | A list whose entries repeat the same labels; a table cell that holds a paragraph |
| One thing with many attributes | A labelled block, in the template's form where it gives one (the workstream and milestone blocks) | A one-row table; a table cell holding several facts |
| Structure: a flow of steps, a dependency, a hierarchy, a ladder, a tiling, a timeline, a layout | A diagram with a caption that says what it shows | Prose the reader has to draw for themselves |
| Numbers to compare | A table with the unit in the header; a chart when the trend is the point | Numbers scattered through sentences |
| A fact used in several places | One home, pointed to from elsewhere ([principle 19, One home per fact](#2-principles)) | The fact restated, drifting between copies |

**One unit of form carries one unit of content.** A unit that holds more has no boundaries a skimmer can see, which is what is wrong with the stuffed table cell. The proposed lint check [L20](PROCESS.md#appendix-b-the-lint-toolscheckpy) warns past each limit; a warning is a finding the merger accepts or rejects ([PROCESS.md Step 3, Merge](PROCESS.md#step-3-merge)).

| Unit of form | Carries | Limit (the lint warns past it) |
| --- | --- | --- |
| Sentence | One idea | 60 words |
| Paragraph | One point and its support | 120 words, six sentences |
| List item | One thing | 60 words |
| Table cell | One value or one short phrase | 25 words |
| Diagram node; edge | One thing; one relation | 15 nodes per diagram, split or layered beyond that |
| Diagram | One question answered | One per caption |

**Everything that carries information is labelled.** Every number has its unit and its source or status. Every table has a header row, with the unit in the column header rather than repeated in the cells. Every diagram has a caption that says what it shows and what its shapes and arrows mean; every axis has its unit; every node and edge has a label; every colour has a stated meaning or no role. A reader who lands on a table or a figure knows what they are looking at without the prose around it.

**Detail is matched to the reader's question.** Each table and diagram answers one question at the level of detail that question needs. Every box of a forty-step flowchart answers nothing at a glance; three boxes labelled input, step and output say nothing at all. The level is set by what the reader will do with the answer: decide, start or check. What does not fit goes to a second figure or a table; what is not worth a reader's glance is left out.

**The same thing looks the same everywhere.** One name per concept, within a document and across the list (the glossary's names); the same column order in every table of a kind; the ids [W1](#49-work-plan-and-milestones), [M2, Usable](#49-work-plan-and-milestones) and [P3, agrees with an independent reference](#491-proof-levels) written as they are in the blocks; the same shape and colour for the same kind of thing in every diagram; the fixed lead-ins. Consistency lets a reader reuse in the next section what they learned in the last.

**A visual property means something or is uniform.** Size, colour, position, line weight and emphasis each encode one stated variable or are the same for every element of a kind. Overlapping text, colour as decoration, boxes sized by how much text happened to fit, whole sentences in bold: each makes the form say something the writer did not mean. Colour is never the only channel for a meaning, because of printed pages, colour-blind readers and the dark theme of the [living doc](#8-glossary).

**Render and look.** Source that reads well can render badly. Every diagram is rendered as the reader will see it, on the repository page and in the living doc, and looked at: overlaps, clipped or unreadable labels, arrows through boxes, type too small to read. The rendering (with the proposed render script of [PROCESS.md Appendix C, Changes needed elsewhere](PROCESS.md#appendix-c-changes-needed-elsewhere), or in a browser by hand until it lands) and the looking are part of the reviewer's brief ([brief A.14, Readability and clarity reviewer](PROCESS.md#appendix-a-reviewer-briefs)).

**Navigation is the price of density.** Readers arrive through a link to a heading as often as from the top. They find their way by the fixed structure ([section 3, Structure of an item document](#3-structure-of-an-item-document)), the summary at the top, the digest at the end, the lead-ins, the ids, and pointers that name what they point to ([6.8, Words: pointers, terms and second readings](#68-words-pointers-terms-and-second-readings)). "One home per fact" ([principle 19, One home per fact](#2-principles)) is a navigation rule as much as a correctness rule: a fact with one home can be found and corrected; a restated fact drifts.

**Diagrams in practice.** One source, two renderings.

| Where | Form |
| --- | --- |
| The repository file | A [Mermaid](#8-glossary) block (the text-to-diagram language the repository host renders), followed by one italic caption line: `*Figure <n>: <what it shows>; <what the shapes and arrows mean>; <the finding the reader should take away>.*` |
| The living doc | The doc's own diagram block with the same caption, drawn from the Mermaid |

The [Mermaid](#8-glossary) in the file is the source of truth; a change made on the doc's side is carried back to it by hand ([SYNC.md](SYNC.md)). The living doc's own rules for drawings apply there:

- the title states the finding;
- the same fill for the same kind of box;
- type no smaller than the body text;
- connectors never across a box.

Due in every document: the Dependencies diagram of [4.9, Work plan and milestones](#49-work-plan-and-milestones). Due where the form table above calls for one: a tool pipeline, a [verification ladder](#8-glossary), how the item's neighbours connect. A diagram shows only what the document states: no invented numbers, steps or parts.

### 6.8 Words: pointers, terms and second readings

Readers land in the middle and have not read the first part, and they will read a sentence in every way except the intended one wherever there is room. So references carry full details, jargon is reduced, no term is made up, and words are chosen against their everyday meanings.

**Every pointer is self-contained.** A reader who arrives at a heading from a link has read nothing before it. A pointer therefore names what it points to in full, in the sentence where it is used:

| Pointing to | Write | Never |
| --- | --- | --- |
| A paper | The authors and year with what it established: "Smith and Lee (2023), who measured X on Y (Key papers)" | "the paper above"; "[3]"; "Smith et al." alone |
| A tool or project | Its name and what it is, at its first use in each `##` section: "[KLayout](https://github.com/KLayout/klayout), the open-source layout editor and design-rule checker" | A bare name the reader might not know |
| A workstream or milestone | Its id and its name: "[W2](#49-work-plan-and-milestones), the [harness](#8-glossary) workstream"; "[M1](#49-work-plan-and-milestones), the first checkable result" | "[W2](#49-work-plan-and-milestones)" alone, outside the blocks and the summary table |
| Another item on the list | Its id and what it is: "[drc-forge](projects/drc-forge.md), the open design-rule-check engine" | The id alone |
| A section of this file or of the document | Its number and its name: "[section 4.9, Work plan and milestones](#49-work-plan-and-milestones)" | A number alone |
| A number | The number with its unit, its baseline and its source or status | "50% faster"; "1,500" |

The reference entry (authors, year, identifier, licence, contents) lives in one place ([hard rule 12, One entry, full names, links](#0-the-fifteen-hard-rules)); every other mention is a full name, linked to the same target ([6.9, Links](#69-links)), plus where the details are.

**Terms of the field are reduced, then defined where they stay.** Where a plain phrase loses nothing, it replaces the term. A term that stays is defined in a few words at its first use in each `##` section, or linked to the glossary ([section 8, Glossary](#8-glossary)). An acronym is written out at its first use in each `##` section; after that, [DRC](#8-glossary), [PDK](#8-glossary), [FPGA](#8-glossary) and the other acronyms more common than their phrase are used as acronyms, and the rest are written out every time. An acronym with a second expansion in the field or in daily use (the table below) is written out every time, except IP, which is used after "IP block" at its first use in the section.

**No invented terms.** A document uses the field's own name for a thing. Where the field has none, the document describes the thing in plain words rather than coining a name. The only coined terms the documents use are the ones this file defines in the glossary ([section 8, Glossary](#8-glossary)), with exactly those meanings; a document introduces no term, label, nickname or acronym of its own, and names nothing after the project or a person.

**A word with a second meaning is replaced or pinned.** Many words mean one thing in this field and another in daily use or in a neighbouring field. Where a reader could take the other meaning, the document uses the specific word, or pins the meaning at its first use in the section. The table lists the collisions met most often; a proposed lint check warns on each occurrence ([L21, collision words](PROCESS.md#appendix-b-the-lint-toolscheckpy) and [L22, acronyms](PROCESS.md#appendix-b-the-lint-toolscheckpy), proposed) and the reviewer judges whether the context pins it. The template's fixed headings, lead-ins and block labels are exempt: they are the documents' own vocabulary, set by this file, and the proposed check skips them.

| Word | Meaning | Write instead |
| --- | --- | --- |
| open | open source | open-source |
| open | open to anyone | publicly available |
| open | an open circuit | open-circuit |
| open | an unanswered question | unanswered |
| open | reproducible, replicable and changeable by anyone (this file's sense) | open, defined at its first use in the section |
| open-source | a licence the Open Source Initiative approves | open-source |
| open-source | code that can merely be read | [source-available](#8-glossary), or public |
| free | no cost | no-cost |
| free | free to study, change and share | open-source |
| commercial | closed source | proprietary |
| commercial | sold or paid for | paid, sold |
| model | an AI model | AI model |
| model | a transistor or device model | device model, SPICE (circuit-simulator) model |
| model | a simulation model | simulation model |
| model | a mental model | the plain phrase |
| cell | a standard cell | standard cell |
| cell | a memory bit cell | bit cell |
| cell | a table cell | table cell |
| process | a manufacturing process | the named process, or process node |
| process | a procedure | procedure |
| process | a running program | program |
| node | a process node | process node |
| node | a graph node | graph node |
| node | a circuit node | net |
| node | a machine | machine |
| corner | a process-voltage-temperature corner | process corner |
| corner | a geometric corner | corner of the die |
| yield | the share of working dies | manufacturing yield |
| yield | to give | gives |
| rule | a design rule | design rule |
| rule | a lint rule | check |
| rule | a rule of thumb | rule of thumb |
| rule | a rule of these guidelines | hard rule N, or the section named |
| deck | a [rule deck](#8-glossary) | rule deck |
| deck | a slide deck | slides |
| flow | a tool flow | tool flow |
| flow | a flow of data or control | data flow, control flow |
| regression | a regression test | regression test |
| regression | a slowdown | slowdown |
| regression | a statistical fit | fit to the data |
| significant | statistically significant | the test and its result |
| significant | important | important |
| device | a transistor | transistor |
| device | a chip | chip |
| device | a board | board |
| library | a cell library | cell library |
| library | a software library | software library |
| slack | timing slack | timing slack |
| slack | spare time | spare time |
| closure | timing closure | timing closure |
| closure | a settled question | settled |
| sign-off | the signoff checks | signoff checks |
| sign-off | approval | approval |
| design | the activity | designing |
| design | the artefact | the design (the chip, the block) |
| [oracle](#8-glossary) | the check that decides a result (this file's term) | oracle, defined at its first use in the section |
| oracle | the company | never |
| fit | the A to D suitability (this file's term) | Fit: A, defined at its first use in the section |
| fit | a curve fit | curve fit |
| fit | fitting within | fits within |
| harness | the test harness (this file's term) | harness, defined at its first use in the section |
| AI processes | AI agents and their model calls (this file's term) | AI processes, defined at its first use in the section |
| landing | merging to main and mirroring the living doc (this file's term) | landing, defined at its first use in the section |
| landing | arriving at a page or section | arriving |
| tier | a size class of AI model (this file's term) | model tier |
| tier | any other ranking | class, level, rank |
| [shuttle](#8-glossary) | a multi-project wafer run | shuttle run, with "multi-project wafer" at its first use |
| may | permission | allowed to |
| may | possibility | might |
| can | ability | can |
| can | permission | allowed to |
| should | a rule | must |
| should | advice | is better, with the reason |
| must | a requirement | must (only for requirements) |
| only, all, not | depends on placement | next to the word it limits |
| up to | a maximum | at most |
| up to | a range | the range, with both ends |
| faster, better, N times | relative to what | the baseline, the unit and the number |
| recently, currently, now | when | a date, or `(as of YYYY-MM)` |
| it, this, which | which referent | the noun again |
| PR | pull request | pull request |
| PR | place and route | place and route |
| IP | IP blocks | IP block at its first use in the section, then IP |
| IP | internet protocol | internet protocol |
| DFT | design for test | design for test |
| DFT | discrete Fourier transform | discrete Fourier transform |
| PV | physical verification | physical verification |
| PV | photovoltaic | photovoltaic |
| FF | flip-flop | flip-flop |
| FF | the fast-fast corner | fast-fast corner |
| FF | fill factor | fill factor |
| CI | continuous integration | continuous integration |
| CI | confidence interval | confidence interval |
| DSP | digital signal processing | digital signal processing |
| DSP | a DSP block | DSP block, defined |

**Assume the hostile reading.** For every sentence that states a number, a capability, a requirement or a prohibition, the writer asks what else it could mean and rewrites until it has one reading. The usual rooms for a second reading:

- a pronoun with two possible referents;
- "only", "all" or "not" placed loosely;
- a comparison without its baseline;
- a percentage without its base;
- a range that does not say whether its ends are included;
- a list that does not say whether its items are alternatives or all required;
- a negative that reads as a positive;
- a unit left to be assumed (seconds or milliseconds; per design rule or per rule deck);
- a precision not stated ("1,500" against "about 1,500");
- an acronym with two expansions.

The reviewer's test is to read each such sentence as an opponent would and quote the second reading ([brief A.14](PROCESS.md#appendix-a-reviewer-briefs)).

### 6.9 Links

Links are cheap; a reader's search is not. A document links everything a reader might want to go to, at the place where they would want to go:

| What | Link target | How often |
| --- | --- | --- |
| A section of this file or of the document ("[4.10, Needs beyond AI processes](#410-needs-beyond-ai-processes)") | The heading's anchor | Every mention |
| An id: a workstream ([W2](#49-work-plan-and-milestones)), a milestone ([M1](#49-work-plan-and-milestones)), a [proof level](#8-glossary) ([P3](#491-proof-levels)), a lint check ([L20](PROCESS.md#appendix-b-the-lint-toolscheckpy)), a brief ([A.14](PROCESS.md#appendix-a-reviewer-briefs)) | The sub-heading or section that defines it | Every mention outside the block that defines it; the first mention in a section also carries its name ("[M1](#49-work-plan-and-milestones), the first checkable result") |
| Another item ([`drc-forge`](projects/drc-forge.md)) | `<id>.md` from an item document (the documents share the `projects/` folder); `projects/<id>.md` from a file at the repository root | The first mention in each `##` section, with what the item is |
| A tool or project | Its home page or repository, the same target as its reference entry under Projects and code | The first mention in each `##` section |
| A paper | Its identifier's resolver page (the DOI, digital object identifier, or arXiv link), the same target as its reference entry under Key papers | The first mention in each `##` section |
| A term of the field | The [glossary](#8-glossary), or the sentence that defines it | The first mention in each `##` section, unless defined there |
| A file ([`items.json`](items.json), [`tools/build.py`](tools/build.py), [SYNC.md](SYNC.md)) | The file | Every mention |

Link text is the name of the thing, never "here" or "this". An internal link points at a heading that exists: a proposed lint check fails on one that does not ([L24, internal links](PROCESS.md#appendix-b-the-lint-toolscheckpy), proposed) and warns on a section number or id left unlinked ([L25, unlinked ids](PROCESS.md#appendix-b-the-lint-toolscheckpy), proposed); until they land, the claim audit checks both ([PROCESS.md Step 5, Revise and audit](PROCESS.md#step-5-revise-and-audit)). Heading anchors are the repository host's: the heading in lower case, punctuation removed, spaces as hyphens, so `### 4.10 Needs beyond AI processes` is `#410-needs-beyond-ai-processes`. How these links carry into the living doc is in [SYNC.md](SYNC.md).

## 7. Definition of done

Copied into the [working folder](#8-glossary) for each iteration and ticked before [landing](#8-glossary), one box per check. The exit condition for the loop is in [PROCESS.md 4, Exit condition](PROCESS.md#4-exit-condition).

**Structure.** The skeleton is complete and clean.
- [ ] All hand-written sections present, in order ([section 3, Structure of an item document](#3-structure-of-an-item-document); [6.3, Headings and lead-ins](#63-headings-and-lead-ins)).
- [ ] Every [guidance line](#8-glossary) and placeholder removed ([6.5, Guidance lines and placeholders](#65-guidance-lines-and-placeholders)).
- [ ] No generated heading in the file ([6.4, Title and the generated tail](#64-title-and-the-generated-tail)).
- [ ] Summary of 60 to 120 words ([4.1, Summary and status line](#41-summary-and-status-line)).
- [ ] Status line in the [4.1, Summary and status line](#41-summary-and-status-line) grammar; its question count matches the Questions for Tim section.

**Goal and value.** The end state and the case for it are in their required elements.
- [ ] Goal has Deliverables, Acceptance test, Framing and Out of scope ([4.2, Goal](#42-goal)).
- [ ] Why it is high value has The pain today, Why not already done, Who is waiting, Why now (naming which of the three framings applies and what changed) and [Shots on goal](#8-glossary) ([4.3, Why it is high value](#43-why-it-is-high-value)).
- [ ] What success unlocks names only items in `related` for this item under Needs first, Unlocks on this list and Cross-checks with; Shared [harness](#8-glossary) is present ([4.4, What success unlocks](#44-what-success-unlocks)).

**Open.** The openness argument is made for this item ([4.5, Why it must be open](#45-why-it-must-be-open)).
- [ ] The closed version, The counterfactual and The strongest case against open are present.
- [ ] Why closed does not deliver has at least two labelled mechanisms.
- [ ] What open means here states the licence per artefact, what must be published to reproduce and to replicate, and names the look-alike licences.

**State of the art.** The survey is dated, classed and sourced ([4.6, State of the art](#46-state-of-the-art)).
- [ ] The five sub-headings are present.
- [ ] Every status carries the [5.5, Status of tools and projects](#55-status-of-tools-and-projects) vocabulary and an as-of month.
- [ ] Every tool entry states its [licence class](#8-glossary), speed and quality.
- [ ] The bar to clear has its three parts.
- [ ] The efforts table has a link per row.
- [ ] What is missing ends with Replace or build on.

**Tim's record.** What Tim worked out is read, attributed and checked ([4.7, What Tim has already worked out](#47-what-tim-has-already-worked-out)).
- [ ] Lists only documents read, marks what was read, marks unpublished ideas.
- [ ] Each claim of Tim's carries the `(Tim's claim, YYYY-MM; checked: …)` status with what was done to check it, or `not checked` where [5.4, Claim statuses](#54-claim-statuses) allows it.
- [ ] Ends with Where the written record runs out.

**Frontier models.** The AI case is argued from counted numbers ([4.8, What frontier models change](#48-what-frontier-models-change)).
- [ ] Why faster, Why better, What has to be true and What people still do are present, argued from counted or sourced numbers, with no estimated rate or duration; no table.

**Work plan.** The plan is checkable: blocks, milestones, metric, cross-checks ([4.9, Work plan and milestones](#49-work-plan-and-milestones)).
- [ ] Three to eight workstream blocks, each with every line.
- [ ] The summary table matches the blocks.
- [ ] [M0, Baseline and harness](#49-work-plan-and-milestones) to [M3, Complete or at the bar](#49-work-plan-and-milestones) ([M4, Proven in hardware or silicon](#49-work-plan-and-milestones) or Not applicable) each have Done when, Evidence, Proof, Needs, Completes, Fit and Gate.
- [ ] [M1, First checkable result](#49-work-plan-and-milestones) needs nothing beyond public resources, no-cost vendor editions and at most one board sold to the public at a listed price.
- [ ] Harness, benchmarks and tool speed is a workstream or is declined with a reason.
- [ ] Dependencies is present and matches the blocks.
- [ ] Metric and baseline has a formula, a guardrail and a pinned baseline or `Unknown (settled by: M0)`.
- [ ] Lead times is present, with a source per wait.
- [ ] Cross-checks has Sources and failure modes, [Verification ladder](#8-glossary), Fast and accurate paths and Effort rule.
- [ ] Every decision number (Acceptance test, Done when, Metric and baseline, Shots on goal) has two independent sources or a computed bound ([principle 2, No single source is trusted, and no single person](#21-checking)).

**Needs, unknowns, questions.** The asks, the blockers and the open questions each carry their check.
- [ ] Needs beyond AI processes has the seven-column table, Licence questions and [Clean room](#8-glossary) (Not applicable for items that do not touch a [PDK](#8-glossary)) ([4.10, Needs beyond AI processes](#410-needs-beyond-ai-processes)).
- [ ] Unknowns, blockers and risks has its three lists, the [plausible-but-wrong risk](#8-glossary) first, each risk with its check, each blocker with its question ([4.11, Unknowns, blockers and risks](#411-unknowns-blockers-and-risks)).
- [ ] Unanswered technical questions each have a way to settle them and a taker ([4.12, Unanswered technical questions](#412-unanswered-technical-questions)).
- [ ] Questions for Tim: at most five, at most 300 words, each in the [4.13, Questions for Tim](#413-questions-for-tim) form, or the section is absent.

**Start here.** An agent can begin from the brief ([4.14, Start here](#414-start-here)).
- [ ] The seven-line [agent digest](#8-glossary) and the seven sub-headings after it.
- [ ] Reproduce first is pinned, with a known-good and a known-bad case.
- [ ] Every paper resolved, with one reference entry under Key papers; every repository fetched, with status and licence, with one reference entry under Projects and code; every other mention links to the same target ([6.9, Links](#69-links)).
- [ ] Every first task fit A in the [4.14, Start here](#414-start-here) form.

**Sources and safety.** Nothing is linked, named or carried that the rules forbid.
- [ ] No Drive link outside the allow-list; no held-back or flagged document ([5.1, Link allow-list](#51-link-allow-list)).
- [ ] No AI company or sponsor named; no prices, contacts, partners or figures from private material ([5.2, Material outside the allow-list](#52-material-outside-the-allow-list); [5.3, Naming](#53-naming)).
- [ ] No [working-draft markers](#8-glossary) ([6.6, Markers that do not survive](#66-markers-that-do-not-survive)).

**Readability and words.** A skimmer gets the gist and a stranger resolves every pointer.
- [ ] Word count within 3,000 to 6,000, counted as [6.2, Length](#62-length) says (the hand-written part, link addresses and table separator rows removed).
- [ ] Skim test passed ([6.7, Readability and presentation](#67-readability-and-presentation)): the [skim path](#8-glossary) read alone gives what the item produces, why it matters and what it unlocks, how the work is cut up and checked, what it needs, the biggest risk and the first task.
- [ ] After every [lead-in](#8-glossary) the first sentence is the conclusion ([6.7, Readability and presentation](#67-readability-and-presentation)).
- [ ] No paragraph that strings three or more parallel things together; no list whose items repeat the same labels; no table cell over 25 words; no flow of steps, dependency or hierarchy described in prose ([6.7, Readability and presentation](#67-readability-and-presentation)).
- [ ] No sentence that would survive unchanged in another item's document ([6.1, Voice](#61-voice)).
- [ ] Every diagram rendered and looked at on the repository page and in the [living doc](#8-glossary) ([6.7, Readability and presentation](#67-readability-and-presentation)).
- [ ] Every pointer names what it points to; every term of the field defined at its first use in its section or linked to the glossary; no coined term outside the glossary ([6.8, Words: pointers, terms and second readings](#68-words-pointers-terms-and-second-readings)).
- [ ] No word from the [6.8, Words: pointers, terms and second readings](#68-words-pointers-terms-and-second-readings) table in an ambiguous sense; every sentence stating a number, a capability, a requirement or a prohibition has one reading.
- [ ] Links ([6.9, Links](#69-links)): every section reference, id, item, tool, paper, term and file linked; every internal link resolves to a heading.

**Landing.** The mechanics of landing ran ([6.4, Title and the generated tail](#64-title-and-the-generated-tail); [PROCESS.md Step 6, Land and ask](PROCESS.md#step-6-land-and-ask)).
- [ ] [`tools/build.py`](tools/build.py) run from the repository root (it rewrites every item file, [README.md](README.md) and [docs.json](docs.json) from [items.json](items.json)); the living doc mirrored per [SYNC.md](SYNC.md).

## 8. Glossary

Short definitions of the terms the documents use. A document defines each at its first use in every section where it appears, or links here ([6.8, Words: pointers, terms and second readings](#68-words-pointers-terms-and-second-readings)); these are the only coined terms the documents are allowed to use.

- **Two-ways framing**: the README's two ways of reading the list: by what a chip does (interface, computation, storage) and by what you need to build one (PDK, tooling, IP blocks, then proof in silicon).
- **Manual-to-generator axis**: the shift, running through every item, from artefacts made by hand to artefacts that are generated, audited and re-run on every change.
- **Stepping stones**: Tim's view that each open layer makes the next one possible: open PDKs make open tools possible, open tools make open IP blocks possible.
- **PDK**: process design kit, the files a foundry gives designers (design rules, device models, standard cells) for one manufacturing process.
- **Fake or proxy PDK**: an open PDK for a process node with no real open kit, realistic enough to design against.
- **DRC, LVS, PEX, STA**: design rule check, layout-versus-schematic, parasitic extraction, static timing analysis: the signoff checks.
- **Rule deck**: the executable form of a PDK's design rules for one checker.
- **Reticle**: the largest area one exposure can print, about 26 x 33 mm; the upper bound on die size.
- **MPW, shuttle**: a multi-project wafer run shared by many designs; the cheap way to get silicon.
- **TCAD**: technology CAD: simulation of the manufacturing-process steps and the resulting devices.
- **Liberty, LEF, DEF, GDS, OASIS, SPEF, SDC**: the standard file formats for timing, abstracts, placement, layout, parasitics and constraints.
- **Bitstream, FASM**: the configuration data of an FPGA, and the FPGA assembly text format that names each feature it sets.
- **FPGA Interchange**: an open format for FPGA device resources and netlists so tools and device databases can be mixed.
- **eFPGA**: an FPGA fabric embedded as a block inside an ASIC (application-specific integrated circuit).
- **PPA, QoR**: power, performance and area; quality of results, the figures a tool flow is judged by.
- **Verification ladder**: the rungs a key result climbs, from a back-of-the-envelope bound through a fundamental limit, an independent source and a first-principles rebuild to a measurement ([4.9, Work plan and milestones](#49-work-plan-and-milestones), Cross-checks).
- **Shots on goal**: the number of attempts an item makes possible per unit time; many more attempts at a lower success rate can mean many more results ([2.1, Checking](#21-checking)).
- **Oracle**: an automated check that says whether a result is right, with known blind spots.
- **Negative control**: a case the oracle must reject, run to show the oracle can fail.
- **Proof level**: [P0, stated](#491-proof-levels) to [P5, proven in hardware or silicon](#491-proof-levels), the kind of evidence behind a milestone; kinds, not a scale ([section 4.9.1, Proof levels](#491-proof-levels)).
- **Proxy check**: a check such as a design-rule check or a SPICE run that stands in for a question about physics or manufacturing; every design rule in it has a reason, which decides when it is allowed to be relaxed ([principle 4, Every check is a proxy for physics, and every rule has a reason](#2-principles)).
- **Scoreboard**: the benchmark item that measures progress for others ([fpga-scoreboard](projects/fpga-scoreboard.md), [asic-scoreboard](projects/asic-scoreboard.md)).
- **Clean room**: work done only from public sources by people who have not seen the confidential equivalent ([section 5.7, Clean-room rule for PDK items](#57-clean-room-rule-for-pdk-items)).
- **Item**: one entry on the hit list, with its id ([`drc-forge`](projects/drc-forge.md)), its `projects/<id>.md` document and its living doc.
- **Living doc**: the editable copy of a document outside the repository, mirrored per [SYNC.md](SYNC.md).
- **Workstream (W1, W2, …)**: one of three to eight pieces of work in the Work plan, which can depend on others, each with its oracle, access, knowledge and fit ([4.9, Work plan and milestones](#49-work-plan-and-milestones)).
- **Milestone (M0 to M4)**: a rung of the ladder in the Work plan, defined by a measurable state, not an activity ([4.9, Work plan and milestones](#49-work-plan-and-milestones)).
- **Fit (A to D)**: how well a workstream suits AI agents, derived from its binding constraint: A, nothing or compute binds and agents do it; B, only access is missing; C, knowledge or a decision binds and a person decides; D, the oracle is a person or a measurement and a person executes ([4.9, Work plan and milestones](#49-work-plan-and-milestones)).
- **Harness**: the scripts, benchmarks, reference results and checks that run a tool and decide whether its output is right; built at [M0, Baseline and harness](#49-work-plan-and-milestones) ([4.9, Work plan and milestones](#49-work-plan-and-milestones)).
- **Binding constraint**: the one thing (the oracle, access, compute other than AI processes, knowledge or a decision) that limits a workstream most ([4.9, Work plan and milestones](#49-work-plan-and-milestones)).
- **Guardrail metric**: a second metric that fails when the primary metric is gamed ([4.9, Work plan and milestones](#49-work-plan-and-milestones), Metric and baseline).
- **The bar to clear**: what an item measures itself against: the physical limit, the first-principles bound, and what agent-scale work needs; never a proprietary result ([4.6, State of the art](#46-state-of-the-art)).
- **Licence class**: open-source, source-available or proprietary ([5.6, Licences](#56-licences)).
- **Open-source**: released under a licence that lets anyone study, change and redistribute it; for software, one on the Open Source Initiative's list ([5.6, Licences](#56-licences)).
- **Source-available**: readable source under a licence that restricts use, change or redistribution, or opens only after a delay, such as the Business Source License; not open ([5.6, Licences](#56-licences)).
- **Open-washing**: calling something open when its licence, data or procedure does not let others reproduce it, change it and redistribute it; named wherever a document meets it ([4.5, Why it must be open](#45-why-it-must-be-open), [5.6, Licences](#56-licences)).
- **Reproducible**: anyone can re-run the published inputs, tools and steps and get the same result ([4.5, Why it must be open](#45-why-it-must-be-open)).
- **Replicable**: an independent rebuild of the method, by other people with their own tools, gets a consistent result ([4.5, Why it must be open](#45-why-it-must-be-open)).
- **Units (of work)**: the independent pieces a workstream splits into, which set how many agents can work in parallel ([4.9, Work plan and milestones](#49-work-plan-and-milestones)).
- **Agent digest**: the seven fixed lines at the top of Start here that an agent can begin from ([4.14, Start here](#414-start-here)).
- **Lead-in**: the bold words that open a required element, in the template's exact wording ([6.3, Headings and lead-ins](#63-headings-and-lead-ins)).
- **Guidance line**: a template line in the form `> *…*`, deleted as the document is written ([6.5, Guidance lines and placeholders](#65-guidance-lines-and-placeholders)).
- **Claim status**: one of the sanctioned markers a claim carries instead of a link: `(as of YYYY-MM)`, `(estimate)`, `None found (searched: …)`, `Unknown (settled by: …)`, `Not applicable (…)`, `(from Tim's unpublished notes)`, `(Tim's claim, YYYY-MM; checked: …)` ([5.4, Claim statuses](#54-claim-statuses)).
- **Source pack**: the file of sourced claims a draft is written from ([PROCESS.md Step 0, Source pack](PROCESS.md#step-0-source-pack)).
- **Skim path**: the title, summary, headings, lead-ins with their first sentences, tables, diagram captions and agent digest; what a five-minute reader sees ([6.7, Readability and presentation](#67-readability-and-presentation)).
- **Model tier**: a size class of AI model used for a step, named generically as tier 1 (largest) to tier 4 (smallest) ([PROCESS.md section 10, Model tiers](PROCESS.md#10-model-tiers)).
- **Proprietary**: closed source, whether or not sold; the documents never write "commercial" for it ([6.1, Voice](#61-voice)).
- **Open** (this file's sense): reproducible and replicable by anyone, under a licence that lets them study, change and redistribute what produced the result ([4.5, Why it must be open](#45-why-it-must-be-open)); in every other sense the documents write open-source, publicly available, open-circuit or unanswered ([6.8, Words: pointers, terms and second readings](#68-words-pointers-terms-and-second-readings)).
- **Tim**: Tim Ansell (GitHub [mithro](https://github.com/mithro)), whose idea the hit list is and whose design documents, talks and experiments are the record most items rest on; the one human reviewer ([4.7, What Tim has already worked out](#47-what-tim-has-already-worked-out)).
- **The hit list**: the list of open-silicon projects worth doing, described in [README.md](README.md), with one item document each.
- **The template**: [TEMPLATE.md](TEMPLATE.md), at the repository root, the skeleton every item document is written in: the headings, the lead-ins, the labelled blocks and the guidance lines.
- **The lint**: [`tools/check.py`](tools/check.py), the script that runs the checks of [PROCESS.md Appendix B, The lint](PROCESS.md#appendix-b-the-lint-toolscheckpy) on a document.
- **Landing**: merging an iteration's `projects/<id>.md` to the main branch and mirroring it to the living doc, after the audit ([PROCESS.md Step 6, Land and ask](PROCESS.md#step-6-land-and-ask)); a push to the thread's branch is not a landing.
- **Canary**: one of the first two item documents through the loop, written to test these guidelines before the rest ([PROCESS.md 10.2, Pilot on the first canary](PROCESS.md#102-pilot-on-the-first-canary)).
- **AI processes**: the running of AI agents and their AI-model calls, assumed unlimited ([section 2, Principles](#2-principles), Working assumption); never costed, rationed or listed as a need.
- **Routed change**: a change to a file an item thread does not own ([`items.json`](items.json), `tools/`, [`SYNC.md`](SYNC.md), [`README.md`](README.md), a resources file), proposed in the packet and routed through the coordinator to the repository thread ([PROCESS.md 12, What agents are allowed to do on their own](PROCESS.md#12-what-agents-are-allowed-to-do-on-their-own)).
- **Review panel**: the set of reviewer personas run on a draft: the core panel for the canaries, the standard panel after them, the lighter panel after Tim's pass ([PROCESS.md 5, Reviews](PROCESS.md#5-reviews)).
- **Persona**: a reviewer brief given to a sub-agent, named for the reader it stands in for ([PROCESS.md Appendix A, Reviewer briefs](PROCESS.md#appendix-a-reviewer-briefs)).
- **Stub report**: the short report an agent writes when it reaches its stop rule or a tool call fails: what it did, where it stopped, what it did not do ([PROCESS.md 12, What agents are allowed to do on their own](PROCESS.md#12-what-agents-are-allowed-to-do-on-their-own)).
- **Deny list**: the private list of documents, names and phrases that never appear in a repository file, read by the lint's `--deny` option and by the compliance checker ([5.2, Material outside the allow-list](#52-material-outside-the-allow-list)).
- **Working-draft marker**: `(unverified)`, `(staging note; not re-checked)`, `(thin: needs research)` or a `[S<n>]` claim id; allowed in a draft, never in a landed document ([6.6, Markers that do not survive](#66-markers-that-do-not-survive)).
- **Sanctioned empty value**: `None found (searched: …)`, `Unknown (settled by: …)` or `Not applicable (…)`, the three claim statuses a required element carries when there is nothing to say ([5.4, Claim statuses](#54-claim-statuses)).
- **Word band**: the 3,000 to 6,000 words an item document stays within ([6.2, Length](#62-length)).
- **Generated tail**: the three sections ("Where it sits", "Resources", "Related items") that [`tools/build.py`](tools/build.py) appends from [`items.json`](items.json) ([6.4, Title and the generated tail](#64-title-and-the-generated-tail)).
- **Plausible-but-wrong risk**: the specific way an item's AI-produced output could look right and be wrong, always the first risk listed ([4.11, Unknowns, blockers and risks](#411-unknowns-blockers-and-risks)).
- **The packet**: the once-per-iteration post to Tim: the questions, the sentences awaiting approval, the proposed changes ([PROCESS.md 6.1, The packet](PROCESS.md#61-the-packet)).
- **Working folder**: `hitlist-work/` in the project's shared files, outside the repository, with one sub-folder per item for its drafts, reviews, pack and notes ([PROCESS.md 2, Where the work lives](PROCESS.md#2-where-the-work-lives)).
- **Item thread**: the thread in the project chat that writes one item's document ([PROCESS.md 1, Roles](PROCESS.md#1-roles)).
- **Repository thread**: the thread that owns the repository's shared files and merges the branches ([PROCESS.md 1, Roles](PROCESS.md#1-roles)).
- **FPGA**: field-programmable gate array, a chip whose logic is configured after manufacture by a [bitstream](#8-glossary).
- **ASIC**: application-specific integrated circuit, a chip manufactured for one design.
- **SoC**: system on chip, a processor with its memory and peripherals on one die.
- **EDA**: electronic design automation, the tools that design, simulate and check chips.
- **SPICE**: the family of circuit simulators, and the device-model formats they read.
- **RF, PHY, PLL**: radio frequency; the physical-layer circuit of an interface; a phase-locked loop.
- **EULA**: end-user licence agreement, the terms a vendor's tool is used under ([5.9, Vendor terms](#59-vendor-terms)).
- **NDA**: non-disclosure agreement; material under one contributes nothing ([5.2, Material outside the allow-list](#52-material-outside-the-allow-list)).
- **DMCA**: the US Digital Millennium Copyright Act, whose anti-circumvention clause bears on reverse engineering.
- **DOI, arXiv identifier, OpenAlex id**: the persistent identifiers a paper is cited by: the digital object identifier, the arXiv preprint number, the [OpenAlex](https://openalex.org/) work id ([5.10, Citations and links](#510-citations-and-links)).
- **CC0, CC-BY-4.0**: the Creative Commons public-domain dedication and attribution licence, the defaults for data and documentation ([5.6, Licences](#56-licences)).
- **Tapeout**: sending a finished design to a foundry for manufacture.
- **Golden results**: reference outputs taken as correct, against which a tool's output is compared.
- **Bring-up**: the first power-on and test of new hardware or silicon.
- **Mermaid**: the [text-to-diagram language](https://github.com/mermaid-js/mermaid) the repository host renders ([6.7, Readability and presentation](#67-readability-and-presentation)).

## 9. References

The evidence behind the claims about the world in [section 2, Principles](#2-principles). Each is a claim, not a ruling: an item document that relies on one re-checks it for its own tools and sources. Entries are resolved with a search tool and carry their identifier; a claim with no resolved source carries a status from [5.4, Claim statuses](#54-claim-statuses).

| Claim (principle) | Evidence | Status |
| --- | --- | --- |
| Published results often fail to reproduce, highly cited ones included (2) | | `Unknown (settled by: the claim audit of draft 3, 2026-10-21)` |
| Simulators and the tools built on them have bugs that change results (2) | | `Unknown (settled by: the claim audit of draft 3, 2026-10-21)` |
| Design rules and compact models stand in for physical and manufacturing constraints, each design rule with a reason (4) | | `Unknown (settled by: the claim audit of draft 3, 2026-10-21)` |
| The open tools in this field are slow, have few users, and spend much of their time recomputing unchanged values (9) | | `Unknown (settled by: the claim audit of draft 3, 2026-10-21)`; re-checked per item in [4.6, State of the art](#46-state-of-the-art) |
| More attempts at a lower success rate give more results where an [oracle](#8-glossary) gates them (10) | | `Unknown (settled by: the claim audit of draft 3, 2026-10-21)` |
| Most of Tim's stopped attempts stopped for resources, not because the idea failed (11) | Tim's statement of 2026-10-21; checked per dead end in [4.7, What Tim has already worked out](#47-what-tim-has-already-worked-out) | `(Tim's claim, 2026-10; checked: per dead end in [4.7, What Tim has already worked out](#47-what-tim-has-already-worked-out))` |
| A reader who skims gets most of a well-formed document's value; readers land mid-document through links ([6.7, Readability and presentation](#67-readability-and-presentation), [6.8, Words: pointers, terms and second readings](#68-words-pointers-terms-and-second-readings)) | | `Unknown (settled by: the claim audit of draft 3, 2026-10-21)` |

## Revision history

- **Draft 4, 2026-10-21 (in progress).** Applies the findings of five reviews of draft 3, each run from the reader's situation (the stranger, the readability and clarity reviewer, the self-application auditor, the opponent and the claim verifier), merged with one decision each in the working folder (`hitlist-guidelines/reviews/findings-draft3.md`), in committed rounds:
  - Round 1a, truth:
    - Lint checks and tools that do not exist yet are marked proposed.
    - [PROCESS.md Appendix B](PROCESS.md#appendix-b-the-lint-toolscheckpy) describes the lint as it is and [PROCESS.md Appendix C, Changes needed elsewhere](PROCESS.md#appendix-c-changes-needed-elsewhere) the changes.
    - The claim that the files pass every check they set replaced by the audit record.
    - Two links that pointed at the wrong file's section fixed.
    - Three estimates removed.
    - "Open technical questions" renamed "Unanswered technical questions" and "Open tools and projects" "Open-source tools and projects".
    - "continuous integration" and "IP block" written out.
    - "sensitivity" for sources, "tier" for models only.
  - Round 1b, contradictions:
    - One reference entry per paper and repository, every other mention linked to it.
    - [hard rules 4, 5, 6, 7, 8, 13, 14 and 15](#0-the-fifteen-hard-rules) reworded to match the sections they summarise.
    - The `(Tim's claim, YYYY-MM; checked: …)` status.
    - Fit derived from the Binding constraint line.
    - Proof levels as kinds.
    - The stop rule as a cap.
    - [M1, First checkable result](#49-work-plan-and-milestones)'s one paid board.
    - [M3, Complete or at the bar](#49-work-plan-and-milestones) "Complete or at the bar".
    - No bare `Unknown` or `estimate`.
    - Land and push defined.
    - Decision numbers named.
    - CC0 and CC-BY-4.0 placed.
    - Avoid items given a severity.
    - The executor's blind test extended.
  - Round 2, the skim path:
    - The principle as a lead-in and in the opening.
    - A bold name on each hard rule.
    - The gist in the depths table.
    - One sentence after every lead-in.
    - The rules of [5.1](#51-link-allow-list) to [5.11](#511-provenance-in-the-text) and [6.1](#61-voice) to [6.6](#66-markers-that-do-not-survive) opened with a lead-in.
    - The four reader tests named.
    - PROCESS.md's exit condition, severities and agent permissions given lead-ins and a table.
    - The [PROCESS.md 5.1, Core panel for the canaries](PROCESS.md#51-core-panel-for-the-canaries) heading shortened.
  - Round 3, words:
    - Tim, the hit list and the template introduced in each file's opening.
    - Glossary entries for the files' own terms (landing, the lint, canary, AI processes, routed change, the panels, stub report, deny list, working-draft marker, word band, generated tail, plausible-but-wrong risk, the packet, the working folder, the threads) and for the acronyms (FPGA, ASIC, SoC, EDA, SPICE, RF, EULA, NDA, DMCA, DOI, CC0).
    - Every acronym written out at its first use per section.
    - "Needs beyond AI processes".
    - `DECISIONS.md` and the working folder by name.
    - "design rule" wherever that is meant.
    - "pointer" kept for cross-references and "link" for the rest.
    - Golden results, tapeout, bring-up, Mermaid and formal equivalence checking defined.
  - Round 4, links:
    - Every section number, id, tool, term and file linked at its first mention in each `##` section with the name of what it points to, by two scripts in the working folder (one for ids and section numbers, one for glossary terms) and by hand.
    - Ranges of ids ("L1 to L19") stay bare.
    - Each box of the definition of done links the rule it checks.
    - The section numbers in the reviewer briefs linked.
    - Tool mentions link to each project's repository with what the project is. The repository links were verified on 2026-10-21 through the repositories' raw files, because github.com pages answer 403 from the writing sandbox.
    - openalex.org did not resolve from the sandbox, so its four links were not fetched (the scholarly-index connector answers, which shows the service, not the page).
  - Round 5, form:
    - The principles as claim, reason and "In the document" lines.
    - The corollary table one row per requirement.
    - The fate of the existing documents' sections as a table.
    - The long lead-ins of 4.5, 4.6 and 4.9 as a conclusion and a nested list.
    - The proof defaults as a column.
    - 5.8, 6.4 and the opening of 6.7 as lists.
    - The reviewer briefs as three labelled lines (You are, Check, Report) with A.14's five tests numbered.
    - The revision history as nested lists.
    - The mechanism table's usual label.
    - 4.14 points at the template's forms for Reproduce first and First tasks.
    - The template's three longest guidance lines split in two or three.
  - Round 6, collision words:
    - Every use of a word from the [6.8, Words: pointers, terms and second readings](#68-words-pointers-terms-and-second-readings) table outside its "Write instead" phrase replaced or pinned: may, should, up to, free, yield, sign-off, now and today, node, cell, process, model, device, flow, deck, library, regression.
    - [PROCESS.md 12, What agents are allowed to do on their own](PROCESS.md#12-what-agents-are-allowed-to-do-on-their-own) renamed from "What agents are allowed to do on their own".
    - The lint check [L18, the approval list](PROCESS.md#appendix-b-the-lint-toolscheckpy) renamed from "the sign-off file".
    - The collision table gains rows for this file's own terms (open, AI processes, landing, rule, tier) and exempts the template's fixed headings, lead-ins and block labels.
    - The template's Rungs line renamed "Rungs in place" and the Access line's "no-cost EULA" renamed "no-cost EULA".
- **Draft 3, 2026-10-21.**
  - One principle at the top ([section 1, One principle](#1-one-principle): a stranger with only this part, little time, no one to ask, no one to trust) and four reader tests.
  - [section 2, Principles](#2-principles) rewritten in the writer's words as twenty-one principles in three groups, with the working assumption of unlimited AI processes and the claims behind the principles listed in [section 9, References](#9-references).
  - Open defined as [reproducible](#8-glossary) and [replicable](#8-glossary), with the look-alike licences named ([4.5, Why it must be open](#45-why-it-must-be-open), [5.6, Licences](#56-licences)).
  - The bar to clear in place of the [proprietary](#8-glossary) yardstick ([4.6, State of the art](#46-state-of-the-art)).
  - The milestone ladder, the [verification ladder](#8-glossary) and the link decision drawn ([4.9, Work plan and milestones](#49-work-plan-and-milestones), [5.1, Link allow-list](#51-link-allow-list)).
  - [6.9, Links](#69-links) added.
  - The file's longest paragraphs, list items and table cells turned into lists and tables.
  - One box per check in the definition of done.
  - The glossary extended.
- **Draft 2.2, 2026-10-21.**
  - Readability as principles ([6.7, Readability and presentation](#67-readability-and-presentation): three depths of reading, the first sentence is the conclusion, form follows the shape of the content, one unit of form per unit of content, everything labelled, detail matched to the question, the same thing looks the same, visual properties with meaning, render and look, navigation), with Tim's five checks kept as instances.
  - The rules for pointers, terms, invented terms, colliding words and second readings ([6.8, Words: pointers, terms and second readings](#68-words-pointers-terms-and-second-readings)).
  - The Dependencies diagram in [4.9, Work plan and milestones](#49-work-plan-and-milestones).
  - [hard rules 11 and 12](#0-the-fifteen-hard-rules) reworded.
  - The definition of done and the glossary extended.
- **Draft 2.1, 2026-10-21.**
  - Tim's working principles ([section 2.1, Checking](#21-checking)) and what they require: Why not already done and [Shots on goal](#8-glossary) in [4.3, Why it is high value](#43-why-it-is-high-value).
  - Speed and quality per tool and Replace or build on in [4.6, State of the art](#46-state-of-the-art).
  - Model-dependent preconditions in [4.8, What frontier models change](#48-what-frontier-models-change).
  - The [Harness](#8-glossary), benchmarks and tool speed workstream, the extraordinary-claims rule and the Cross-checks sub-section in [4.9, Work plan and milestones](#49-work-plan-and-milestones).
  - Cross-checks with and Shared harness in [4.4, What success unlocks](#44-what-success-unlocks).
- **Draft 2, 2026-10-21.** After an AI review panel of eleven persona reviews across four model tiers and two template dry runs on [drc-forge](projects/drc-forge.md). Main changes:
  - The fifteen hard rules.
  - The process moved to [PROCESS.md](PROCESS.md) and the private side of the confidentiality rules to the project's working notes.
  - Workstream blocks with a full [oracle](#8-glossary) description, access and knowledge values, a [binding constraint](#8-glossary) and a derived fit.
  - One workstream summary table instead of a second AI-fit table.
  - Proof levels [P0, stated](#491-proof-levels) to [P5, proven in hardware or silicon](#491-proof-levels) and a gate per milestone.
  - [M1, First checkable result](#49-work-plan-and-milestones) restricted to public resources.
  - An extended [M4, Proven in hardware or silicon](#49-work-plan-and-milestones) block.
  - Cost and lead time in the needs table.
  - The clean-room and upstream-contribution rules.
  - Sanctioned empty values and the claim-status table.
  - Status thresholds for tools.
  - The "Past and parallel efforts" table.
  - Licence defaults.
  - The status-line grammar with a fixed AI disclosure.
  - One document word band with a counting rule instead of per-section bands.
  - The [agent digest](#8-glossary) and the first-task form.
  - "What Tim has already worked out" limited to documents read, with approval.
  - The generated tail removed from the template.
  - Every example rewritten from facts verified on 2026-10-21 and marked illustrative.
  - The invented "1,500 checks" figure and an internal quotation removed.
- **Draft 1, 2026-10-21.** First version.
