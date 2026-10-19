# Open Silicon Hit List

A shortlist of high-value targets in open source silicon (ASIC and FPGA) where frontier AI models could do work that has so far been too large, too tedious or too specialised for the open community to finish.

Each item gets its own living doc (a Claude Doc; this overview's is [here](https://claude.ai/code/artifact/6d4a568d-1cf3-4685-9d6a-4f16aa337846)) and a matching markdown file in this repository. See [SYNC.md](SYNC.md) for how the two stay in step, and [docs.json](docs.json) for which doc backs which file.

## The list

| # | Project | One-line goal | Doc |
| --- | --- | --- | --- |
| 1 | [FPGA bitstream documentation](projects/fpga-bitstream-docs.md) | Complete, machine-readable bitstream databases for every commercial off-the-shelf FPGA family | [doc](https://claude.ai/code/artifact/aa157a9f-1861-462c-a747-93e328a6d783) |
| 2 | [Open "almost manufacturable" PDKs](projects/open-fake-pdks.md) | Realistic open PDKs at 55/45nm, 28/22nm and pre-EUV FinFET (16/12nm class) | [doc](https://claude.ai/code/artifact/d8823fe7-a41a-46e0-b526-e88e7f58725b) |
| 3 | [Distributed DRC engine](projects/distributed-drc.md) | Full DRC of a reticle-sized chip in under one hour on a cluster, map-reduce style | [doc](https://claude.ai/code/artifact/8905247e-d38f-4309-8787-2e6236dedb10) |
| 4 | [Open TCAD stack](projects/open-tcad-stack.md) | Process and device simulation that reproduces an existing open PDK from its process description | [doc](https://claude.ai/code/artifact/499ffdc7-8356-448b-b175-88f36df7ce53) |

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
