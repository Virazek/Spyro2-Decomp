# Spyro2-Decomp
Disassembly of Spyro 2


This is a reverse-engineering project for 'Spyro 2: Ripto's Rage!' for the Sony PlayStation.

The 'ghidra' directory is a Ghidra project disassembling the main executable (SCUS_944.25) for the USA version of the game.



## Ghidra Label Naming Convention
All label names are in ALL_CAPS_WITH_UNDERSCORES_SEPARATING_WORDS.
Functions do not have any other convention besides that.
Other values are named corresponding to how they are treated when they are loaded into RAM:
- 'DRAM' is 'data RAM'; this value is used solely as a data source
- 'WRAM' is 'working RAM'; this is a value actively written to in order to track state during gameplay
- 'SRAM' is 'save RAM'; this is a value used to store save data state that should be tracked across multiple play sessions
- Labels prefixed with '?' are questionable to their purpose, but are otherwise named with our best guess as to what they are for.