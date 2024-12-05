from utils import read_raw_input
import os
from re import findall

with open(read_raw_input("day03"), 'r') as f:
    line = f.read()

# brute force

# part 1
nums = findall(r"mul\((\d+),(\d+)\)", line)
results = sum(list(map(lambda x: int(x[0]) * int(x[1]), nums)))
print(results)