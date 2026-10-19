# Open "almost manufacturable" PDKs

## Goal

Open source process design kits for process nodes with no real open PDK, realistic enough that designs built on them would need only a rule-deck and model swap to tape out at a real foundry. Initial targets:

- **55nm/45nm class** planar bulk CMOS.
- **28nm/22nm class** planar high-k metal gate (bulk, with an FD-SOI variant worth considering).
- **Pre-EUV FinFET** (GF12LP / Intel 16 class) with multi-patterning rules.

Each kit should include DRC, LVS and PEX decks, SPICE models (BSIM4 or BSIM-CMG), standard cells, SRAM, IO cells and technology files for the open flow (OpenROAD, KLayout, Magic, Xschem/ngspice).

## Why it is high value

- Today's choice is real but old open PDKs (SKY130, GF180MCU, IHP SG13G2) or predictive kits that are unrealistic: FreePDK45 has simplified rules and no real manufacturing realism, and ASAP7 is useful for research but far from a manufacturable rule set.
- A realistic advanced-node kit lets open EDA tools, IP and research be developed and benchmarked where industry actually designs.
- Writing self-consistent rule decks, models and libraries is a large, detail-heavy job well suited to AI agents, checked by the DRC and TCAD projects in this list.

## State of the art

- Real open PDKs: SkyWater SKY130 (130nm), GlobalFoundries GF180MCU (180nm), IHP SG13G2 (130nm SiGe BiCMOS).
- Predictive/academic: FreePDK45 and FreePDK15 (NCSU), ASAP7 and ASAP5 (ASU with Arm), ASU Predictive Technology Models (PTM).

## Open questions

- A concrete definition of "almost manufacturable" and how to measure it.
- How to derive rules and models only from public literature (papers, conference data) so no foundry-confidential data leaks in.
- Licensing for the outputs.
- Whether the TCAD stack (item 4) should generate the device models rather than fitting them by hand.
