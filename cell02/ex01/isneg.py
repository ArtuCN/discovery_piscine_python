#!/usr/bin/env python3
num = input()
try:
	num = float(num)
	if num < 0:
		print("This number is negative.")
	if num > 0:
		print("This number is positive.")
	if num == 0:
		print("This number is both negative and positive.")
except:
	print("This is not a number.")
