# open-airwaves: Open wireless stacks on eFPGA and software-defined radio

## Goal

Open wireless stacks (LoRa, NFC, Bluetooth, WiFi and cellular) built on eFPGA and software-defined radio (SDR). The RF front end (LNA, mixer, PLL, ADC and DAC) is analog IP on an open PDK, while modulation, the PHY and the protocol stay reprogrammable in eFPGA fabric and software. The same design can be prototyped on an FPGA with an SDR front end and then taped out.

## Why it is high value

- Wireless is one of the largest classes of chips and today depends entirely on licensed RF IP and closed baseband firmware; there is no open path from radio standard to silicon.
- Putting the baseband in eFPGA and software means one chip can follow evolving standards, regional variants and new protocols without a respin.
- Radio standards are long, precise and testable against reference waveforms and conformance vectors, which suits agents writing, testing and optimising modems and protocol stacks in bulk.
- It exercises much of the rest of the list at once: open analog front ends, an open eFPGA, partial hardening and connectivity PHYs.

## State of the art

- SDR software: GNU Radio, srsRAN and OpenAirInterface (LTE and 5G), and many open LoRa, Bluetooth LE and 802.11 implementations in software.
- FPGA basebands: openwifi (802.11 on Xilinx Zynq with AD9361), LiteX- and Migen-based SDR gateware, and vendor RFSoC reference designs.
- Open silicon: a few RF and wireless blocks on SKY130 and GF180MCU through open shuttles, but no complete open radio; RF front ends and PLLs are largely missing from open PDK libraries.

## Open questions

- Which standard first: LoRa and NFC are simplest, Bluetooth LE has the widest reach, WiFi and cellular are the hardest.
- Where to split hard, eFPGA and software for each standard, and what fabric size the baseband needs.
- Which open PDKs can support usable RF front ends, and at what frequencies.
- How regulatory certification and conformance testing work for an open design.

## Sources

TODO: create a publicly shareable version of Tim's "Enabling fully open source wireless stack on open source PDKs" presentation and link it here.

## Where it sits

Layer: **IP**. Function: **interface**. Target: **ASIC and FPGA**. Interface IP: the deck's wireless "uncore", with analog RF front ends and a flexible eFPGA and software baseband.

## Related items

- [open-fabric](open-fabric.md) (Fully open FPGA and eFPGA): The eFPGA holds the reprogrammable baseband.
- [hard-core](hard-core.md) (Partial hardening: ASIC core plus eFPGA and software): Same hard, eFPGA and software split, applied to radios.
- [open-links](open-links.md) (Open high-speed connectivity IP): Shares PHY, SerDes and PLL building blocks.
- [shadow-pdks](shadow-pdks.md) (Open "almost manufacturable" PDKs): RF front ends are built per PDK; see also the analog generators candidate.
- [shuttle-program](shuttle-program.md) (Open MPW tapeout programs): Shuttles prove RF front ends in silicon.
