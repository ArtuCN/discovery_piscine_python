#!/usr/bin/env python3

user_input = input("What you gotta say? : ")
clear_input = user_input.strip()
while clear_input != "STOP":
	user_input = input("I got that! anything else? : ")
	clear_input = user_input.strip()

