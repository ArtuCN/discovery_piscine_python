#!/usr/bin/env python3

import sys

if len(sys.argv) == 1:
	print("none")
	exit()

sys.argv.reverse()

i = 0

while i + 1 < len(sys.argv):
	print(sys.argv[i])
	i += 1