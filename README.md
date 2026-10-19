# Open Silicon Hit List

A shortlist of high-value targets in open source silicon (ASIC and FPGA) where frontier AI models could do work that has so far been too large, too tedious or too specialised for the open community to finish.

Each item gets its own living doc (a Claude Doc) and a matching markdown file in this repository. See [SYNC.md](SYNC.md) for how the two stay in step, and [docs.json](docs.json) for which doc backs which file.

## The list

| # | Project | One-line goal | Doc |
| --- | --- | --- | --- |
| 1 | [FPGA bitstream documentation](projects/fpga-bitstream-docs.md) | Complete, machine-readable bitstream databases for every commercial off-the-shelf FPGA family | see docs.json |
| 2 | [Open "almost manufacturable" PDKs](projects/open-fake-pdks.md) | Realistic open PDKs at 55/45nm, 28/22nm and pre-EUV FinFET (16/12nm class) | see docs.json |
| 3 | [Distributed DRC engine](projects/distributed-drc.md) | Full DRC of a reticle-sized chip in under one hour on a cluster, map-reduce style | see docs.json |
| 4 | [Open TCAD stack](projects/open-tcad-stack.md) | Process and device simulation that reproduces an existing open PDK from its process description | see docs.json |

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
