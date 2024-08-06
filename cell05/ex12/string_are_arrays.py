#!/usr/bin/env python3

import sys
import re

if (len(sys.argv) != 2):
	print("none")
	exit()


string = ''.join(re.findall('z', sys.argv[1]))
print(string)