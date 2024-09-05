# Creation of Anti-cheese Firmware

> [!NOTE]
> It is assumed the person following this guide knows how to use vivado and get values from their donor board. This is not a guide on how to use vivado and how to get values from a donor board

The steps below will be done to bypass some Anti-Cheeses at a basic level and will be in the [FW Customisations list for some Anti-Cheeses](https://github.com/Rakeshmonkee/DMA/blob/main/EAC-BE%20FW%20Creation/EAC-BE%20FW%20Customisations). You might have also seen this list in the [Possible Vivado Customisations](https://github.com/Silverr12/DMA-CFW-Guide/blob/main/Possible%20Vivado%20Customisations.md) list I made in the [DMA-CFW-Guide](https://github.com/Silverr12/DMA-CFW-Guide/tree/main) which I contributed to. 

To bypass some Anti-Cheeses at a moderate level you should change a few more values around within the config space and implement Bar Emulation to successfully load the driver of the device you are trying to mimic which can be found [here](https://github.com/Rakeshmonkee/DMA/tree/main/Bar%20Emulation). otherwise, you will most likely see a yellow icon next to the device in Device Manager.

For a high-level bypass, use TLP Emulation

You can be assured after you follow the basic steps, you will last a while on any some Anti-Cheeses game considering you don't rage cheat and be blatant about cheating. I personally have done the basic step as a test and have lasted over 1 month, no Anti-Cheeses ban but I did receive 1 temp ban for 7 days during the process which was most likely done manually by the server admin because I got too many reports. I got this temp ban because I was too blatant. The game will not be mentioned, but it does use an very well known Anti-Cheese. All I can suggest is, don't be blatant about cheating

By changing these values to match your donor board, you can bypass some Anti-Cheeses at a basic level. You don't need to go into the Core Top file and change PTRS/NEXT PTRS around. You could maybe even bypass Ricochet AC and maybe even Electronic Arts Anti Cheat. I am not sure about those 2 and have not tested them.

Steps:
1. Change DSN value[215], master abort flag[209], and bus master[210] in `/PCIeSquirrel/src/pcileech_pcie_cfg_a7.sv` [xx] being the line
2. Generate the pcileech IP core
3. Under the basic tab in the `Re-Customise IP` UI, set the Mode to `Advanced`

Everything I mention here is what to change to match your donor board

Basic Tab:
- Number of Lanes
- Maximum Link Speed

IDs Tab:
- Vendor ID
- Device ID
- Revision ID
- Subsystem Vendor ID
- Subsystem ID

- Base Class Menu/Value
- Sub Class Interface Menu/Value
- Interface Value
- Cardbus CIS Pointer

Bars Tab:

Will need to look at your donor board to see how many bars to enable
- Size Unit
- Size Value
- 64 bit
- Prefetchable

Core Capabilities Tab:

Try to match the Device Capabilities Register Hex to match the hex on your donor board
- Max Payload Size
- Extended Tag Field
- Extended Tag Default
- Phantom Functions
- Acceptable L0s Latency
- Acceptable L1 Latency

Link Registers Tab:
- ASPM Optionality
- DLL Link Active Reporting Capability
- Target Link Speeds
- Slot Clock Configuration

Interrupts Tab:
- Interrupt Pin
- MSI Capability Struct
- 64-bit address Capable
- Per Vector Masking Capable
- Multiple Message Capable
- MSIx Capability Struct

Power Management Tab:
- Device Specific Initialisation
- D1 Support
- D2 Support
- PME Support

EXT Capabilities Tab:
- DSN Capability
- VC Capability
- VSEC Capability
- User Defined Configuration Capabilities

EXT Capabilities 2 Tab:
- AER
