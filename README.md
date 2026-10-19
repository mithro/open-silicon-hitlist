# Open Silicon Hit List

A shortlist of high-value targets in open source silicon (ASIC and FPGA) where frontier AI models could do work that has so far been too large, too tedious or too specialised for the open community to finish.

Each item gets its own living doc (a Claude Doc; this overview's is [here](https://claude.ai/code/artifact/6d4a568d-1cf3-4685-9d6a-4f16aa337846)) and a matching markdown file in this repository. See [SYNC.md](SYNC.md) for how the two stay in step, and [docs.json](docs.json) for which doc backs which file.

## The list

| Id | Project | One-line goal | Important |
| --- | --- | --- | --- |
| [bitstream-atlas](projects/bitstream-atlas.md) | FPGA bitstream documentation ([doc](https://claude.ai/code/artifact/aa157a9f-1861-462c-a747-93e328a6d783)) | Complete, machine-readable bitstream databases for every commercial off-the-shelf FPGA family |  |
| [shadow-pdks](projects/shadow-pdks.md) | Open "almost manufacturable" PDKs ([doc](https://claude.ai/code/artifact/d8823fe7-a41a-46e0-b526-e88e7f58725b)) | Realistic open PDKs at 55/45nm, 28/22nm and pre-EUV FinFET (16/12nm class), with consistency audits and generated docs |  |
| [drc-forge](projects/drc-forge.md) | Design rule checking (DRC) ([doc](https://claude.ai/code/artifact/8905247e-d38f-4309-8787-2e6236dedb10)) | Full-chip DRC in under one hour on a cluster, with exhaustive per-rule test suites and rules that explain themselves | Yes |
| [tcad-twin](projects/tcad-twin.md) | Open TCAD stack ([doc](https://claude.ai/code/artifact/499ffdc7-8356-448b-b175-88f36df7ce53)) | Process and device simulation that reproduces an existing open PDK from its process description |  |
| [arithmetic-zoo](projects/arithmetic-zoo.md) | Adder and multiplier exploration ([doc](https://claude.ai/code/artifact/771c023d-5bc3-42c3-99ae-26d6f6d6df1f)) | Generate and characterise many arithmetic architectures per node so open synthesis picks the best one | Yes |
| [signed-builds](projects/signed-builds.md) | Reproducible and signed toolchain ([doc](https://claude.ai/code/artifact/5a2f37b0-2ede-4564-b87c-fe5b19e542e8)) | Bit-identical tool builds and outputs, with every tool, PDK and artefact signed and logged | Yes |
| [sim-mosaic](projects/sim-mosaic.md) | Composable and distributed simulation ([doc](https://claude.ai/code/artifact/4f3e9e6d-cfa4-4689-8dc0-9f8aa2afeef8)) | Swap Renode, Verilator or FPGA emulation per SoC block, and scale the model across a cluster | Yes |
| [cell-foundry](projects/cell-foundry.md) | Standard cell generation ([doc](https://claude.ai/code/artifact/1048550f-5cc9-4bab-8977-2311b629bb19)) | Generate, characterise and verify complete cell libraries for any PDK, voltage and track height | Yes |
| [flow-proofs](projects/flow-proofs.md) | Toolchain verification ([doc](https://claude.ai/code/artifact/77d56d12-4789-4728-af38-829826c6e607)) | Per-stage checks that each open FPGA and ASIC tool's output is correct, so failures point at the tool that caused them | Yes |
| [accel-harness](projects/accel-harness.md) | Accelerator interface and harness (FPGA and ASIC) ([doc](https://claude.ai/code/artifact/95d666e0-1da6-42eb-bb7e-435b6265946c)) | One accelerator interface with two focuses: a LiteX FPGA flavour and a Sea2sky-style ASIC harness, sharing host software | Yes |
| [fpga-scoreboard](projects/fpga-scoreboard.md) | FPGA benchmarking ([doc](https://claude.ai/code/artifact/2cb90a0e-c02a-438b-9d1a-f686e1b99816)) | Continuous open-versus-vendor FPGA toolchain benchmark on real boards, with seed statistics | Yes |
| [asic-scoreboard](projects/asic-scoreboard.md) | ASIC benchmarking ([doc](https://claude.ai/code/artifact/1f6ff4ba-c327-40d2-a8a2-adbb152efca9)) | Re-runnable benchmark of open ASIC flows on every open shuttle design, tracked over time | Yes |
| [open-pnr](projects/open-pnr.md) | FPGA Interchange and open place and route ([doc](https://claude.ai/code/artifact/a153f4c8-3b75-4ebe-828d-e412c1702213)) | Revive FPGA Interchange and make VPR and nextpnr competitive with vendor tools |  |
| [instant-rebuild](projects/instant-rebuild.md) | Incremental toolchains ([doc](https://claude.ai/code/artifact/b85b73c8-f073-47b1-ae95-a21397267324)) | FPGA and ASIC flows where a small change costs a small rebuild, identical to a full one |  |
| [open-fabric](projects/open-fabric.md) | Fully open FPGA and eFPGA ([doc](https://claude.ai/code/artifact/66911c98-027c-4bef-a820-a7d1f3b301af)) | An open FPGA and eFPGA architecture, hardened with open tools, competitive with commercial parts |  |
| [open-links](projects/open-links.md) | Open high-speed connectivity IP ([doc](https://claude.ai/code/artifact/8c19b51b-76f6-40a0-94b4-a582eefd7d1f)) | Open PCIe, USB 3, Ethernet and DDR controllers and PHYs that work on FPGAs and in ASICs |  |
| [shuttle-program](projects/shuttle-program.md) | Open MPW tapeout programs ([doc](https://claude.ai/code/artifact/76226e22-8eb8-40b6-9f0c-e1c66ee2cea2)) | Recurring open shuttles whose designs and silicon results build a library of proven IP and benchmarks |  |
| [paper-replay](projects/paper-replay.md) | Replicating classic ASIC and FPGA papers ([doc](https://claude.ai/code/artifact/7e9bd90f-7872-47ad-98a8-b3e2635ab5c4)) | Reproduce key past papers and test whether their conclusions hold with AI and fast compute |  |
| [format-kit](projects/format-kit.md) | Libraries for every EDA file format ([doc](https://claude.ai/code/artifact/ca1fcb56-52dd-43ce-a0cd-4ba22b4f0b1d)) | Well-tested readers and writers for every open and proprietary EDA format, shared by all tools |  |
| [hard-core](projects/hard-core.md) | Partial hardening: ASIC core plus eFPGA and software ([doc](https://claude.ai/code/artifact/9e30e382-1584-4286-b9c8-2f3bd7a4fd28)) | Harden only the critical high-performance core as ASIC; put the rest in eFPGA and software on CPUs |  |

Tim marked the items with "Yes" as important on 2026-10-19. Ids are stable names for each item; the order of the table carries no meaning.

## How the items connect

Each item lists its closest neighbours under "Related items". At a higher level the list falls into four groups:

- **PDKs and physical design** (shadow-pdks, drc-forge, tcad-twin, cell-foundry, shuttle-program): shadow-pdks needs rule decks (drc-forge), physics-based models (tcad-twin) and cell libraries (cell-foundry) to be usable, and shuttles (shuttle-program) to prove them in silicon.
- **FPGA ecosystem** (bitstream-atlas, open-pnr, open-fabric, fpga-scoreboard): bitstream-atlas feeds open-pnr; open-fabric skips the reverse engineering entirely; fpga-scoreboard scores all of it.
- **Toolchain quality and speed** (signed-builds, flow-proofs, instant-rebuild, asic-scoreboard, paper-replay, format-kit): signed-builds makes flow-proofs and instant-rebuild checkable; format-kit gives every tool correct readers and writers; asic-scoreboard and paper-replay measure the result.
- **Design, IP and system integration** (arithmetic-zoo, accel-harness, open-links, sim-mosaic, hard-core): arithmetic-zoo and open-links are building blocks; accel-harness and sim-mosaic connect them to hosts and to each other; hard-core combines a hard block, open-fabric eFPGA and CPUs in one chip.

## Candidates not yet written up

Unvetted ideas to triage into full entries:

- Open SRAM, register-file and ROM compilers that are competitive at each fake-PDK node.
- Open parasitic extraction (PEX) and static timing signoff correlated against commercial tools.
- Open LVS and equivalence checking that scale to full chips.
- Open analog and mixed-signal generators (PLLs, ADCs, SerDes, IO and ESD libraries).
- Open DFT and ATPG flows.

## Adding an item

1. Create a Claude Doc for it with the sections the existing items use: Goal, Why it is high value, State of the art, Open questions, then Related items.
2. Add the matching file under `projects/` and its entry (id, path, title, doc ids, one-line goal, related items, group) in `items.json`.
3. Run `python3 tools/build.py` to regenerate this table, the groups and every "Related items" section, then mirror the changed sections into the docs and commit, following [SYNC.md](SYNC.md).
