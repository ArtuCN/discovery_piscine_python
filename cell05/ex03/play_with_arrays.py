#!/usr/bin/env python3

def add_two(array):
	i = 0

	while i < len(array):
		if (array[i] > 5):
			array[i] += 2
		i += 1
	new = [num for num in array if num >= 5]
	return new

array = [4, 42, 88, 69, 13, -69, 10, 42]
print(array)

array = add_two(array)

seen=set()

array = [x for x in array if not (x in seen or seen.add(x))]

print(array)