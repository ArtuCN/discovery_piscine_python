#!/usr/bin/env python3

def famous_births(scientists):
	for key, info in scientists.items():
		name = info["name"]
		date_of_birth = info["date_of_birth"]
		print(f"{name} is a great scientist born in {date_of_birth}.")
def	main():
	women_scientists = {
		"ada": { "name": "Ada Lovelace", "date_of_birth": "1815" },
		"cecilia": { "name": "Cecila Payne", "date_of_birth": "1900" },
		"lise": { "name": "Lise Meitner", "date_of_birth": "1878" },
		"grace": { "name": "Grace Hopper", "date_of_birth": "1906" }
	}
	famous_births(women_scientists)
		
if __name__ == '__main__':
	main()
