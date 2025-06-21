# Automatic Firmware Creation

Parts of this part have been redacted to ensure people who paste firmware cannot abuse this script. Those who have used Vivado and its TCL commands within Vivado will know what goes where. It's pretty simple. HINT: You can get all the commands from within the terminal in Vivado while generating the core and bitstream. TCL is needed to create the firmware with vivado.bat. I'm not telling which and where the commands are supposed to go. It's your job to learn 💖

To those who think the script is useless, you are correct. It is useless as is. It is your job to create and modify the TCL files to your firmware specifics, the same as the files that are being replaced. Once you get the TCL files completed, the script is no longer useless. See the examples of the TCL scripts below (NOTE: SOME COMMANDS IN THE EXAMPLES ARE MISSING).

This video showcases what happens when everything is working.

https://youtu.be/qU3CvEFWHAA

TCL scripts and files being replaced are configured to my firmware (Sound Card). If you want to create NIC firmware, you will need to change the `tcl_script_name` Script, and the files that are being replaced.



Parts to do yourself:
- generatebitstream_tcl_name TCL file
- tcl_script_name TCL file
- Replacement files


## Requirements
1. Python 3.13
  - requests
  - colorama 
2. Xilinx Vivado


## project.py

``` py
replacement_file_prefix
vivado_path
tcl_script_name
generatebitstream_tcl_name
last_replacement_files
```

replacement_file_prefix is the directory where the files you want to replace are in either /IP or /src sit

vivado_path is the directory where Xilinx Vivado is installed. Link the directory where `vivado.bat` is, which is in `Xilinx/Vivado/2023.2/bin/`. 
E.G `D:/Xilinx/Vivado/2023.2/bin/vivado.bat`

tcl_script_name and generatebitstream_tcl_name are the directories where the TCL script will be 

last_replacement_files is the directory where the last replacement file will be, which will be the core_top.v file.

## tcl_script_name
#### Example TCL script
```
source vivado_generate_project.tcl -notrace

set_property -dict [list \
.....
] [get_ips pcie_7x_0]

generate_target {all} [get_files pcie_7x_0.xci]
```


## generatebitstream_tcl_name
#### Example TCL script
```
open_project xpr file name

update_compile_order -fileset sources_1
```
