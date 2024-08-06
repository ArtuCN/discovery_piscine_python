#!/usr/bin/env python3

import sys

def shrink(s):
	return s[:8]

def enlarge(s):
	return s + (8 - len(s)) * "z"


def main():
	if (len(sys.argv) < 2):
		print("none")
		return
	for i in range(1, len(sys.argv)):
		if len(sys.argv[i]) > 8:
			print(shrink(sys.argv[i]))
		else:
			print(enlarge(sys.argv[i]))

if __name__ == "__main__":
	main()