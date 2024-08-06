#!/usr/bin/env python3

num1 = input("Give me the first number: ")
try:
	num1 = int(num1)
except:
	print("Please enter a number")
	exit()
num2 = input("Give me the second number: ")
try:
	num2 = int(num2)
except:
	print("Please enter a number")
	exit()
print(f"{num1} + {num2} = {num1 + num2}")
print(f"{num1} - {num2} = {num1 - num2}")
if num2 == 0:
	print("Cannot divide by zero")
else:
	print(f"{num1} / {num2} = {num1 / num2}")
print(f"{num1} * {num2} = {num1 * num2}")
