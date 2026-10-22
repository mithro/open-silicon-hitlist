# Open Silicon Hit List

A shortlist of high-value targets in open source silicon (ASIC and FPGA) where frontier AI models could do work that has so far been too large, too tedious or too specialised for the open community to finish.

Each item gets its own living doc (a Claude Doc; this overview's is [here](https://claude.ai/code/artifact/6d4a568d-1cf3-4685-9d6a-4f16aa337846)) and a matching markdown file in this repository. See [SYNC.md](SYNC.md) for how the two stay in step, and [docs.json](docs.json) for which doc backs which file.

## Start with the canaries

Every item on this list needs the same first step before anyone builds anything: a deep-dive document that turns its one-paragraph idea into a brief an AI agent can plan and start work from. Two items have had that step, done by AI agents end to end:

- **[drc-forge](projects/drc-forge.md)**, design rule checking ([doc](https://claude.ai/code/artifact/8905247e-d38f-4309-8787-2e6236dedb10)): test layouts and a sourced reason for every design rule of three open PDKs, a per-PDK consistency audit, and a rule-checking engine that splits a layout across machines. Draft 3.
- **[bitstream-atlas](projects/bitstream-atlas.md)**, FPGA bitstream documentation ([doc](https://claude.ai/code/artifact/aa157a9f-1861-462c-a747-93e328a6d783)): open, machine-readable documentation of how each off-the-shelf FPGA family encodes a design, with a public count of what is still unexplained. Draft 2.

Each was written from a source pack of public material and Tim's documents, reviewed by a panel of AI reviewers at more than one model tier, claim-audited and linted. Neither has had a human review yet, and each carries five questions for Tim. They are the examples to read first: [TEMPLATE.md](TEMPLATE.md) is the form they fill, [GUIDELINES.md](GUIDELINES.md) the rules they follow, [PROCESS.md](PROCESS.md) the loop that produced them, and [MODELS.md](MODELS.md) what each model tier did on them. The other items are still one-page overviews waiting for the same step.

## Open tools only

Every item can be done with open-source tools alone ([GUIDELINES.md hard rule 16](GUIDELINES.md#0-the-sixteen-hard-rules)). There are two exceptions: vendor FPGA tools, used to produce reference bitstreams for bitstream documentation, and the sign-off tooling a FinFET tape-out needs. Benchmarks test open tools against themselves: every change is tracked over time, ideas are measured against the best earlier open result, and every run is kept as a corpus AI can learn and generalise from.

## Two ways to read this list

Tim describes a complete open silicon ecosystem in two ways ([slides](https://docs.google.com/presentation/d/1zuEaR5LsVPNMacMraFNnLPR5i1pNiTdLMwk0zBnBjK8/edit); the halves on their own: [Interface / Computation / Storage](https://docs.google.com/presentation/d/1LD-dE5ID98Kfb1dc6jWuprDgtSDS5p8-BL8j6nobjqk/edit) and [Tooling / IP / PDK](https://docs.google.com/presentation/d/1YGcGUTdSPlVF8DzVdG1Kpy7n9Dix1SJ3gGtqvsaTZL8/edit)). By what a chip does: **interface**, **computation** and **storage**. And by what you need to build one: a **PDK**, **tooling** and **IP**, where open PDKs come first because they make open tools and open IP possible. Across both runs a shift from manual work to generators, which is where frontier models help most. Each item is tagged with its layer, function and target (ASIC, FPGA or both) in its "Where it sits" section; the grids under "How the items connect" show where the list is thin.

## Process node break points

A third lens runs across the list: which process nodes to aim at. Tim splits them into five groups, and the list targets the first four:

| Group | Nodes | Wafer size | Targeted | Known for |
| --- | --- | --- | --- | --- |
| Legacy bulk¹ | 180nm, 130nm | 200mm | Yes | Low-volume, high-mix work |
| Mid bulk | 65nm to 40nm | 300mm | Yes | Traditionally the best cost per transistor |
| Late planar bulk² | 28nm, 22nm | 300mm | Yes | Loved by analog designers |
| Pre-EUV FinFET³ | GF12LP, Intel 16, TSMC 16 | 300mm | Yes | Good open tooling from DARPA POSH and IDEA |
| — | — | — | — | — |
| EUV FinFET | 7nm-class and below | 300mm | No | Price per transistor stopped falling |

1. 200mm suits small runs; 300mm wrecks minimum-spend economics ([why](NODES.md#wafer-size-and-minimum-spend)).
2. Slowly replacing mid bulk.
3. The early FinFET generations, more than ten years old; the last group before EUV. No real or usable predictive open PDK covers it, a big hole that [shadow-pdks](projects/shadow-pdks.md) should fill.

Below 14nm-class FinFET things get really hard and complicated, so those nodes are best avoided if you want velocity. Speciality processes such as FDSOI and SiGe have real advantages but small ecosystems; generating PDKs, IP and models quickly is how open silicon could break out of "everything is bulk CMOS or FinFET". [NODES.md](NODES.md) has the detail and the items that serve each group.

## The list

| Id | Project | Target | Living doc | One-line goal |
| --- | --- | --- | --- | --- |
| [bitstream-atlas](projects/bitstream-atlas.md) | FPGA bitstream documentation | FPGA | [doc](https://claude.ai/code/artifact/aa157a9f-1861-462c-a747-93e328a6d783) | Complete, machine-readable bitstream databases for every commercial off-the-shelf FPGA family |
| [shadow-pdks](projects/shadow-pdks.md) | Open "almost manufacturable" PDKs | ASIC | [doc](https://claude.ai/code/artifact/d8823fe7-a41a-46e0-b526-e88e7f58725b) | Realistic open PDKs at 55/45nm, 28/22nm and 16/12nm pre-EUV FinFET, with consistency audits and generated docs |
| [drc-forge](projects/drc-forge.md) | Design rule checking (DRC) | ASIC | [doc](https://claude.ai/code/artifact/8905247e-d38f-4309-8787-2e6236dedb10) | Per-rule tests, sourced reasons and a rule-deck audit for SKY130, GF180MCU and SG13G2, plus a distributed DRC engine |
| [tcad-twin](projects/tcad-twin.md) | Open TCAD stack | ASIC | [doc](https://claude.ai/code/artifact/499ffdc7-8356-448b-b175-88f36df7ce53) | Process and device simulation that reproduces an existing open PDK from its process description |
| [arithmetic-zoo](projects/arithmetic-zoo.md) | Adder and multiplier exploration | ASIC and FPGA | [doc](https://claude.ai/code/artifact/771c023d-5bc3-42c3-99ae-26d6f6d6df1f) | Generate and characterise many arithmetic architectures per node so open synthesis picks the best one |
| [signed-builds](projects/signed-builds.md) | Reproducible and signed toolchain | ASIC and FPGA | [doc](https://claude.ai/code/artifact/5a2f37b0-2ede-4564-b87c-fe5b19e542e8) | Bit-identical tool builds and outputs, with every tool, PDK and artefact signed and logged |
| [sim-mosaic](projects/sim-mosaic.md) | Composable and distributed simulation | ASIC and FPGA | [doc](https://claude.ai/code/artifact/4f3e9e6d-cfa4-4689-8dc0-9f8aa2afeef8) | Swap Renode, Verilator or FPGA emulation per SoC block, and scale the model across a cluster |
| [cell-foundry](projects/cell-foundry.md) | Standard cell generation | ASIC | [doc](https://claude.ai/code/artifact/1048550f-5cc9-4bab-8977-2311b629bb19) | Generate, characterise and verify complete cell libraries for any PDK, voltage and track height |
| [flow-proofs](projects/flow-proofs.md) | Toolchain verification | ASIC and FPGA | [doc](https://claude.ai/code/artifact/77d56d12-4789-4728-af38-829826c6e607) | Per-stage checks that each open FPGA and ASIC tool's output is correct, so failures point at their cause |
| [accel-harness](projects/accel-harness.md) | Accelerator interface and harness | ASIC and FPGA | [doc](https://claude.ai/code/artifact/95d666e0-1da6-42eb-bb7e-435b6265946c) | One accelerator interface, as a LiteX FPGA flavour and a Sea2sky-style ASIC harness sharing host software |
| [fpga-scoreboard](projects/fpga-scoreboard.md) | FPGA benchmarking | FPGA | [doc](https://claude.ai/code/artifact/2cb90a0e-c02a-438b-9d1a-f686e1b99816) | Continuous benchmark of open FPGA toolchains against themselves on real boards, with seed statistics, kept as an AI training corpus |
| [asic-scoreboard](projects/asic-scoreboard.md) | ASIC benchmarking | ASIC | [doc](https://claude.ai/code/artifact/1f6ff4ba-c327-40d2-a8a2-adbb152efca9) | Re-runnable benchmark of open ASIC flows against themselves on every open shuttle design, kept as an AI training corpus |
| [open-pnr](projects/open-pnr.md) | FPGA Interchange and open place and route | FPGA | [doc](https://claude.ai/code/artifact/a153f4c8-3b75-4ebe-828d-e412c1702213) | Revive FPGA Interchange and make VPR and nextpnr better release over release, measured open against open |
| [instant-rebuild](projects/instant-rebuild.md) | Incremental toolchains | ASIC and FPGA | [doc](https://claude.ai/code/artifact/b85b73c8-f073-47b1-ae95-a21397267324) | FPGA and ASIC flows where a small change costs a small rebuild, identical to a full one |
| [open-fabric](projects/open-fabric.md) | Fully open FPGA and eFPGA | ASIC and FPGA | [doc](https://claude.ai/code/artifact/66911c98-027c-4bef-a820-a7d1f3b301af) | An open FPGA and eFPGA architecture, hardened with open tools, improving generation over generation |
| [open-links](projects/open-links.md) | Open high-speed connectivity IP | ASIC and FPGA | [doc](https://claude.ai/code/artifact/8c19b51b-76f6-40a0-94b4-a582eefd7d1f) | Open PCIe, USB 3, Ethernet and DDR controllers and PHYs that work on FPGAs and in ASICs |
| [shuttle-program](projects/shuttle-program.md) | Open MPW tapeout programs | ASIC | [doc](https://claude.ai/code/artifact/76226e22-8eb8-40b6-9f0c-e1c66ee2cea2) | Recurring open shuttles whose designs and silicon results build a library of proven IP and benchmarks |
| [paper-replay](projects/paper-replay.md) | Replicating classic ASIC and FPGA papers | ASIC and FPGA | [doc](https://claude.ai/code/artifact/7e9bd90f-7872-47ad-98a8-b3e2635ab5c4) | Reproduce key past papers and test whether their conclusions hold with AI and fast compute |
| [format-kit](projects/format-kit.md) | Libraries for every EDA file format | ASIC and FPGA | [doc](https://claude.ai/code/artifact/ca1fcb56-52dd-43ce-a0cd-4ba22b4f0b1d) | Well-tested readers and writers for every open EDA format, and proprietary ones with a public description, shared by all tools |
| [hard-core](projects/hard-core.md) | Partial hardening | ASIC | [doc](https://claude.ai/code/artifact/9e30e382-1584-4286-b9c8-2f3bd7a4fd28) | Harden only the critical high-performance core as ASIC, with the rest in eFPGA and software on CPUs |
| [open-airwaves](projects/open-airwaves.md) | Open wireless with eFPGA and SDR | ASIC and FPGA | [doc](https://claude.ai/code/artifact/ab1d8101-fcd5-4f6a-8ea4-65b9a9ed6879) | Open LoRa, NFC, Bluetooth, WiFi and cellular stacks with open RF front ends and baseband in eFPGA and software |
| [cloud-fab](projects/cloud-fab.md) | Virtual foundry in the cloud | ASIC | [doc](https://claude.ai/code/artifact/4de972cb-2eb1-43e3-8149-9d38ab529e37) | Simulate every process step and recipe of a fab, and its effect on devices, yield and fab operations |
| [any-angle](projects/any-angle.md) | Non-rectilinear layout tooling | ASIC | [doc](https://claude.ai/code/artifact/ed4a53a0-4b38-4f00-8ad5-81be845d6bca) | Open layout tools, rules and cells for hexagonal, octagonal, diagonal and curved geometry, measured against Manhattan flows |

Ids are stable names for each item; the order of the table carries no meaning.

## How the items connect

Each item lists its closest neighbours under "Related items". At a higher level, the items sit in the layers you need to make a chip, with FPGA work alongside ASIC work:

| Layer | ASIC | FPGA | Both |
| --- | --- | --- | --- |
| PDK | [shadow-pdks](projects/shadow-pdks.md), [drc-forge](projects/drc-forge.md), [tcad-twin](projects/tcad-twin.md), [cell-foundry](projects/cell-foundry.md), [cloud-fab](projects/cloud-fab.md), [any-angle](projects/any-angle.md) | [bitstream-atlas](projects/bitstream-atlas.md) |  |
| Tooling | [drc-forge](projects/drc-forge.md), [asic-scoreboard](projects/asic-scoreboard.md), [any-angle](projects/any-angle.md) | [fpga-scoreboard](projects/fpga-scoreboard.md), [open-pnr](projects/open-pnr.md) | [signed-builds](projects/signed-builds.md), [sim-mosaic](projects/sim-mosaic.md), [flow-proofs](projects/flow-proofs.md), [instant-rebuild](projects/instant-rebuild.md), [paper-replay](projects/paper-replay.md), [format-kit](projects/format-kit.md) |
| IP | [hard-core](projects/hard-core.md) |  | [arithmetic-zoo](projects/arithmetic-zoo.md), [accel-harness](projects/accel-harness.md), [open-fabric](projects/open-fabric.md), [open-links](projects/open-links.md), [open-airwaves](projects/open-airwaves.md) |
| Proof in silicon | [shuttle-program](projects/shuttle-program.md) |  |  |

For FPGAs the analogy is direct: the device database (bitstream-atlas) plays the PDK's role.

By what a chip does, the same items cover:

| Layer | Interface | Computation | Storage | Cross-cutting |
| --- | --- | --- | --- | --- |
| PDK |  |  |  | [bitstream-atlas](projects/bitstream-atlas.md), [shadow-pdks](projects/shadow-pdks.md), [drc-forge](projects/drc-forge.md), [tcad-twin](projects/tcad-twin.md), [cell-foundry](projects/cell-foundry.md), [cloud-fab](projects/cloud-fab.md), [any-angle](projects/any-angle.md) |
| Tooling |  |  |  | [drc-forge](projects/drc-forge.md), [signed-builds](projects/signed-builds.md), [sim-mosaic](projects/sim-mosaic.md), [flow-proofs](projects/flow-proofs.md), [fpga-scoreboard](projects/fpga-scoreboard.md), [asic-scoreboard](projects/asic-scoreboard.md), [open-pnr](projects/open-pnr.md), [instant-rebuild](projects/instant-rebuild.md), [paper-replay](projects/paper-replay.md), [format-kit](projects/format-kit.md), [any-angle](projects/any-angle.md) |
| IP | [accel-harness](projects/accel-harness.md), [open-links](projects/open-links.md), [open-airwaves](projects/open-airwaves.md) | [arithmetic-zoo](projects/arithmetic-zoo.md), [accel-harness](projects/accel-harness.md), [open-fabric](projects/open-fabric.md), [hard-core](projects/hard-core.md) |  |  |
| Proof in silicon |  |  |  | [shuttle-program](projects/shuttle-program.md) |

What the grid shows:

- **Storage has no item.** The memory compilers candidate (SRAM, register file, ROM) would fill it.
- **Analog interface is thin.** Only open-links' PHYs and open-airwaves' RF front ends touch it; the analog generators candidate fills the rest.
- **CPUs have no item.** This is deliberate: open RISC-V cores are plentiful, and the gaps are in the layers around them.
- **Tooling dominates,** by choice: open PDKs and tools are what make open IP possible.

## Candidates not yet written up

Unvetted ideas to triage into full entries. Loose collections of links for every item and for some of these candidates are in [resources/](resources/README.md).

- Open SRAM, register-file and ROM compilers that are competitive at each fake-PDK node.
- Open parasitic extraction (PEX) and static timing signoff checked against each other and against measured silicon.
- Open LVS and equivalence checking that scale to full chips.
- Open analog and mixed-signal generators (PLLs, ADCs, SerDes, IO and ESD libraries).
- Open DFT and ATPG flows.

## Adding an item

1. Create a Claude Doc for it and the matching file under `projects/`, using [TEMPLATE.md](TEMPLATE.md). [GUIDELINES.md](GUIDELINES.md) says what each section must contain and [PROCESS.md](PROCESS.md) how a document is drafted, reviewed and landed.
2. Add its entry (id, path, title, doc ids, one-line goal, layer, function, target, a one-line note on where it sits, related items) in `items.json`.
3. Run `python3 tools/build.py` to regenerate this table, the grids and every "Where it sits", "Resources" and "Related items" section, and `python3 tools/check.py projects/<id>.md` to lint the document. Then mirror the changed sections into the docs and commit, following [SYNC.md](SYNC.md).

## How this stays in sync with git

Every doc here has a markdown twin in the git repository (this one is README.md). The docs are where people edit and comment; the repository is the versioned history. Any change lands in both in the same session, and a change made directly in git is copied back into the doc. The full convention is in [SYNC.md](SYNC.md) in the repository.
