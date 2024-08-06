#!/usr/bin/env python3

text = input()

i = 0
res = []

while i < len(text):
	char = text[i]
	if char.isupper():
		res.append(char.lower())
	elif char.islower():
		res.append(char.upper())
	else:
		res.append(char)
	i += 1
print("".join(res))