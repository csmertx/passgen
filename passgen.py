#!/usr/bin/env python

######################################################################
# passgen is a relatively strong password generator
# Copyright (C) 2020 csmertx@null.net
######################################################################
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
######################################################################

# Uses: Example below
# python3 /path/passgen.py 20
# Tested with: Ubuntu, Arch Linux, and Windows 10
# For 'best practice' guidelines search 'digital identity' via nist.gov/publications

import os
import sys
import argparse
import random
from io import StringIO

# vfile = a 'virtual file'
vfile = StringIO()

# Fetch password length from cmd line
charnum = (sys.argv[1])
charnum2 = int(charnum) + 1

## Array: ~1234567890-=qwertyuiop[]asdfghjkl;zxcvbnm,./`!@#$%^&*()_+QWERTYUIOP{}|ASDFGHJKL:"ZXCVBNM<>? (92)
passchars = [ '~', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '-', '=', 'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', '[', ']', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', ';', 'z', 'x', 'c', 'v', 'b', 'n', 'm', ',', '.', '/', '`', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+', 'Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', '{', '}', '|', 'A', 'S', 'D', 'F', 'G', 'J', ',', 'K', 'L', ':', '"', 'Z', 'X', 'C', 'V', 'B', 'N', 'M', '<', '>', '?' ]

# Shuffle the array a few times
random.shuffle(passchars)
random.shuffle(passchars)
random.shuffle(passchars)

# Write to vfile and print to stdout
for x in range(1, int(charnum2)):
    for y in range(1):
        rannum = random.randint(0,91)
    vfile.write(passchars[rannum])
readout = vfile.getvalue()
print(readout)

# Clear and close out buffers
readout = vfile.write(' ')
vfile.close()
passchars = [ ' ' ]
charnum = 1
charnum2 = 1
