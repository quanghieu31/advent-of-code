from utils import read_raw_input
import numpy as np

with open(read_raw_input("day06"), 'r') as f:
    grid = [list(line) for line in f.read().split()]
    grid = np.array(grid)

# locate the starting arrow/guard position
start_coord = list()
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if grid[i, j] in ("^", ">", "<", "v"):
            start_coord = [i, j]


current_coord = start_coord
history = [grid[*current_coord]]

directions = {
    "^": (-1, 0),
    ">": (0, 1),
    "v": (1, 0),
    "<": (0, -1),
}

change_directions = {
    "^": (0, 1),
    ">": (1, 0),
    "v": (0, -1),
    "<": (-1, 0),
}

change_direction_history = {
    "^": ">",
    ">": "v",
    "v": "<",
    "<": "^",
}

while True:

    try:
        row, col = current_coord
        current_cell = grid[row, col]

        if row < 0 or col < 0:
            break

        if current_cell in directions.keys():
            drow, dcol = directions[history[-1]]
            grid[row, col] = "X"
            next_coord = [row + drow, col + dcol]
            history.append(current_cell)
            
        elif current_cell == ".":
            drow, dcol = directions[history[-1]]
            grid[row, col] = "X"
            next_coord = [row + drow, col + dcol]

        elif current_cell == "X":
            # already visited, continue in the same direction
            drow, dcol = directions[history[-1]]
            next_coord = [row + drow, col + dcol]

        if current_cell == "#":
            # if bump, go back to previous cell and change direction
            drow, dcol = directions[history[-1]]
            row, col = row - drow, col - dcol
            new_drow, new_dcol = change_directions[history[-1]]
            next_coord = [row + new_drow, col + new_dcol]
            history.append(change_direction_history[history[-1]])

        # update
        current_coord = next_coord

    except IndexError:
        break

print(np.count_nonzero(grid == "X"))