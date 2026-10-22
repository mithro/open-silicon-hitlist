# Non-rectilinear layout tooling — resources

Loose collection, 2026-10-22. No publicly shared Drive files on this topic were found yet.

## Projects and repositories
- [KLayout](https://github.com/KLayout/klayout) — layout viewer and editor with all-angle polygons and DRC on arbitrary edges
- [Magic](https://github.com/RTimothyEdwards/magic) — VLSI layout tool; Manhattan plus 45-degree (non-Manhattan) geometry
- [OpenROAD](https://github.com/The-OpenROAD-Project/OpenROAD) — open placement and routing, built around rectangular cells and preferred-direction tracks; the baseline to beat
- [gdsfactory](https://github.com/gdsfactory/gdsfactory) — parametric layout with curved (photonic) geometry
- [SKY130](https://github.com/google/skywater-pdk), [GF180MCU](https://github.com/google/gf180mcu-pdk) (archived; development continues in its forks) and [IHP SG13G2](https://github.com/IHP-GmbH/IHP-Open-PDK) — open 180/130nm rule decks to check which angles they allow

## Papers and other reading
- [Teig, "The X architecture: not your father's diagonal wiring" (SLIP 2002)](https://doi.org/10.1145/505348.505355) — the case for 45-degree wiring on upper layers
- [Teig et al., "X Architecture Place and Route: Physical Design for the X Interconnect Architecture" (2008)](https://doi.org/10.1201/9781420013481-40) — how the X Architecture was implemented
- [Ho, Chang, Chang and Chen, "Multilevel full-chip routing for the X-based architecture" (DAC 2005)](https://doi.org/10.1145/1065579.1065734) — an academic X-architecture router
- [Chang and Chang, "X-Route: An X-architecture full-chip multilevel router" (SOCC 2007)](https://doi.org/10.1109/socc.2007.4545464) — a later X-architecture router
- [Zhu et al., "Efficient octilinear Steiner tree construction based on spanning graphs" (ASP-DAC 2004)](https://doi.org/10.1109/aspdac.2004.1337680) — net topology with 45-degree edges
- [Chen, Yao, Zhou and Cheng, "The Y-architecture: yet another on-chip interconnect solution" (ASP-DAC 2003)](https://doi.org/10.1145/1119772.1119957) — 0/60/120-degree (hexagonal) wiring
- [Zhou et al., "A hierarchical three-way interconnect architecture for hexagonal processors" (SLIP 2003)](https://doi.org/10.1145/639929.639955) — hexagonal floorplans and wiring
- [Iff et al., "HexaMesh: Scaling to Hundreds of Chiplets with an Optimized Chiplet Arrangement" (DAC 2023)](https://doi.org/10.1109/dac56929.2023.10248006) — hexagonal arrangement at the chiplet level
- [Anelli et al., "Radiation tolerant VLSI circuits in standard deep submicron CMOS technologies for the LHC experiments: practical design aspects" (IEEE TNS 1999)](https://doi.org/10.1109/23.819140) — enclosed-gate transistors in practice ([open copy](http://cds.cern.ch/record/428128/files/cer-002177437.pdf))
- [Platcheck, Cardoso and Balen, "Pseudo-Symmetric Enclosed Layout Transistors for Radiation Hardened Analog Applications" (IEEE TAES 2022)](https://doi.org/10.1109/taes.2022.3210079) — recent enclosed-gate device work
- [Pang et al., "Breakthrough curvilinear ILT enabled by multi-beam mask writing" (JM3 2021)](https://doi.org/10.1117/1.jmm.20.4.041405) — masks are already curvilinear at advanced nodes
