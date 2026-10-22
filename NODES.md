# Process node break points

Tim's view of where the silicon process landscape breaks into groups, and why it matters for this list. Like the [two ways to read this list](README.md#two-ways-to-read-this-list), it is a lens across every item rather than an item of its own: it says which nodes an open PDK, open IP or an open shuttle should aim at, and where the open world could go that the commercial one has neglected.

*Status of this file: draft 1, 2026-10-21. Written from Tim's notes in the project thread and his FDSOI analysis; Tim has not yet reviewed it.*

## The break points

Going down the table, manufacturing times and prices go up significantly.

| Break point | Nodes | Wafer size | Targeted | Known for | Open PDK today | Open tape-outs |
| --- | --- | --- | --- | --- | --- | --- |
| **Legacy bulk**¹ | 180nm, 130nm | 200mm | Yes | Low volume, high mix | SKY130, GF180MCU, IHP SG13G2² | Every open shuttle so far |
| **Mid bulk** | 65nm, 55nm, 45nm, 40nm | 300mm | Yes | Best cost per transistor, traditionally | ICsprout ICS55³ | ICS55 shuttle, unconfirmed³ |
| **Late planar bulk**⁴ | 28nm, 22nm | 300mm | Yes | Loved by analog designers | None | None |
| **Pre-EUV FinFET**⁵ | GF14LPP/12LP, Intel 16, TSMC 16/12 | 300mm | Yes | Last group before EUV⁶ | None⁷ | GF12LP, Intel 16⁸ |
| — | — | — | — | — | — | — |
| **EUV FinFET** | 7nm-class with EUV, 5nm and below | 300mm | No | Price per transistor stopped falling⁹ | ASAP7, ASAP5¹⁰ | Not tracked |

