# cloud-fab: Virtual foundry in the cloud

## Goal

An open, cloud-scale simulation of a whole foundry: every process step and recipe (deposition, lithography, etch, implant, anneal, CMP) modelled end to end, so a change to any recipe shows its effect on the finished devices, their variation and yield, and on how the fab runs (tool usage, cycle time, throughput and cost of a lot).

## Why it is high value

- Process development today happens on real wafers inside a handful of companies; a virtual fab lets anyone explore process choices, and lets open PDKs be derived from a simulated process rather than reverse engineered.
- It turns the fake PDKs into something principled: each PDK becomes the output of a stated process flow that can be inspected, varied and re-run.
- Linking device physics to fab operations (throughput, cost, yield) answers questions no single tool answers today, such as what a recipe change costs per wafer.
- The work is huge, parallel and checkable against measured data from open shuttles, which suits agents and large-scale cloud compute.

## State of the art

- Process and device TCAD: proprietary Sentaurus and Silvaco; open tools such as DEVSIM, Charon and academic process simulators cover parts of the flow (see tcad-twin).
- Virtual fabrication: proprietary tools such as Coventor SEMulator3D model 3D process steps; there is no open equivalent.
- Fab operations: discrete-event fab simulators and digital twins are used inside foundries and are proprietary; academic models (for example the SEMATECH and SMT2020 datasets) exist for scheduling research.

## Open questions

- Which process to model first: one already open (SKY130, GF180MCU, IHP SG13G2) so results can be checked against its PDK and silicon.
- How far to go on fidelity versus speed for each step, and where machine-learned surrogates replace physics.
- How to model fab operations without proprietary tool and recipe data.
- How results feed back into the fake PDKs, DRC rules and device models.

## Where it sits

Layer: **PDK**. Function: **cross-cutting**. Target: **ASIC**. PDK layer, one level below the PDK itself: the process a PDK comes from. Moves process development from wafers inside a few companies to open, automated simulation.

## Resources

Loose collection of links for fleshing this item out: [resources/cloud-fab.md](../resources/cloud-fab.md).

## Related items

- [tcad-twin](tcad-twin.md) (Open TCAD stack): TCAD supplies the per-step process and device physics.
- [shadow-pdks](shadow-pdks.md) (Open "almost manufacturable" PDKs): Each fake PDK becomes the output of a simulated process flow.
- [drc-forge](drc-forge.md) (Design rule checking (DRC)): Process limits from the simulation explain and generate design rules.
- [shuttle-program](shuttle-program.md) (Open MPW tapeout programs): Measured shuttle silicon checks the simulated process.
- [sim-mosaic](sim-mosaic.md) (Composable and distributed simulation): Shares the distributed, mixed-fidelity simulation approach.
