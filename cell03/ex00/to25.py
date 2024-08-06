#!/usr/bin/env python3

num = input("Enter a number less than 25: ")
try:
	num = int(num)
except:
	print("This is not a number")
	exit()
if num <= 25:
	while num <= 25:
		print("inside the loop, my varable is: ", num)
		num+=1
else:
	print("Error")
