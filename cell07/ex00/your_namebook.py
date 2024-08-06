#!/usr/bin/env python3

def full_of_names(persons):
	full_names = []
	for first_name, last_name in persons.items():
		full_name = f"{first_name.capitalize()} {last_name.capitalize()}"
		full_names.append(full_name)
	return full_names

def main():
	persons = {
        "jean": "valjean",
        "grace": "hopper",
        "xavier": "niel",
        "fifi": "brindacier"
    }
	print(full_of_names(persons))

if __name__ == '__main__':
	main()