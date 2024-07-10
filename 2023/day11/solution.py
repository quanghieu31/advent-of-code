####################### Read input ###################################

# read lines
file_path = "2023/day11/input.in"
with open(file_path, "r") as f:
    lines = [list(line.strip()) for line in f.readlines()]

####################### check expand ###################################

# for every col and every row, duplicate to next position
def add_duplicate_no_galaxies(lines, expand=999999):  # expand=1000000-1 for part 2

    expanded_row_lines = []
    # check row
    for line in lines:
        expanded_row_lines.append(line)
        if len(set(line)) == 1:
            for _ in range(expand):
                expanded_row_lines.append(line)
   
    # check columns using transpose of expanded_row_lines
    transposed = zip(*expanded_row_lines) # consequentially pairs
    expanded_transposed = []
    for col in transposed:
        expanded_transposed.append(col)
        if len(set(col)) == 1:
            for _ in range(expand):
                expanded_transposed.append(col)

    # transpose back and convert to list
    expanded_lines = list(map(list, zip(*expanded_transposed)))
    return expanded_lines

# print("\nThe expanded lines/space is:\n", *add_duplicate_no_galaxies(lines), "\n")

############### gridding and preparing #######################################

GridPoint = tuple[int, int]     # a tuple of two integers = cooridinate
Grid = dict[GridPoint, str]     # the keys are GridPoints and the values are strings

def parse_grid(array2d: list[list]) -> Grid:
    grid_dict = {}
    for row, line in enumerate(array2d):
        for col, ele in enumerate(line):
            grid_dict[(row, col)] = ele

    # assign unique_number for galaxy (for this Day puzzle only)
    unique_number = 1
    for k, v in grid_dict.items():
        if v == "#":
            grid_dict[k] = unique_number
            unique_number += 1

    return grid_dict

grid = parse_grid(add_duplicate_no_galaxies(lines))
# print("Grid with coordinate is\n", grid)
# print()


############### find shortest path between each pair ##########################

# combinations (unique matters, ignore duplicates)
from itertools import combinations
galaxies = list(filter(lambda x: x != '.', grid.values()))
combinations = list(combinations(galaxies, 2))

# coord of each galaxies
coord_galaxies = {}
for key, val in grid.items():
    if val in galaxies:
        coord_galaxies[val] = key

# shortest_path function between two given coords on a grid
def shortest_path(coord_g1, coord_g2):
    height = coord_g1[0] - coord_g2[0]
    width = coord_g1[1] - coord_g2[1]
    shortest_steps = abs(height) + abs(width)
    return shortest_steps

# shortest_path steps between pairs
shortest_steps_dict = {}
for pair in combinations:
    g1, g2 = pair
    coord_g1, coord_g2 = coord_galaxies[g1], coord_galaxies[g2]
    shortest_steps = shortest_path(coord_g1, coord_g2)
    shortest_steps_dict[pair] = shortest_steps

# quick visuals of the steps
# print("Pairs with shortest steps path:\n", shortest_steps_dict)
# print()

########################## ANSWERS ####################################

# answer part 1
print(sum(shortest_steps_dict.values()))  # 9312968

# answer part 2 is the same above code but changing the `expand` param in
# add_duplicate_no_galaxies function to 1000000-1
# but I can't solve it hmm because it takes too long