#!/usr/bin/env python3

age = (input("How old are you? "))
try:
	age = int(age)
except:
	print("Please enter a number")
	exit()
print(f"You are currently {age} years old.")
print(f"In 10 years you will be {age + 10} years old.")
print(f"In 20 years you will be {age + 20} years old.")
print(f"In 30 years you will be {age + 30} years old.")
