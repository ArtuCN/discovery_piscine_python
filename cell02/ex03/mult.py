#!/usr/bin/env python3
num1 = input("Enter the first number: ")
try:
	num1 = float(num1)
except:
	print("Invalid input for the first number.")
	exit()
num2 = input("Enter the second number: ")
try:
	num2 = float(num2)
except:
	print("Invalid input for the second number.")
	exit()

num3 = num1 * num2
if num3 < 0:
	print("The product of these numbers is negative.")
elif num3 > 0:
	print("The product of these numbers is positive.")
else:
	print("The product of these numbers is both negative and positive.")
