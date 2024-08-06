#!/usr/bin/env python3

import sys

def downcase_all(s):
	return s.lower()

def main():
	if (len(sys.argv) < 2):
		print("none")
		return
	for i in range(1, len(sys.argv)):
		print(downcase_all(sys.argv[i]))

if __name__ == "__main__":
	main()