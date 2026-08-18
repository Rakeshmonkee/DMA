## DMA Firmware, Flashing, trouble-shooting Guide.

DMA (Direct Memory Access) is a mechanism that allows a hardware device to directly read from or write to system memory without requiring the CPU to perform each individual memory transfer. DMA is commonly used by legitimate hardware such as network cards, storage controllers, and GPUs to efficiently transfer data between the device and system memory. DMA used to and still is actively being abused in video games to bypass anti-cheat systems with the sole purpose to cheat. By having a specialised DMA card to conduct the DMA operation powered by the Firmware on the FPGA (Field Programmable Gate Array), the card disguises itself as legitimate PCIE devices to look like a real device to the computer and anti-cheat. By connecting to the PCIe bus, the DMA card can directly access system memory without needing the CPU to execute instructions to read from or write to a memory address, which anti-cheat systems may attempt to detect using various heuristic techniques.

The original goal of this repository was to make custom DMA firmware more accessible and affordable. Over time, however, its purpose has evolved into a resource for helping users troubleshoot issues with their DMA card.




> [!WARNING]
> 
> This guide has been specifically created for educational purposes to provide valuable information and insights to help users understand anything todo with DMA, Firmware creation, Flashing, and Trouble-shooting
> 


> [!IMPORTANT]
> 
> This guide is not a spoon feed. I have purposely left out some information. It is your job to make FW while learning something.
> 


### Contents
- [Automatic Firmware Creation](https://github.com/Rakeshmonkee/DMA/tree/main/Automatic%20Firmware%20Creation)
- [Vivado Customisations](https://github.com/Rakeshmonkee/DMA/tree/main/Vivado%20Customisations)
- [DMA FAQ](https://github.com/Rakeshmonkee/DMA/blob/main/DMA%20FAQ.md)
- [How to Flash](https://github.com/Rakeshmonkee/DMA/tree/main/How%20to%20Flash)
- [Anti-Cheese FW Creation](https://github.com/Rakeshmonkee/DMA/tree/main/Anti-Cheese%20FW%20Creation)
- [VGK FW Creation](https://github.com/Rakeshmonkee/DMA/tree/main/VGK%20FW%20Creation)
- [TLSCAN to COE](https://github.com/Rakeshmonkee/DMA/tree/main/.tlscan%20to%20.coe)
- [1:1 CFG of real device](https://github.com/Rakeshmonkee/DMA/tree/main/1%3A1%20CFG%20of%20real%20device)
- [DMA Troubleshooting](https://github.com/Rakeshmonkee/DMA/tree/main/DMA%20Troubleshooting)

#### If you have any questions or problems/issues, feel free to join my discord server and ask in one of the channels that best suits your issue.

[![Discord Banner](https://discord.com/api/guilds/1201428101964513300/widget.png?style=banner2)](https://discord.gg/4kSWZsexvq)

------------------------
# Disclaimer:

The content of this post is intended for educational and informational purposes only. Any references to anti-cheat software, including but not limited to descriptions, functionalities, or general characteristics, are made in the context of promoting security awareness and understanding within the software development community. This post does not endorse or promote any actions that would violate the terms of service of any software or service.

All trademarks, service marks, and company names are the property of their respective owners. The use of these names, logos, and brands is for identification purposes only and does not imply endorsement. If you represent a company and believe this post infringes on your intellectual property, please contact me, and I will take appropriate action.



