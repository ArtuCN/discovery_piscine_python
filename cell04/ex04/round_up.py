#!/usr/bin/env python3

num = input("Give me a number: ")
try:
	num = float(num)
except ValueError:
	print("Please enter a number")
	exit()
if num%1 == 0:
	print(int(num))
else:
	print(int(num + 1))