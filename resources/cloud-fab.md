# Virtual foundry in the cloud — resources

Loose collection, 2026-10-21. Drive links are publicly shared (anyone with the link).

## Tim's Google Drive (public)
- [(Open Source Silicon) TCAD Flows](https://docs.google.com/presentation/d/1lMfMHNLSb8cuPYUNfC6DerJhv1ddvy7ec7QQRA_eJcc/edit) — process-to-device loop, "TCAD on cloud"
- [Open source process characterization flow (test structures / simulation / test data collection)](https://docs.google.com/drawings/d/1uPqgGqe4tB0qG-bMLlaYzMi9ILhh217VeVVLWLFBLDY/edit) — how simulation is checked against measured silicon
- [Test structure generation and measurement](https://docs.google.com/document/d/1bjYUnjGlZHi8bQ5vNUcXg4tPJ-BaLDjqHjbtrOhnM9Y/edit) — generating test structures and measuring them, the data a simulated process is checked against (listed on mith.ro)
- [Open source TCAD Market Overview - bit.ly/pg-tcad](https://docs.google.com/spreadsheets/d/1dK1GxGl1C7v3rhWKw3RcbeZsRre66HPAOPFbgYni74A/edit) — survey of open process and device simulators (by Philipp Gühring)
- [Building a (future) open source process design kit (PDK) - bit.ly/build-pdk](https://docs.google.com/document/d/1Y-RbdGYOzswOI5EkUuCKZnWjdT1K9UbGQc_CbcIQ9O4/edit) — rules and models that state where they come from
- [SKY130 Cross sections](https://docs.google.com/drawings/d/1gbpWye9Gmi4Es-IaQQ0azpaUYSnrT6se4ogGDGroEBE/edit) — process cross-sections a simulated flow should reproduce
- [SKY130 (SkyWater PDK) -- Stackup Capacitance Data (public)](https://docs.google.com/spreadsheets/d/1N9To-xTiA7FLfQ1SNzWKe-wMckFEXVE9WPkPPjYkaxE/edit) — back-end stack-up for checking results
- [wafer.space - GF180MCU Metal Stackup](https://docs.google.com/spreadsheets/d/1dc7NKRQ8zPLQ5zjTvlCQ6sERVP4lDZzYKM6wU9RbHFI/edit) — second open process stack-up
- [Process Technologies sizes at 180nm + 130nm + 90nm](https://docs.google.com/spreadsheets/d/1kL4-_4WDMSn4z6TB4NrC2em9Kvh3i4ORAz1VXlAlLVA/edit) — feature sizes across older nodes

## Projects and repositories
- [ViennaPS](https://github.com/ViennaTools/ViennaPS) — topography simulation of etch and deposition steps
- [ViennaLS](https://github.com/ViennaTools/ViennaLS) and [ViennaRay](https://github.com/ViennaTools/ViennaRay) — level-set and ray-tracing engines under ViennaPS
- [DEVSIM](https://github.com/devsim/devsim) — open TCAD device simulator
- [gdsfactory](https://github.com/gdsfactory/gdsfactory) — layout and simulation plugins for test structures
- [OpenVAF](https://github.com/pascalkuthe/OpenVAF) — Verilog-A compiler for the compact models a process produces
- [Xyce](https://github.com/Xyce/Xyce) — circuit simulation to carry device results up to circuits
- [SKY130 raw device measurements](https://github.com/google/skywater-pdk-sky130-raw-data) — measured data to check a simulated process (archived)
- [SKY130](https://github.com/google/skywater-pdk), [GF180MCU](https://github.com/google/gf180mcu-pdk) (archived; development continues in its forks) and [IHP SG13G2](https://github.com/IHP-GmbH/IHP-Open-PDK) — open processes to model first

## Papers and other reading
- [Nassif, Strojwas and Director, "FABRICS II: A Statistically Based IC Fabrication Process Simulator" (IEEE TCAD, 1984)](https://doi.org/10.1109/tcad.1984.1270055) — early statistical process-to-yield simulation
- [Wong, Pan and Plummer, "A virtual factory-based environment for semiconductor device development" (ISMSS 1992)](https://doi.org/10.1109/ismss.1992.197649) — the virtual factory idea
- [Cipriany et al., "22nm technology yield optimization using multivariate 3D virtual fabrication" (SISPAD 2013)](https://doi.org/10.1109/sispad.2013.6650583) — virtual fabrication used for yield
- [Wang et al., "Embracing Semiverse™ Solutions: Semiconductor Virtual Fabrication and Its Applications" (EDTM 2025)](https://doi.org/10.1109/edtm61175.2025.11040233) — current proprietary virtual-fab practice
- [Sánchez, "DEVSIM: A TCAD Semiconductor Device Simulator" (JOSS, 2022)](https://doi.org/10.21105/joss.03898) — open device simulation
- [Kopp, Hassoun, Kalir and Mönch, "SMT2020—A Semiconductor Manufacturing Testbed" (IEEE TSM, 2020)](https://doi.org/10.1109/tsm.2020.3001933) — open fab-operations dataset
- [Rose, "Improved simple simulation models for semiconductor wafer factories" (WSC 2007)](https://doi.org/10.1109/wsc.2007.4419793) — reduced fab-operations models
- [Bagchi et al., "A full-factory simulator as a daily decision-support tool for 300MM wafer fabrication productivity" (WSC 2008)](https://doi.org/10.1109/wsc.2008.4736297) — whole-fab discrete-event simulation
- [Deenen, Adriaensen and Fowler, "Building a Digital Twin of the Photolithography Area of A Real-World Wafer FAB To Validate Improved Production Control" (WSC 2022)](https://doi.org/10.1109/wsc57314.2022.10015307) — fab digital twin
