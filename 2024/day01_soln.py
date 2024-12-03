
import os
from collections import Counter, defaultdict

input_path = os.getcwd() + "/2024/day01/input.in"

with open(input_path, 'r') as f:
    l1, l2 = [], []
    for line in f.read().splitlines():
        elements = line.split()
        l1.append(int(elements[0]))
        l2.append(int(elements[1]))
    
# part 1
l1.sort()
l2.sort()
result = 0
for i, j in zip(l1, l2):
    result += abs(i-j)
print("Part 1:", result)

# part 2
sim_scores = defaultdict(int)
for i in l1:
    count = 0
    for j in l2:
        if i == j:
            count += 1
    sim_scores[i] += i * count
print("Part 2:", sum(sim_scores.values()))
    

# more efficient part 2
l2_counts = Counter(l2) # O(n)
# https://stackoverflow.com/questions/42461840/what-is-the-time-complexity-of-collections-counter-in-python

sim_scores = defaultdict(int)
for i in l1:
    if i in l2_counts: 
        sim_scores[i] += i * l2_counts[i]
print("Part 2 efficient:", sum(sim_scores.values()))
