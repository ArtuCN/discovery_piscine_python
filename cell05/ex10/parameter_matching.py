#!/usr/bin/env python3

import sys

if (len(sys.argv) != 2):
	print("none")
	exit()

string = input("What was the paramater: ")
if (string == sys.argv[1]):
	print("Good job!")
else:
	print("Nope... sorry!")