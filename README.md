# Open Silicon Hit List

A shortlist of high-value targets in open source silicon (ASIC and FPGA) where frontier AI models could do work that has so far been too large, too tedious or too specialised for the open community to finish.

Each item gets its own living doc (a Claude Doc; this overview's is [here](https://claude.ai/code/artifact/6d4a568d-1cf3-4685-9d6a-4f16aa337846)) and a matching markdown file in this repository. See [SYNC.md](SYNC.md) for how the two stay in step, and [docs.json](docs.json) for which doc backs which file.

## The list

| # | Project | One-line goal | Doc |
| --- | --- | --- | --- |
| 1 | [FPGA bitstream documentation](projects/fpga-bitstream-docs.md) | Complete, machine-readable bitstream databases for every commercial off-the-shelf FPGA family | [doc](https://claude.ai/code/artifact/aa157a9f-1861-462c-a747-93e328a6d783) |
| 2 | [Open "almost manufacturable" PDKs](projects/open-fake-pdks.md) | Realistic open PDKs at 55/45nm, 28/22nm and pre-EUV FinFET (16/12nm class) | [doc](https://claude.ai/code/artifact/d8823fe7-a41a-46e0-b526-e88e7f58725b) |
| 3 | [Design rule checking (DRC)](projects/drc.md) | Full-chip DRC in under one hour on a cluster, with exhaustive per-rule test suites and rules that explain themselves | [doc](https://claude.ai/code/artifact/8905247e-d38f-4309-8787-2e6236dedb10) |
| 4 | [Open TCAD stack](projects/open-tcad-stack.md) | Process and device simulation that reproduces an existing open PDK from its process description | [doc](https://claude.ai/code/artifact/499ffdc7-8356-448b-b175-88f36df7ce53) |
| 5 | [Adder and multiplier exploration](projects/arithmetic-units.md) | Generate and characterise many arithmetic architectures per node so open synthesis picks the best one | [doc](https://claude.ai/code/artifact/771c023d-5bc3-42c3-99ae-26d6f6d6df1f) |
| 6 | [Reproducible and signed toolchain](projects/reproducible-signed-toolchain.md) | Bit-identical tool builds and outputs, with every tool, PDK and artefact signed and logged | [doc](https://claude.ai/code/artifact/5a2f37b0-2ede-4564-b87c-fe5b19e542e8) |
| 7 | [Composable and distributed simulation](projects/composable-simulation.md) | Swap Renode, Verilator or FPGA emulation per SoC block, and scale the model across a cluster | [doc](https://claude.ai/code/artifact/4f3e9e6d-cfa4-4689-8dc0-9f8aa2afeef8) |
| 8 | [Standard cell generation](projects/standard-cells.md) | Generate, characterise and verify complete cell libraries for any PDK, voltage and track height | [doc](https://claude.ai/code/artifact/1048550f-5cc9-4bab-8977-2311b629bb19) |
| 9 | [Toolchain verification](projects/toolchain-verification.md) | Per-stage checks that each open FPGA and ASIC tool's output is correct, so failures point at the tool that caused them | [doc](https://claude.ai/code/artifact/77d56d12-4789-4728-af38-829826c6e607) |
| 10 | [LiteX accelerator interface](projects/litex-accelerator-interface.md) | Write an accelerator once and attach it over Ethernet, USB 3.0, PCIe or an on-chip bus, on FPGA or in silicon | [doc](https://claude.ai/code/artifact/95d666e0-1da6-42eb-bb7e-435b6265946c) |

Tim marked items 3 and 5 to 10 as important on 2026-10-19.

## Candidates not yet written up

Unvetted ideas to triage into full entries:

- Open SRAM, register-file and ROM compilers that are competitive at each fake-PDK node.
- Open parasitic extraction (PEX) and static timing signoff correlated against commercial tools.
- Open LVS and equivalence checking that scale to full chips.
- nextpnr (or similar) place-and-route support for every family documented by item 1.
- Open analog and mixed-signal generators (PLLs, ADCs, SerDes, IO and ESD libraries).
- Open DFT and ATPG flows.

## Adding an item

1. Create a Claude Doc for it with the sections used by the existing items: Goal, Why it is high value, State of the art, Open questions.
2. Add the matching file under `projects/`, a row to the table above, and its entry in `docs.json`.
3. Commit, following [SYNC.md](SYNC.md).
