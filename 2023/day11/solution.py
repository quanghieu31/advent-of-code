####################### Read input ###################################

# read lines
file_path = "2023/day11/example.in"
with open(file_path, "r") as f:
    lines = [list(line.strip()) for line in f.readlines()]

####################### check expand ###################################

# for every col and every row, duplicate to next position
def add_duplicate_no_galaxies(lines):  

    expanded_row_lines = []
    # check row
    for line in lines:
        expanded_row_lines.append(line)
        if len(set(line)) == 1:
            expanded_row_lines.append(line)
   
    # check columns using transpose of expanded_row_lines
    transposed = zip(*expanded_row_lines) # consequentially pairs
    expanded_transposed = []
    for col in transposed:
        expanded_transposed.append(col)
        if len(set(col)) == 1:
            expanded_transposed.append(col)

    # transpose back and convert to list
    expanded_lines = list(map(list, zip(*expanded_transposed)))
    return expanded_lines

print("\nThe expanded lines/space is:\n", *add_duplicate_no_galaxies(lines), "\n")

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
print("Grid with coordinate is", grid)


############### find shortest path between each pair ##########################