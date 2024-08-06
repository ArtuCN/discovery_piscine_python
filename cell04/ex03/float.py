#!/usr/bin/env python3

num = input("Give me a number: ")
try:
	num = float(num)
except ValueError:
	print("Please enter a number")
	exit()
if num%1 == 0:
	print("This number is an integer")
else:
	print("This number is a decimal")