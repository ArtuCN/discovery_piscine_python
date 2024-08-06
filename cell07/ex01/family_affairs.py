#!/usr/bin/env python3

def find_the_redheads(family):
	redhead = []
	for name, hair_color in family.items():
		if hair_color == "red":
			redhead.append(name)
	return redhead


def main():
	family = {
	"florian": "red",
	"marie": "blond",
	"virginie": "brunette",
	"david": "red",
	"franck": "red"
	}
	print((find_the_redheads(family)))

if __name__ == '__main__':
	main()