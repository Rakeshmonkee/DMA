import requests
import subprocess
import os
import shutil
import tempfile
import time
import threading
import re
import random
from colorama import Fore, init, Back, Style
init(convert=True)
os.system("mode 100, 70")
os.system("cls")



replacement_file_prefix = 'directory of replacement files'

vivado_path = "directory of vivado.bat E.G. D:/Xilinx/Vivado/2023.2/bin/vivado.bat"

def Generate():

    replacement_files = {
        """Dict containing the files within pcileech-FPGA you want to replace"""
        """Example:"""
        'IP/pcileech_bar_zero4k.coe': replacement_file_prefix + '/example/pcileech_bar_zero4k.coe',
        'src/pcileech_pcie_cfg_a7.sv': replacement_file_prefix + '/example/pcileech_pcie_cfg_a7.sv'
    }

    # Tcl script paths
    tcl_script_name = "example.tcl"

    generatebitstream_tcl_name = "generatebitstream.tcl"

    script_dir = os.path.dirname(os.path.abspath(__file__))
    tcl_script_path = os.path.join(script_dir, tcl_script_name)
    generatebitstream_tcl_path = os.path.join(script_dir, generatebitstream_tcl_name)

    # Last replacement files after running Tcl script
    last_replacement_files = {
        'pcileech_squirrel/pcileech_squirrel.srcs/sources_1/ip/pcie_7x_0/source/pcie_7x_0_core_top.v': replacement_file_prefix + '/ directory of pcie_7x_0_core_top.v to replace'
    }

    def generate_random_hex_string(length=8):
        return ''.join(random.choices('0123456789ABCDEF', k=length))

    # Function to replace files if directory exists if the
    # path exists, it will replace the file with the last_replacement_files
    def replace_file_if_directory_exists(working_dir, directory_path, replacement_files, vivado_path,
                                         generatebitstream_tcl_path):
        while True:
            target_dir = os.path.join(working_dir, directory_path)
            if os.path.exists(target_dir):
                for relative_path, replacement_path in replacement_files.items():
                    target_path = os.path.join(working_dir, relative_path)
                    if os.path.exists(target_path):
                        os.remove(target_path)
                    shutil.copyfile(replacement_path, target_path)
                print(Fore.LIGHTGREEN_EX + "Successfully replaced the file in the directory.")
                print(Style.RESET_ALL)
                working_dir_with_squirrel = os.path.join(working_dir, 'pcileech_squirrel')
                bin_thread = threading.Thread(target=checkbin, args=(working_dir_with_squirrel,))
                bin_thread.start()

                generate_bitstream(vivado_path, working_dir_with_squirrel, generatebitstream_tcl_path)

            time.sleep(5)  # Sleep to avoid busy-waiting

    def checkbin(working_dir):
        bin_file = os.path.join(r"", working_dir, r"pcileech_squirrel.runs", r"impl_1", r"pcileech_squirrel_top.bin")
        while not os.path.isfile(bin_file):
            """file doesn't exist"""

        print(Fore.LIGHTGREEN_EX + "File exists")
        print(Style.RESET_ALL)


    def download_and_extract_repo(url, temp_dir):
        zip_path = os.path.join(temp_dir, 'repo.zip')

        response = requests.get(url)
        with open(zip_path, 'wb') as file:
            file.write(response.content)

        extracted_dir = os.path.join(temp_dir, 'extracted')
        shutil.unpack_archive(zip_path, extracted_dir)

        source_dir = os.path.join(extracted_dir, 'pcileech-fpga-4.15', 'PCIeSquirrel')
        dest_dir = os.path.join(temp_dir, 'PCIeSquirrel')
        shutil.move(source_dir, dest_dir)

        for item in os.listdir(extracted_dir):
            if item != 'PCIeSquirrel':
                shutil.rmtree(os.path.join(extracted_dir, item))

        return dest_dir

    def replace_files(base_dir, replacements):
        for relative_path, replacement_path in replacements.items():
            target_path = os.path.join(base_dir, relative_path)
            target_dir = os.path.dirname(target_path)
            os.makedirs(target_dir, exist_ok=True)
            shutil.copyfile(replacement_path, target_path)

    def edit_file(file_path):
        with open(file_path, 'r') as file:
            content = file.readlines()

        pattern = r'^\s*rw\[127:64\]'
        replacement_hex = "64'h00000000" + generate_random_hex_string(8)

        for i, line in enumerate(content):
            if re.search(pattern, line):
                content[i] = re.sub(r'64\'h[0-9A-Fa-f]{16}', replacement_hex, line)

        with open(file_path, 'w') as file:
            file.writelines(content)

    def run_vivado(vivado_path, working_dir, tcl_file, generatebitstream_tcl_path):
        thread = threading.Thread(target=replace_file_if_directory_exists, args=(
        working_dir, 'pcileech_squirrel/pcileech_squirrel.srcs/sources_1/ip/pcie_7x_0/source', last_replacement_files,
        vivado_path, generatebitstream_tcl_path))
        thread.start()

        subprocess.run([vivado_path, '-mode', 'tcl', '-source', tcl_file], cwd=working_dir)

        thread.join()

    def generate_bitstream(vivado_path, working_dir, tcl_file):
        subprocess.run([vivado_path, '-mode', 'tcl', '-source', tcl_file], cwd=working_dir)

    with tempfile.TemporaryDirectory() as temp_dir:
        repo_dir = download_and_extract_repo(
            'https://github.com/ufrisk/pcileech-fpga/archive/refs/tags/v4.15.zip', temp_dir)

        replace_files(repo_dir, replacement_files)
        edit_file(os.path.join(repo_dir, 'src/pcileech_pcie_cfg_a7.sv'))

        run_vivado(vivado_path, repo_dir, tcl_script_path, generatebitstream_tcl_path)


Generate()