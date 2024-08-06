#!/usr/bin/env python3

def add_two(num):
	return num + 2

array = [42, 88, 69, 13, 10]
print(array)

i = 0

while i < len(array):
	array[i] = add_two(array[i])
	i += 1

print(array)

