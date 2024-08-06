#!/usr/bin/env python3
num = input()
try:
	num = float(num)
	if num == 0:
		print("This number is equal to zero.")
	else:
		print("This number is different from zero.")
except:
	print("This is not a number.")
