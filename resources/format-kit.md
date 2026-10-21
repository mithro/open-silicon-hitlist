# Libraries for every EDA file format — resources

Loose collection, 2026-10-21. Drive links are publicly shared (anyone with the link).

## Tim's Google Drive (public)
- [Open Source ASIC CAD tooling and file formats relationships - bit.ly/cad-ff](https://docs.google.com/spreadsheets/d/14f1R7LdGAmY7LGJOmKO0c3akV7ctFelNITSxVAIg7Q0/edit?resourcekey=0-D3ZYGrArfwVXDCqjiB2rdg) — which open and proprietary tools read and write which ASIC formats
- [Open Source (FOSS) FPGA (EDA) Tooling Interchange Formats + Toolchain parts](https://docs.google.com/document/d/1DWZ0G8vehkuZTPs5N3AQqIvZZtLMGzC8i0MWPRP54O4/edit) — formats at each FPGA flow stage boundary
- [FPGA Tooling Common Interchange Formats](https://docs.google.com/document/d/1qc-iXMv3XzU21WV1qaQLtx7658nH_xqwIdqNOjR7qQM/edit) — origin of the FPGA Interchange idea
- [SymbiFlow Interchange Format Slides](https://docs.google.com/presentation/d/1Odulf22CnW576RIPK5_x6CcOJw3WHR4THHecVht29HM/edit) — interchange design overview
- [FPGA Interchange - Architectures support and VPR status](https://docs.google.com/spreadsheets/d/1hF7-PpOpa35uik2C2-RYSpY-oFJS2SpbVJj_SF_IAF0/edit) — per-family coverage of one shared format
- [Extend python-fpga-interchange with API to manipulate device resources data](https://docs.google.com/document/d/1JMyMzeEkX5Qhqv1x_HGlGOqQ-byF2lWgv77nwAW6kuQ/edit) — library API work on a format
- [Interchange Format - Macros + Macro Definitions](https://docs.google.com/document/d/1gvY8XSIH48wu04PaZrhsaaUA5-OvpI_jXBeZGNdBtAk/edit) — format extension details
- [FPGA ASM (FASM) File Format Requirements](https://docs.google.com/document/d/13ubzrxcfU0TUVIIRpmZt0aMwaMFm_HsjNlzRK0uvNhI/edit) — designing a bitstream-level text format
- [FASM Database Specification](https://docs.google.com/document/d/1NUVo-k_TYDZvH8EKcL7c-q30rMhPSeVA2DaHzT4zSLE/edit) — bit-to-feature database format
- [SKY130 (SkyWater PDK) -- Layer (GDS-II / Magic / Calibre / etc) Information - (public)](https://docs.google.com/spreadsheets/d/1oL6ldkQdLu-4FEQE0lX6BcgbqzYfNnd1XA8vERe0vpE/edit) — one layer map across many tool formats
- [File naming in open source PDKs - bit.ly/open-source-pdks-naming](https://docs.google.com/document/d/1rDN5jw8sh0aTwf1jScn0nP2zy4FWLxC-82M8TL3Lbr4/edit) — consistent naming for PDK views in many formats
- [(Open Source) PDK Python Tooling - bit.ly/python-pdk](https://docs.google.com/document/d/1VZIpYx0FN1oMd2KW_oWL1gsQbssSM8JEJjRJVLamNI0/edit) — Python access to PDK data files
- [Yosys Timing Annotation support](https://docs.google.com/document/d/1A0ceG2ltz4jttb_KS4tijJrIhxrUcB23V16Sl3StO34/edit) — timing data passing between tools
- [Open Source EDA - Roadmap (Nov 2024)](https://drive.google.com/file/d/1dVIi6BnwZg78IU1jd8Iq7z0UYfAnwBdW/view) — public roadmap (FOSSi et al.) incl. format gaps

## Projects and repositories
- [KLayout](https://github.com/KLayout/klayout) — layout database with GDS, OASIS, LEF/DEF, CIF and DXF readers and writers
- [gdstk](https://github.com/heitzmann/gdstk) — C++/Python GDSII and OASIS library (archived)
- [gdsfactory](https://github.com/gdsfactory/gdsfactory) — Python layout generation on top of GDS libraries
- [OpenROAD](https://github.com/The-OpenROAD-Project/OpenROAD) — OpenDB with LEF/DEF, Verilog and GDS I/O
- [OpenSTA](https://github.com/parallaxsw/OpenSTA) — Liberty, SPEF, SDF and SDC readers
- [Yosys](https://github.com/YosysHQ/yosys) — Verilog, Liberty, BLIF, EDIF and JSON netlist I/O
- [Surelog](https://github.com/chipsalliance/Surelog) and [UHDM](https://github.com/chipsalliance/UHDM) — SystemVerilog parser and a serialised interchange model
- [slang](https://github.com/MikePopoloski/slang) — SystemVerilog compiler and language services
- [Verible](https://github.com/chipsalliance/verible) — SystemVerilog parser, linter and formatter
- [Magic](https://github.com/RTimothyEdwards/magic) and [netgen](https://github.com/RTimothyEdwards/netgen) — layout and SPICE/Verilog netlist handling
- [Xyce](https://github.com/Xyce/Xyce) — SPICE simulator with its own netlist dialect parser
- [spydrnet](https://github.com/byuccl/spydrnet) — EDIF and other netlist parsing and transformation
- [FPGA Interchange schema](https://github.com/chipsalliance/fpga-interchange-schema) and [python-fpga-interchange](https://github.com/chipsalliance/python-fpga-interchange) — Cap'n Proto FPGA netlist and device formats
- [FASM](https://github.com/chipsalliance/fasm) — FPGA assembly parser and generator

## Papers and other reading
- [Kahn and Goldman, "The Electronic Design Interchange Format EDIF: present and future" (DAC 1992)](https://doi.org/10.1109/dac.1992.227802) — history of a shared netlist format
- [Jung et al., "OpenDesign flow database: the infrastructure for VLSI design and design automation research" (ICCAD 2016)](https://doi.org/10.1145/2966986.2980074) — open database with LEF/DEF I/O, the base of OpenDB
- [Lavin and Kaviani, "RapidWright: Enabling Custom Crafted Implementations for FPGAs" (FCCM 2018)](https://doi.org/10.1109/fccm.2018.00030) — access to proprietary FPGA design checkpoints
- [Townsend and Nelson, "Vivado design interface: An export/import capability for Vivado FPGA designs" (FPL 2017)](https://doi.org/10.23919/fpl.2017.8056809) — round-tripping a proprietary tool's netlists
- [Baungarten-Leon, "From RTL to Fabrication: Survey of Open-Source EDA Tools and PDKs" (Electronics, 2026)](https://doi.org/10.3390/electronics15051048) — survey of the tools and formats in open flows
- ["AiEDA: An Open-Source AI-Aided Design Library for Design-to-Vector" (2025)](https://arxiv.org/abs/2511.05823) — unified data extraction from physical design formats
