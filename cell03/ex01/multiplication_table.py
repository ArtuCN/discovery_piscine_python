#!/usr/bin/env python3

num = input()
try:
	num = int(num)
except:
	print("This is not a number")
	exit()
i = 0
while i <= 9:
	print(num, "x", i, "=", num*i)
	i+=1