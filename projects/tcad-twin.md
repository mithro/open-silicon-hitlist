# tcad-twin: Open TCAD stack

## Goal

A complete open technology CAD stack: process simulation (implant, diffusion, oxidation, deposition, etch, lithography), device simulation (drift-diffusion with quantum corrections) and compact-model extraction, able to start from an existing open PDK's process description and reproduce its published device characteristics.

## Why it is high value

- It closes the loop for the fake PDKs in item 2: models generated from physics, not just fitted by hand.
- Reproducing a real open PDK gives a hard, checkable validation target.
- Commercial TCAD (Synopsys Sentaurus, Silvaco) is closed and expensive; the open pieces exist but are not integrated.

## State of the art

- Device simulation: DEVSIM, Charon (Sandia), Archimedes, open-source Genius.
- Process simulation: ViennaTS and ViennaPS (topography), FLOOXS (University of Florida).
- No open end-to-end flow from process recipe to BSIM model card.

## PDK consistency audit and generated docs

The process description, device models and device documentation (cross-sections, I-V and C-V curves, model parameters) come from one source and are audited against each other and against the PDK's published models, so a model change cannot drift silently from the documented process.

## Open questions

- Which PDK to reproduce first: IHP SG13G2, SKY130 or GF180MCU, based on how much process detail is public.
- What measured data (I-V, C-V, ring oscillators) exists to validate against.
- Accuracy target: which device metrics, within what tolerance.

## Where it sits

Layer: **PDK**. Function: **cross-cutting**. Target: **ASIC**. PDK layer: generates the device models a PDK ships, from process physics instead of foundry data.

## Resources

Loose collection of links for fleshing this item out: [resources/tcad-twin.md](../resources/tcad-twin.md).

## Related items

- [shadow-pdks](shadow-pdks.md) (Open "almost manufacturable" PDKs): Generates the device models for the fake PDKs.
- [drc-forge](drc-forge.md) (Design rule checking (DRC)): Gives the device-physics reasons behind some design rules.
- [shuttle-program](shuttle-program.md) (Open MPW tapeout programs): Measured shuttle silicon is the validation data.
- [paper-replay](paper-replay.md) (Replicating classic ASIC and FPGA papers): Published device results are reproduction targets.
- [cloud-fab](cloud-fab.md) (Virtual foundry in the cloud): The virtual foundry chains TCAD steps into a full process and fab model.
- [any-angle](any-angle.md) (Non-rectilinear layout tooling): Simulates circular and enclosed-gate devices before they are drawn into cells.
