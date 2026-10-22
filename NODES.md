# Process node break points

Tim's view of where the silicon process landscape breaks into groups, and why it matters for this list. Like the [two ways to read this list](README.md#two-ways-to-read-this-list), it is a lens across every item rather than an item of its own: it says which nodes an open PDK, open IP or an open shuttle should aim at, and where the open world could go that the commercial one has neglected.

*Status of this file: draft 1, 2026-10-21. Written from Tim's notes in the project thread and his FDSOI analysis; Tim has not yet reviewed it.*

## The break points

Going down the table, manufacturing times and prices go up significantly.

| Break point | Nodes | What it is good for | Open PDK today | Open tape-outs |
| --- | --- | --- | --- | --- |
| **Legacy bulk, 200mm** | 180nm, 130nm | Low volume, high mix: 300mm wafers give a better cost per transistor but wreck the minimum-spend economics | SKY130, GF180MCU, IHP SG13G2 (130nm SiGe BiCMOS) | Every open shuttle so far |
| **Mid bulk** | 65nm, 55nm, 45nm, 40nm | Traditionally the best cost per transistor and performance before costs get insane | None at real-foundry realism; FreePDK45 is predictive and simplified | None |
| **Late planar bulk** | 28nm, 22nm | Slowly replacing mid bulk as leakage has come under control; analog designers love it because they can still use all their randomly sized transistors | None | None |
| **Pre-EUV FinFET** | GF14LPP/12LP, Intel 16, TSMC 16/12 and similar, in volume since about 2014–2016 | FinFET's large gains over planar, before EUV and heavy multi-patterning; export controls probably don't matter; good open tooling from DARPA POSH and IDEA | None; predictive kits (ASAP7, FreePDK15) stand in ([Tim's notes on GF12LP and other 12nm nodes](https://docs.google.com/document/d/1gnzFKTaANRHWMMWReaZHsEo18S_SjQho1bG3IAqVGUE/edit)) | OpenFASoC and OpenTitan on GF12LP; OpenFASoC on Intel 16 |
| **EUV FinFET** | 7nm-class with EUV, 5nm and below | Not a target: the price per transistor stopped going down, AI causes a resource crunch, export controls are heavy | Not a target | Not a target |

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

- [shadow-pdks](projects/shadow-pdks.md): open "almost manufacturable" PDKs for the three empty rows (55/45nm, 28/22nm with an FDSOI variant, pre-EUV FinFET).
- [tcad-twin](projects/tcad-twin.md) and [cloud-fab](projects/cloud-fab.md): derive device models, and in time whole PDKs, from a stated process, which is what a speciality process needs most.
- [cell-foundry](projects/cell-foundry.md), and the memory compiler and analog generator candidates in the [README](README.md#candidates-not-yet-written-up): the IP every chip needs, regenerated per node rather than redrawn, including back-bias-aware cells for FDSOI.
- [drc-forge](projects/drc-forge.md): checked rule decks, the part of a PDK that is hardest to trust when it is new.
- [arithmetic-zoo](projects/arithmetic-zoo.md) and [asic-scoreboard](projects/asic-scoreboard.md): show what each node actually buys, per design, instead of assuming smaller is better.
- [any-angle](projects/any-angle.md): layout that is not locked to right angles (hexagonal and octagonal grids, diagonal wiring, enclosed-gate transistors). The older nodes, whose rules still allow 45-degree and other angles on many layers, are where it is most practical; FinFET nodes force gridded, one-direction geometry.
- [shuttle-program](projects/shuttle-program.md): many cheap tapeouts on the 200mm row now, and on the pre-EUV FinFET row later, rather than one expensive one. A FinFET tape-out is the one place the list allows proprietary sign-off tooling, where the foundry needs it ([GUIDELINES.md hard rule 16](GUIDELINES.md#0-the-sixteen-hard-rules)); everything else runs on open tools.
