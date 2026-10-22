# shadow-pdks: Open "almost manufacturable" PDKs

## Goal

Open source process design kits for process nodes with no real open PDK, realistic enough that designs built on them would need only a rule-deck and model swap to tape out at a real foundry. Initial targets:

- **55nm/45nm class** planar bulk CMOS.
- **28nm/22nm class** planar high-k metal gate (bulk, with an FD-SOI variant worth considering).
- **Pre-EUV FinFET** (GF12LP / Intel 16 class) with multi-patterning rules.

Each kit should include DRC, LVS and PEX decks, SPICE models (BSIM4 or BSIM-CMG), standard cells, SRAM, IO cells and technology files for the open flow (OpenROAD, KLayout, Magic, Xschem/ngspice).

## Why it is high value

- **Pre-EUV FinFET is the biggest hole.** Nothing covers the GF12LP / Intel 16 / TSMC 16 class: no real open PDK and no predictive one, so open tools and IP cannot be built or tested where FinFETs start. A predictive or shadow PDK for it is a project in its own right ([NODES.md](../NODES.md#the-break-points)).
- Today's choice is real but old open PDKs (SKY130, GF180MCU, IHP SG13G2) or predictive kits that are unrealistic: FreePDK45 has simplified rules and no real manufacturing realism, and ASAP7 is useful for research but far from a manufacturable rule set.
- A realistic advanced-node kit lets open EDA tools, IP and research be developed and benchmarked where industry actually designs.
- Writing self-consistent rule decks, models and libraries is a large, detail-heavy job well suited to AI agents, checked by the DRC and TCAD projects in this list.

## State of the art

- Real open PDKs: SkyWater SKY130 (130nm), GlobalFoundries GF180MCU (180nm), IHP SG13G2 (130nm SiGe BiCMOS).
- Predictive/academic: FreePDK45 and FreePDK15 (NCSU), ASAP7 and ASAP5 (ASU with Arm), ASU Predictive Technology Models (PTM).

## PDK consistency audit and generated docs

Each fake PDK ships with an automated consistency audit (every cell's Verilog, Liberty, SPICE, LEF and GDS views agree, and the DRC, LVS and PEX decks match the layer and device definitions) and with documentation generated from the PDK data rather than written by hand. The same audit should run on SKY130, GF180MCU and IHP SG13G2, which have known gaps.

## Open questions

- A concrete definition of "almost manufacturable" and how to measure it.
- How to derive rules and models only from public literature (papers, conference data) so no foundry-confidential data leaks in.
- Licensing for the outputs.
- Whether the TCAD stack should generate the device models rather than fitting them by hand.

## Where it sits

Layer: **PDK**. Function: **cross-cutting**. Target: **ASIC**. The foundation layer: open PDKs come first because they make open tools and open IP possible. Covers bulk and FinFET nodes.

## Resources

Loose collection of links for fleshing this item out: [resources/shadow-pdks.md](../resources/shadow-pdks.md).

## Related items

- [drc-forge](drc-forge.md) (Design rule checking (DRC)): Each PDK needs a rule deck, its tests and generated rule docs.
- [tcad-twin](tcad-twin.md) (Open TCAD stack): TCAD generates and validates the device models.
- [cell-foundry](cell-foundry.md) (Standard cell generation): Cell libraries make a PDK usable for digital design.
- [arithmetic-zoo](arithmetic-zoo.md) (Adder and multiplier exploration): Arithmetic units are characterised on each node.
- [asic-scoreboard](asic-scoreboard.md) (ASIC benchmarking): Benchmarks compare PPA across real and fake nodes.
- [shuttle-program](shuttle-program.md) (Open MPW tapeout programs): Shuttles validate the real PDKs the fake ones are modelled on.
- [format-kit](format-kit.md) (Libraries for every EDA file format): Audits rely on correct readers for every view.
- [cloud-fab](cloud-fab.md) (Virtual foundry in the cloud): A virtual foundry can derive each fake PDK from a stated process.
- [any-angle](any-angle.md) (Non-rectilinear layout tooling): A fake PDK can carry non-Manhattan rules for new tools to target.
