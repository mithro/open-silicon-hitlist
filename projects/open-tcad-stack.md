# Open TCAD stack

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

## Open questions

- Which PDK to reproduce first: IHP SG13G2, SKY130 or GF180MCU, based on how much process detail is public.
- What measured data (I-V, C-V, ring oscillators) exists to validate against.
- Accuracy target: which device metrics, within what tolerance.
