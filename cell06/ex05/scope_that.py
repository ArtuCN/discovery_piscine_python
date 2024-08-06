#!/usr/bin/env python3

def adds_one(x):
	x += 1
	return(x)

def main():
	x = 0
	print(f"x before adds_one: {x}")
	x2 = adds_one(x)
	print(f"x after adds_one: {x}")
	print(f"x2 after adds_one: {x2}")

if __name__ == "__main__":
	main()