# BFS and DFS

from collections import defaultdict, deque

with open('2023/day10/input.in', 'r') as f:
    arrays = [list(line.strip()) for line in f.readlines()]


# Directions: N, E, S, W
directions = {
    '|': [(-1, 0), (1, 0)],     # (steps_vertically, step_horizontally) x2 because connection to 2 neighbors
    '-': [(0, -1), (0, 1)],     # negative means up and left, positive means down and right
    'L': [(-1, 0), (0, 1)],
    'J': [(-1, 0), (0, -1)],
    '7': [(1, 0), (0, -1)],
    'F': [(1, 0), (0, 1)],
}

# assume S is like F in this particular case

# find position of S
def find_location_S(arrays):
    for i, row in enumerate(arrays):
        for j, entry in enumerate(row):
            if entry == 'S':
                return i, j
coord_x, coord_y = find_location_S(arrays)


# check adjacent neigbor to entry at start_i, start_j
top_most, bot_most, left_most, right_most = 0, len(arrays), 0, len(arrays[0])

def are_adjacent(x, y, new_x, new_y):
    if 0 <= new_x < bot_most and 0 <= new_y < right_most:
        if arrays[new_x][new_y] in directions:    # to avoid the "." case
            for dx, dy in directions[arrays[new_x][new_y]]:
                if (new_x + dx, new_y + dy) == (x, y):
                    return True
    return False


# BFS to find all single connected components
queue = deque([(coord_x, coord_y, 0)])      
# each element is a tuple of 3 things: (coord_x, coord_y, steps from S)

visited = set((coord_x, coord_y))
steps_increment = {}

while queue: # running after adding and visiting all pipes in queue

    print(queue)
    x, y, dist = queue.popleft()
    steps_increment[(x, y)] = dist

    current_pipe = arrays[x][y] if arrays[x][y] != 'S' else 'F' # assuming 'S' is actually 'F'
    
    for dx, dy in directions.get(current_pipe, []):
        nx, ny = x + dx, y + dy
        if (nx, ny) not in visited and are_adjacent(x, y, nx, ny):
            visited.add((nx, ny))
            queue.append((nx, ny, dist + 1))


# Find the maximum distance
max_distance = max(steps_increment.values())

print(max_distance) 