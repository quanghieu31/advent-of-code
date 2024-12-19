from utils import read_raw_input
import numpy as np

with open(read_raw_input("day08"), 'r') as f:
    raw = [list(line) for line in f.read().split("\n")]
    grid = np.array(raw)

n_rows, n_cols = grid.shape[0], grid.shape[1]
unique_eles = set([x for l1 in raw for x in l1 if x != "."])

# get all coordinates of all required points
dict_coords = {}
for ele in unique_eles:
    list_coords = []
    for i in range(n_rows):
        for j in range(n_cols):
            if grid[i, j] == ele:
                # first encounter, and break/continue later
                list_coords.append((i, j))
    dict_coords[ele] = list_coords

count = 0

for key, value in dict_coords.items():

    for idx, coord in enumerate(value):
        value_copy = value.copy()
        value_copy.pop(idx)
        
        for other_coord in value_copy:
            d_vertical, d_horizontal = coord[0] - other_coord[0], coord[1] - other_coord[1]
            new_coord = (coord[0] + d_vertical, coord[1] + d_horizontal)
            
            # update grid
            try:
                if 0 <= new_coord[0] <= n_rows and 0 <= new_coord[1] <= n_cols and grid[new_coord] != "#":
                    grid[new_coord] = "#"
                    count += 1
            except IndexError:
                continue

print(count)