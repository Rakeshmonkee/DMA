# Automatic Firmware Creation

## Requirements
1. Python 3.13
  - requests
  - colorama 
2. Xilinx Vivado


Parts of this part have been redacted to ensure people who paste firmware cannot abuse this script. Those who have used Vivado and its TCL commands within Vivado will know what goes where. It's pretty simple. HINT: You can get all the commands from within the terminal in Vivado while generating the core and bitstream. TCL is needed to create the firmware with vivado.bat. I'm not telling which and where the commands are supposed to go. It's your job to learn 💖

To those who think the script is useless, you are correct. It is useless as is. It is your job to create and modify the TCL files to your firmware specifics, the same as the files that are being replaced. Once you get the TCL files completed, the script is no longer useless. See the examples of the TCL scripts below (NOTE: SOME COMMANDS IN THE EXAMPLES ARE MISSING. AGAIN, YOUR JOB TO DO THIS PART).

This video showcases what happens when everything is working.

https://youtu.be/qU3CvEFWHAA

### Scripts used in video

```tcl
Soundcard.tcl
35tgeneratebitstream.tcl
```

### Files replaced in video

```python
pcie_7x_0_core_top.v
pcileech_bar_zero4k.coe
pcileech_cfgspace.coe
pcileech_fifo.sv
pcileech_pcie_a7.sv
pcileech_pcie_cfg_a7.sv

------------------------------------------------------------------------

replacement_files = {
    'IP/pcileech_bar_zero4k.coe': replacement_file_prefix + '/SoundCard/pcileech_bar_zero4k.coe',
    'IP/pcileech_cfgspace.coe': replacement_file_prefix + '/SoundCard/pcileech_cfgspace.coe',
    'src/pcileech_fifo.sv': replacement_file_prefix + '/SoundCard/pcileech_fifo.sv',
    'src/pcileech_pcie_cfg_a7.sv': replacement_file_prefix + '/SoundCard/pcileech_pcie_cfg_a7.sv',
    'src/pcileech_pcie_a7.sv': replacement_file_prefix + '/SoundCard/pcileech_pcie_a7.sv'
}


last_replacement_files = {
    'pcileech_squirrel/pcileech_squirrel.srcs/sources_1/ip/pcie_7x_0/source/pcie_7x_0_core_top.v': replacement_file_prefix + '/SoundCard/pcie_7x_0_core_top.v'
}
```
Replace the original files with your updated ones configured to the firmware you want to make

Example:

Original pcileech_cfgspace.coe

```python
memory_initialization_radix=16;
memory_initialization_vector=

fffff000,fffff004,fffff008,fffff00c,
fffff010,fffff014,fffff018,fffff01c,
fffff020,fffff024,fffff028,fffff02c,
fffff030,fffff034,fffff038,fffff03c,
fffff040,fffff044,fffff048,fffff04c,
fffff050,fffff054,fffff058,fffff05c,
fffff060,fffff064,fffff068,fffff06c,
fffff070,fffff074,fffff078,fffff07c,
fffff080,fffff084,fffff088,fffff08c,
fffff090,fffff094,fffff098,fffff09c,
fffff0a0,fffff0a4,fffff0a8,fffff0ac,
fffff0b0,fffff0b4,fffff0b8,fffff0bc,
fffff0c0,fffff0c4,fffff0c8,fffff0cc,
fffff0d0,fffff0d4,fffff0d8,fffff0dc,
fffff0e0,fffff0e4,fffff0e8,fffff0ec,
fffff0f0,fffff0f4,fffff0f8,fffff0fc,
```
<br>

When replacing the original with your updated pcileech_cfgspace.coe

```python
memory_initialization_radix=16;
memory_initialization_vector=

02111200,06001000,01000304,10000000,
04c07ffc,00000000,04807ffc,00000000,
00000000,00000000,00000000,02111000,
00000000,40000000,00000000,18010000,
01500304,08000000,00000000,00000000,
05708001,00000000,00000000,00000000,
00000000,00000000,00000000,00000000,
10000200,00802c01,10200000,113c0200,
40001110,00000000,00000000,00000000,
00000000,10000000,10000000,02000000,
00000000,00000000,00000000,00000000,
00000000,00000000,00000000,00000000,
00000000,00000000,00000000,00000000,
00000000,00000000,00000000,00000000,
00000000,00000000,00000000,00000000,
00000000,00000000,00000000,00000000,
```

<br>


TCL scripts and files being replaced are configured to my firmware (Sound Card). If you want to create NIC firmware, you will need to change the `tcl_script_name` Script and the files that are being replaced.

Scripts can be used to make 35t, 75t, 100t, and M.2. You'll need to edit the Python script, and `tcl_script_name` for that part.

```tcl
35t - open_project pcileech_squirrel.xpr
75t - open_project pcileech_enigma_x1.xpr
100t - open_project pcileech_tbx4_100t.xpr
M.2 - open_project pcileech_screamer_m2.xpr
```

### 35T py

