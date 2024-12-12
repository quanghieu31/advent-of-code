from utils import read_raw_input

with open(read_raw_input("day04"), 'r') as f:
    grid = [list(line) for line in f.read().splitlines()]

i_end, j_end = len(grid), len(grid[0])

# check row (2)
def check_row(i, j):

    def left_to_right(i, j):
        try:
            if grid[i][j+1: j+4] == ['M', 'A', 'S']:
                return 1
        except IndexError:
            return 0
        return 0

    def right_to_left(i, j):
        try:
            if grid[i][j-3: j] == ['S', 'A', 'M']:
                return 1
        except IndexError:
            return 0
        return 0

    return left_to_right(i, j) + right_to_left(i, j)


# check col (2)
def check_col(i, j):

    def top_to_bottom(i, j):
        try:
            if [x[j] for x in grid[i+1: i+4]] == ['M', 'A', 'S']:
                return 1
        except IndexError:
            pass
        return 0
    
    def bottom_to_top(i, j):
        try:
            if [x[j] for x in grid[i-3: i]] == ['S', 'A', 'M']:
                return 1
        except IndexError:
            pass
        return 0

    return top_to_bottom(i, j) + bottom_to_top(i, j)


# check diag (4)
def check_diag(i, j):

    def topleft_to_botright(i,j):
        try:
            if [grid[i+step][j+step] for step in range(1, 4)] == ['M', 'A', 'S']:
                return 1
        except IndexError:
            pass
        return 0

    def botright_to_topleft(i,j):
        try:
            if [grid[i-step][j-step] for step in range(1, 4) if i-step >= 0 and j-step >= 0] == ['M', 'A', 'S']:
                return 1
        except IndexError:
            pass
        return 0

    def topright_to_botleft(i, j):
        try:
            if [grid[i+step][j-step] for step in range(1, 4) if j-step >= 0] == ['M', 'A', 'S']:
                return 1
        except IndexError:
            pass
        return 0

    def botleft_to_topright(i, j):
        try:
            if [grid[i-step][j+step] for step in range(1, 4) if i-step >= 0] == ['M', 'A', 'S']:
                return 1
        except IndexError:
            pass
        return 0

    return topleft_to_botright(i,j) + botright_to_topleft(i,j) + topright_to_botleft(i,j) + botleft_to_topright(i,j)


count = 0

for i in range(i_end):
    for j in range(j_end):
        if grid[i][j] != "X":
            continue
        count += check_row(i, j) + check_col(i, j) + check_diag(i, j)

print(count)





from utils import read_raw_input

def count_xmas(grid):
    rows, cols = len(grid), len(grid[0])
    count = 0
    directions = [
        (0, 1), (0, -1),  # horizontal
        (1, 0), (-1, 0),  # vertical
        (1, 1), (-1, -1), (1, -1), (-1, 1)  # diagonal
    ]
    
    def check_direction(i, j, di, dj):
        try:
            return grid[i+di][j+dj] == 'M' and grid[i+2*di][j+2*dj] == 'A' and grid[i+3*di][j+3*dj] == 'S'
        except IndexError:
            return False

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 'X':
                count += sum(check_direction(i, j, di, dj) for di, dj in directions)

    return count

with open(read_raw_input("day04"), 'r') as f:
    grid = [list(line.strip()) for line in f]

print(count_xmas(grid))
