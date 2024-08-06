#!/usr/bin/env python3

import sys
if len(sys.argv) >= 2:
	print("none")
	sys.exit(1)
i = 0
num = 0

while i <= 10:
    results = []
    num = 0
    while num <= 10:
        results.append(str(i * num))
        num += 1
    result_str = " ".join(results)
    print(f"Table de {i}: {result_str}")
    i += 1