```python
tcl_script_name = "SoundCard.tcl"
generatebitstream_tcl_name = "35tgeneratebitstream.tcl"

working_dir_with_squirrel = os.path.join(working_dir, 'pcileech_squirrel')
last_replacement_files = {
    'pcileech_squirrel/pcileech_squirrel.srcs/sources_1/ip/pcie_7x_0/source/pcie_7x_0_core_top.v': replacement_file_prefix + '/SoundCard/pcie_7x_0_core_top.v'
}

bin_file = os.path.join(r"", working_dir, r"pcileech_squirrel.runs", r"impl_1", r"pcileech_squirrel_top.bin")

source_dir = os.path.join(extracted_dir, 'pcileech-fpga-4.15', 'PCIeSquirrel')
dest_dir = os.path.join(temp_dir, 'PCIeSquirrel')

if item != 'PCIeSquirrel':

thread = threading.Thread(target=replace_file_if_directory_exists, args=(
working_dir, 'pcileech_squirrel/pcileech_squirrel.srcs/sources_1/ip/pcie_7x_0/source', last_replacement_files,
vivado_path, generatebitstream_tcl_path))

```





### 75T py

```python
tcl_script_name = "SoundCard.tcl"
generatebitstream_tcl_name = "75tgeneratebitstream.tcl"

working_dir_with_squirrel = os.path.join(working_dir, 'pcileech_enigma_x1')

last_replacement_files = {
    'pcileech_enigma_x1/pcileech_enigma_x1.srcs/sources_1/ip/pcie_7x_0/source/pcie_7x_0_core_top.v': replacement_file_prefix + '/SoundCard/pcie_7x_0_core_top.v'
}

bin_file = os.path.join(r"", working_dir, r"pcileech_enigma_x1.runs", r"impl_1", r"pcileech_enigma_x1_top.bin")

source_dir = os.path.join(extracted_dir, 'pcileech-fpga-4.15', 'EnigmaX1')
dest_dir = os.path.join(temp_dir, 'EnigmaX1')

if item != 'EnigmaX1':

thread = threading.Thread(target=replace_file_if_directory_exists, args=(
working_dir, 'pcileech_enigma_x1/pcileech_enigma_x1.srcs/sources_1/ip/pcie_7x_0/source', last_replacement_files,
vivado_path, generatebitstream_tcl_path))
```


### 100T py

```python
tcl_script_name = "SoundCard_100t.tcl"
generatebitstream_tcl_name = "100tgeneratebitstream.tcl"

working_dir_with_squirrel = os.path.join(working_dir, 'pcileech_tbx4_100t')

last_replacement_files = {
    'pcileech_tbx4_100t/pcileech_tbx4_100t.srcs/sources_1/ip/pcie_7x_0/source/pcie_7x_0_core_top.v': replacement_file_prefix + '/SoundCard/pcie_7x_0_core_top.v'
}

bin_file = os.path.join(r"", working_dir, r"pcileech_tbx4_100t.runs", r"impl_1", r"pcileech_tbx4_100t_top.bin")

source_dir = os.path.join(extracted_dir, 'pcileech-fpga-4.15', 'ZDMA')
dest_dir = os.path.join(temp_dir, 'ZDMA')

if item != 'ZDMA':

thread = threading.Thread(target=replace_file_if_directory_exists, args=(
        working_dir, 'pcileech_tbx4_100t/pcileech_tbx4_100t.srcs/sources_1/ip/pcie_7x_0/source', last_replacement_files,
        vivado_path, generatebitstream_tcl_path))

edit_file(os.path.join(repo_dir, '100T/src/pcileech_pcie_cfg_a7.sv'))
```

### M.2 py
```python
tcl_script_name = "SoundCard.tcl"
generatebitstream_tcl_name = "M.2generatebitstream.tcl"

working_dir_with_squirrel = os.path.join(working_dir, 'pcileech_screamer_m2')

last_replacement_files = {
    'pcileech_screamer_m2/pcileech_screamer_m2.srcs/sources_1/ip/pcie_7x_0/source/pcie_7x_0_core_top.v': replacement_file_prefix + '/SoundCard/DrvRed/pcie_7x_0_core_top.v'
}

bin_file = os.path.join(r"", working_dir, r"pcileech_screamer_m2.runs", r"impl_1", r"pcileech_screamer_m2_top.bin")

source_dir = os.path.join(extracted_dir, 'pcileech-fpga-4.14', 'ScreamerM2')
dest_dir = os.path.join(temp_dir, 'ScreamerM2')

if item != 'ScreamerM2':

thread = threading.Thread(target=replace_file_if_directory_exists, args=(
        working_dir, 'pcileech_screamer_m2/pcileech_screamer_m2.srcs/sources_1/ip/pcie_7x_0/source', last_replacement_files,
        vivado_path, generatebitstream_tcl_path))
```

### Parts to do yourself:
- generatebitstream_tcl_name TCL file
- tcl_script_name TCL file
- Replacement files


## project.py

```python
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
```tcl
source vivado_generate_project.tcl -notrace

set_property -dict [list \
.....
] [get_ips pcie_7x_0]

generate_target {all} [get_files pcie_7x_0.xci]

lock core command here
```


## generatebitstream_tcl_name
#### Example TCL script
```tcl
open_project xpr file name

update_compile_order -fileset sources_1

generate bitstream command here
```
