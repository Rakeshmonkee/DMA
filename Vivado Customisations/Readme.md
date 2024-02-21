## Automatically generate and customise ip core for pcileech-fpga-4.14/PCIeSquirrel

This is just something I made in 20 mins for fun. Not really a purpose to use but use it if you want.

> [!NOTE]
> You will need to go into each file and change the file location to the dir of your project
>
> You will need to comment/uncomment the customisations you want
> 
> This doesn't create the .bin file. you will need to open the xpr file in /PCIeSquirrel/pcileech_squirrel and generate the file within Vivado by pressing Generate Bitstream, or Synthesis.

##### List of possible customisations as of now
- Device ID
- Vendor ID
- Subsystem ID
- Subsystem Vendor ID
- Revision ID

##### Soon to come
- Class Code
- Header Type
- Int Pin
- Bars
- Base Ptrs (MSI/MSIx/Header0/PMC/PCIe)
- Next Ptrs (MSI/MSIx/Header0/PMC/PCIe)

## Steps:
1. Make sure Python and Xilinx Vivado is installed on your OS
   
2. Download the project
   
3. Leave all 3 files in the same directory
   
4. Run the `generate-project.py` until the IP core is generated. Depending on your PC specs, this might be fast or slow. To check go to `pcileech-fpga-4.14/PCIeSquirrel/pcileech_squirrel/pcileech_squirrel.srcs/sources_1/ip/pcie_7x_0`.

You can stop the `generate-project.py` file if you can see this directory. If you don't see this directory, let the IP core generate.

5. Run `Vivado.py`

Once Vivado.py has finished running. You can go to this directory `PCIeSquirrel/pcileech_squirrel/pcileech_squirrel.srcs/sources_1/ip/pcie_7x_0/source/` and open the `pcie_7x_0_core_top.v` to see if your customisations have been changed. 



