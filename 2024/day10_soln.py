from utils import read_raw_input

with open(read_raw_input("day10"), 'r') as f:
    rawinput = f.read().split("\n")

all_map = {}
all_start_pos = set()

for i, row in enumerate(rawinput):
    for j, val in enumerate(row):
        val = int(val)
        all_map[(i, j)] = val
        if val == 0:
            all_start_pos.add((i, j))


directions = [
    (1, 0), 
    (-1, 0), 
    (0, -1), 
    (0, 1)
    ]

target = 9
meet_target_count = 0

def DFS_explore(pos, all_map, visited):

    global meet_target_count
    cur_value = all_map[pos]

    if cur_value == target:
        meet_target_count += 1
        return

    for d_horizontal, d_vertical in directions:
        next_pos = (pos[0] + d_horizontal, pos[1] + d_vertical)

        if next_pos in all_map and next_pos not in visited:
            if all_map[next_pos] == cur_value + 1:
                visited.add(next_pos)
                DFS_explore(next_pos, all_map, visited)


for start_pos in all_start_pos:
    visited = set()
    DFS_explore(start_pos, all_map, visited)

print(meet_target_count)
