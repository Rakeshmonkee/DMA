#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Script: TeleScan PE PCIE config space '.tlscan' to Vivado '.coe' file converter.

Args:
    1) source '.tlscan' file path.
    2) destination '.coe` file path.

Format:
https://docs.xilinx.com/r/en-US/ug896-vivado-ip/Using-a-COE-File
"""
import os
import sys
import datetime
import xml.etree.ElementTree


assert len(sys.argv) >= 2, 'Missing argument'
src_path = os.path.normpath(sys.argv[1])
dst_path = os.path.normpath(os.path.expanduser("~/Desktop") + "/output.coe")

# Load and parse the XML format '.tlscan' file
bs = xml.etree.ElementTree.parse(str(src_path)).find('.//bytes').text
# Make one 8,192 char long hex bytes string
bs = ''.join(bs.split())
assert len(bs) == 8192, f'Expected 8912 character (4096 hex byte) string, got {len(bs):,}!'

# Write out ".coe" file
with open(dst_path, 'w') as fp:
    fp.write(f'\n; Converted to COE from "{src_path}" on {datetime.datetime.now()}\n')
    fp.write('memory_initialization_radix=16;\nmemory_initialization_vector=\n')

    for y in range(16):
        fp.write(f'\n; {(y * 256):04X}\n')

        for x in range(16):
            fp.write(f'{bs[0:8]},{bs[8:16]},{bs[16:24]},{bs[24:32]},\n')
            bs = bs[32:]

    fp.write(';\n')
