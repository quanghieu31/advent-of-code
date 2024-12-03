import os
from utils import read_raw_input

with open(read_raw_input("day02"), "r") as f:
    lines = [list(map(int, line.split())) for line in f.read().splitlines()]


### brute force

def check(line):
    diff = [line[i] - line[i-1] for i in range(1, len(line))]

    # first condition
    check_in_de = all(list(map(lambda x: x<0, diff))) or all(list(map(lambda x: x>0, diff)))
    # second condition
    abs_diff = list(map(abs, diff))
    check_too_large = all(list(map(lambda x: x in (1,2,3), abs_diff)))

    return check_in_de and check_too_large

# part 1
safes = 0

# normal check for absolutely safe ones (safes_1)
for line in lines:
    if check(line):
        safes += 1

print("Part 1:", safes)


# part 2
safes_1 = 0
recheck_lines = []
safes_2 = 0

# normal check for absolutely safe ones (safes_1)
for line in lines:
    if check(line):
        safes_1 += 1
    else:
        recheck_lines.append(line)

# recheck the unsafe ones (safes_2_)
for line in recheck_lines: 
    for idx in range(len(line)):

        # ln = line.copy()
        # ln.remove(line[idx])

        ln = line[:idx] + line[idx+1:]
        
        if check(ln):
            safes_2 += 1
            break
            
            
print("Part 2:", safes_1 + safes_2)