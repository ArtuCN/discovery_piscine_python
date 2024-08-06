#!/usr/bin/env python3

def greetings(name=None):
	if name == None:
		name = "noble stranger"
	elif not isinstance(name, str):
		print("Error it wasn't a name.")
		return
	print(f"Hello {name}.")

if __name__ == "__main__":
	greetings('Alexandra')
	greetings('Will')
	greetings()
	greetings(42)