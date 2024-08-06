#!/usr/bin/env python3

import sys

def free_range(num1, num2):
	if num1 > num2:
		return list(range(num2, num1+1))
	return list(range(num1, num2+1))


def main():
	if len(sys.argv) != 3:
		print('none')
		sys.exit(1)
	try:
		num = int(sys.argv[1])
	except ValueError:
		print('Error: Invalid number')
		sys.exit(1)
	try:
		num2 = int(sys.argv[2])
	except ValueError:
		print('Error: Invalid number')
		sys.exit(1)
	print(free_range(num, num2))
		
if __name__ == "__main__":
    main()