1. 300mm wafers give a better cost per transistor but wreck the minimum-spend economics, so 200mm lines are where small runs make sense ([Wafer size and minimum spend](#wafer-size-and-minimum-spend)).
2. SG13G2 is a 130nm SiGe BiCMOS process.
3. [ICS55](https://github.com/openecos-projects/icsprout55-pdk) is a 55nm CMOS kit from the ICsprout foundry and Zhejiang University, first released in October 2025 under Apache 2.0 ([docs](https://icsprout55-pdk-en.readthedocs.io/en/latest/)). It is still a preview: SPICE models and RAMs are missing, and its first shuttle was planned for December 2025, which we have not confirmed ran. FreePDK45, the older stand-in, is predictive and simplified.
4. Slowly replacing mid bulk as problems such as leakage have come under control. Analog designers love it because they can still use all their randomly sized transistors.
5. The first FinFET generations, in volume since about 2014–2016 and so more than ten years old. FinFETs offer huge advantages over planar.
6. The "last" group before EUV and heavy multi-patterning made things insane, and the last where export-control issues probably don't matter. Open tooling support is actually pretty good thanks to the DARPA POSH and IDEA programmes.
7. Nothing stands in for it: there is no real open PDK and no usable predictive PDK for this class. The nearest, FreePDK15, is a generic FinFET kit modelled on no real node. Its rules are registration-gated and non-commercial, and it lacks IO and SRAM. ASAP7 sits in the EUV row. This is a big hole in the ecosystem, and a project to tackle: a predictive or shadow PDK (realistic but not manufacturable, modelled on the real node) for the GF12LP / Intel 16 / TSMC 16 class, within [shadow-pdks](projects/shadow-pdks.md). Tim's notes: [GF12LP and other 12nm pre-EUV FinFET information](https://docs.google.com/document/d/1gnzFKTaANRHWMMWReaZHsEo18S_SjQho1bG3IAqVGUE/edit).
8. OpenFASoC generators and OpenTitan on GF12LP, and OpenFASoC on Intel 16.
9. There is also a massive resource crunch because of AI, and huge export-control issues.
10. ASAP7 and ASAP5 are academic predictive PDKs from Arizona State University with Arm; they are not manufacturable.

The last row is a deliberate "no": below the 14nm-class FinFETs design gets far harder, so those nodes are best avoided if you want velocity.
- What makes it harder: heavy multi-patterning, then EUV, with far more and stranger design rules.
- The trade: ten tapeouts on a pre-EUV FinFET node look like a better deal than one on a 5nm node, especially for work that improves the design rather than "doing the same with faster transistors".

So the open ladder Tim proposes stops at pre-EUV FinFET. Each stage is gated on the open PDK for it:

| Stage | Nodes |
| --- | --- |
| 1. Budget | 180nm, 130nm |
| 2. Mid | 65nm, 55nm, 45nm |
| 3. Late planar | 28nm, 22nm |
| 4. FinFET | 16nm, 14nm, 12nm |

On export controls, the pre-EUV FinFET row means the very early FinFET processes, more than ten years old. Open source silicon is a global effort, so this list does not take any one country's point of view on controls. Why that row is widely held:
- they are made with DUV lithography, whose equipment is far less controlled than EUV;
- the technology has spread: SMIC, for one, has gone well beyond it to 7nm-class parts using DUV multi-patterning.

## Wafer size and minimum spend

The move from 200mm to 300mm wafers made each transistor cheaper for parts that ship in huge volumes, and made a small run far more expensive. For anything not shipping billions of units, the second effect wins, which is why the legacy row stays on 200mm. The newer targeted rows have little or no capacity on the smaller wafers, so they have to live with the larger wafers' minimums.

### Why 300mm helps volume

| Wafer | Area | Relative area |
| --- | --- | --- |
| 200mm | about 31,400mm² | 1× |
| 300mm | about 70,700mm² | 2.25× |

A 300mm wafer costs more to process than a 200mm one, but not 2.25 times more, and a smaller share of it is lost at the edge. A product that fills thousands of wafers a month gets more dies (individual chips) for each wafer's worth of cost, so its cost per transistor falls.

### Why 300mm hurts small runs

A multi-project wafer (MPW) shuttle shares one mask set (the set of patterns that defines every layer) and one lot (a batch of wafers processed together) among many designs. Each design buys a slot: an area of the reticle, the pattern stepped across every wafer in the lot. A slot's price has four parts:

| Part of the slot price | Set by | Shrinks with a smaller slot? |
| --- | --- | --- |
| Masks | One set per run, shared by slot area | Yes |
| Wafers | Slot area × wafers in the lot | Yes |
| Pad ring and seal ring | IO count, a fixed area per die | No |
| Dicing, sorting, packaging | Number of dies | No |

On 300mm the masks are much the same, but each wafer costs more and carries 2.25 times as many copies of every slot, while the fab still runs a minimum number of wafers per lot. So the smallest quantity a shuttle can sell grows, and its price with it.

The last two rows put a floor under the price, whatever the wafer size:
- **Pad rings don't shrink.** The pads that connect a chip to its package are sized for wire bonding and probing, not for the process node. A small die with the same IO count is mostly pad ring.
- **Dicing and handling don't shrink.** Every die needs saw streets (the gaps cut between dies), picking, sorting and usually a package, paid per die. wafer.space charges $1.50 a die for chip-on-board packaging.

wafer.space's own GF180MCU slots show the floor. Slot sizes are fractions of a full slot:

| Slot | Size | Die area | Share of full slot's area | Core area¹² | Core share | Share of full slot's price |
| --- | --- | --- | --- | --- | --- | --- |
| Full | 1×1 | 20.12mm² | 100% | 12.92mm² | 64% | 100% |
| Quarter | 0.5×0.5 | 4.9mm² | 24% | 1.73mm² | 35% | 38% |

12. With the default pad ring. A custom pad ring or none at all leaves more core; only chip-on-board packaging needs the default ring.
### What it means in practice

Tim's [cost and resource planning sheet](https://docs.google.com/spreadsheets/d/10Mf6xPItqGFgfc9TSsLO5k3iaSjSlgC8shX2bvC8wtw/edit) (2022, updated 2025) budgets an open shuttle programme node by node. The cost of one shuttle run, from its per-node finance tabs:

| Node | Foundry manufacturing | Programme management | Finishing and distribution | Total per run |
| --- | --- | --- | --- | --- |
| 180nm | $150k | $50k | $100k | $300k |
| 130nm | $250k | $100k | $100k | $450k |
| 90nm | $400k | $150k | $150k | $700k |
| 55nm | $600k | $250k | $250k | $1,100k |
| 28nm | $1,200k | $250k | $750k | $2,200k |
| 12nm | $4,000k | $350k | $1,000k | $5,350k |

The cost of one design's tapeout, from its "Market sizes" tab:

| Nodes | Low | High |
| --- | --- | --- |
| 180nm, 130nm | about $50k | about $300k |
| 110nm, 90nm | about $150k | about $400k |
| 65nm, 55nm, 45nm | about $300k | about $750k |
| 32nm, 28nm, 22nm | about $500k | about $1,250k |
| 16nm, 14nm, 12nm | about $1,000k | about $5,000k |

What the sheet shows:
- **Fixed costs rise with the node.** Finishing and distribution, the work after the wafers leave the fab, grows tenfold from 180nm to 12nm.
- **Only the legacy row is cheap enough for small runs.** A 180nm run costs about a seventh of a 28nm one.

Prices on each wafer size for a shuttle that sells 1,000-part slots or more; the wafer.space rows are standard prices for its third GF180MCU run (October 2026):

| Route | Wafer | Slot price | Parts returned | Cost per part made |
| --- | --- | --- | --- | --- |
| wafer.space quarter slot | 200mm | $3,000 | 1,000 | $3 |
| wafer.space full slot | 200mm | $8,000 | 1,000 | $8 |
| 180nm on 300mm¹¹ | 300mm | about $20,000–$30,000 | about 5,000–10,000 | about $2–$6 |

11. Tim's illustrative estimate for a 180nm shuttle on a 300mm line; not a quoted price, and the slot size is not specified. Packaging is extra on every row.

What the table shows:
- **Cost per part made is similar.** That is the number a volume buyer cares about.
- **Cost per part needed is not.** A prototype, a class or a hobby project needs tens to hundreds of parts, so on 300mm it pays for thousands it will not use.
- **Nor is the entry price.** The smallest 300mm buy is several times the cost of a 200mm slot.

Traditional MPW services on 300mm nodes avoid the part-count problem another way: they return only tens of dies per design, and charge far more per mm² of silicon. Either way, a small design pays much more on 300mm than its share of the wafers.

This is the economics [wafer.space](https://wafer.space/price.html) works within on its 200mm line. It is also why the budget stage of the ladder stays on 200mm, and why the open ecosystem needs [shuttle-program](projects/shuttle-program.md) runs that pool many small designs rather than waiting for prices on bigger wafers to fall.

## Speciality processes

Bulk CMOS and FinFET are not the only options; they are just the only ones with market share.

**FDSOI** (fully depleted silicon on insulator) offers compelling advantages but, lacking market share, has always been a second-class citizen. Its advantages:
- back-biasing to trade speed against leakage at run time ("dynamic performance");
- very low leakage;
- operation down to about 0.4V;
- good RF.

The commercial FDSOI nodes:

| Foundry | Node | Year |
| --- | --- | --- |
| ST | 28nm FDSOI | 2012 |
| Samsung | 28FDS | 2015 |
| Samsung | 18FDS | Not stated |
| GlobalFoundries | 22FDX | 2017 |
| GlobalFoundries | 12FDX | Announced |
| Renesas | 65nm SOTB | Not stated |
| SkyWater | SKY90FD | Not stated |

It has never lived up to its potential, for three reasons:
- thin IP catalogues;
- few libraries tuned for back-bias;
- tools that treat it as odd bulk.

Tim's analysis:
- [FDSOI, an underappreciated technology](https://docs.google.com/presentation/d/1pLtqy_9Vp6n__-8zAqi9UmDtX3iWpN0cwAKYDU1YeUQ/edit): the node map, marking which are open, could be opened or are missing;
- [FDSOI information](https://docs.google.com/document/d/1YN_hJBLliAt2WGyuUkR7Cun4su6-_Qrce34EmnM2GVs/edit);
- [advanced (sub-45nm) FDSOI nodes](https://docs.google.com/spreadsheets/d/1yjLZLEQznOrWpyvdtEr49cI_3vWJuQVRC9OwOpeTBDs/edit).

**Exotics** such as SiGe BiCMOS, RF SOI and silicon photonics have it a hundred times worse than FDSOI: each is a niche with its own devices, models and rules. IHP SG13G2 shows an exotic can have an open PDK; it is still the exception.

## Why this matters for the list

What keeps everyone on bulk CMOS or FinFET is not physics but the cost of the ecosystem around a process. A niche process never earns that investment, so it never gets the users that would pay for it. The ecosystem is:
- a PDK;
- standard cells, memories, IO and analog blocks;
- models good enough to simulate with;
- tools that understand the devices.

If PDKs and the IP they need could be generated quickly and easily, and simulators were better, that loop breaks: a new node or a speciality process would get a usable ecosystem far faster than the years it takes today. That is the same manual-to-generator shift the two-ways framing describes, applied to process choice. The items that do it:

- [shadow-pdks](projects/shadow-pdks.md): open "almost manufacturable" PDKs for the empty rows (55/45nm, 28/22nm with an FDSOI variant, pre-EUV FinFET). Pre-EUV FinFET, with neither a real nor a predictive kit, is the biggest hole.
- [tcad-twin](projects/tcad-twin.md) and [cloud-fab](projects/cloud-fab.md): derive device models, and in time whole PDKs, from a stated process, which is what a speciality process needs most.
- [cell-foundry](projects/cell-foundry.md), and the memory compiler and analog generator candidates in the [README](README.md#candidates-not-yet-written-up): the IP every chip needs, regenerated per node rather than redrawn, including back-bias-aware cells for FDSOI.
- [drc-forge](projects/drc-forge.md): checked rule decks, the part of a PDK that is hardest to trust when it is new.
- [arithmetic-zoo](projects/arithmetic-zoo.md) and [asic-scoreboard](projects/asic-scoreboard.md): show what each node actually buys, per design, instead of assuming smaller is better.
- [any-angle](projects/any-angle.md): layout that is not locked to right angles (hexagonal and octagonal grids, diagonal wiring, enclosed-gate transistors). The older nodes, whose rules still allow 45-degree and other angles on many layers, are where it is most practical; FinFET nodes force gridded, one-direction geometry.
- [shuttle-program](projects/shuttle-program.md): many cheap tapeouts on the 200mm row now, and on the pre-EUV FinFET row later, rather than one expensive one. A FinFET tape-out is the one place the list allows proprietary sign-off tooling, where the foundry needs it ([GUIDELINES.md hard rule 16](GUIDELINES.md#0-the-sixteen-hard-rules)); everything else runs on open tools.
