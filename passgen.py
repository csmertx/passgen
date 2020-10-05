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
# python3 /path/passgen.py 20    # for full QWERTY
# python3 /path/passgen.py 20 -c # for common QWERTY
# Tested with: Ubuntu, Arch Linux, and Windows 10
# For 'best practice' guidelines search 'digital identity' via nist.gov/publications

import os, sys, argparse, getopt, random
from io import StringIO

### vfile = a 'virtual file'
vfile = StringIO()

### Default to Full QWERTY characters
commchar = 0

### Parse user arguments
try:
    opts, args = getopt.getopt(sys.argv[1:], "hc", ["help", "common"])
except getopt.GetoptError as err:
    err = "\n\nInvalid command.  Use --help for valid commands.\n\n"
    print(err)
    usage()
    sys.exit(2)
for o, a in opts:
    if o in ("-h", "--help"):
        print("\npassgen: Quasi secure password generator\n    Usage: -hc, --help, --common, --full\n        -h, --help      Prints this message\n        -c, --common    Use only common QWERTY password characters\n\nExamples:\n    python3 /path/passgen.py 20\n    python3 /path/passgen.py 20 -c\n")
        sys.exit()
    elif o in ("-c", "--common"):
        commchar = 1
    else:
        assert False, "unhandled option"

### Full QWERTY
## Array: ~1234567890-=qwertyuiop[]asdfghjkl;zxcvbnm,./`!@#$%^&*()_+QWERTYUIOP{}|ASDFGHJKL:"ZXCVBNM<>? (92)
passchars = [ '~', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '-', '=', 'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', '[', ']', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', ';', 'z', 'x', 'c', 'v', 'b', 'n', 'm', ',', '.', '/', '`', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+', 'Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', '{', '}', '|', 'A', 'S', 'D', 'F', 'G', 'J', ',', 'K', 'L', ':', '"', 'Z', 'X', 'C', 'V', 'B', 'N', 'M', '<', '>', '?' ]

### Common QWERTY
## Array: 1234567890-=qwertyuiopasdfghjklzxcvbnm./!@#$%*()_QWERTYUIOPASDFGJKLZXCVBNM? (75)
passchars2 = [ '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '-', '=', 'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm', '.', '/', '!', '@', '#', '$', '%', '*', '(', ')', '_', 'Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', 'A', 'S', 'D', 'F', 'G', 'J', 'K', 'L', 'Z', 'X', 'C', 'V', 'B', 'N', 'M', '?' ]

charnum = (sys.argv[1])
charnum1 = int(charnum)

if commchar == 1:
    passchars = passchars2

# Shuffle the array a few times
random.shuffle(passchars)
random.shuffle(passchars)
random.shuffle(passchars)

# Write to vfile and print to stdout
for x in range(1, int(charnum1)):
    for y in range(1):
        if commchar == int(1):
            rannum = random.randint(0,74)
        elif commchar == int(0):
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
