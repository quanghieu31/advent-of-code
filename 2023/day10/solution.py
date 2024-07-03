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
top_most, bot_most, left_most, right_most = 0, len(arrays)-1, 0, len(arrays[0])-1

def bool_adjacent_based_on_given_directions(x, y, new_x, new_y):
    if top_most <= x <= bot_most and left_most <= y <= right_most:
        if arrays[x][y] in directions.keys(): # to avoid the '.' case
            
            for (change_x, change_y) in directions[arrays[x][y]]:
                
                # check new_x, new_y if this adjacent
                if (change_x, change_y) == (-(x-new_x), -(y-new_y)):
                    return True

    return False 



# BFS to find all single connected components
queue = deque([(coord_x, coord_y, 0)])      
# each element is a tuple of 3 things: (coord_x, coord_y, steps from S)

visited = set((coord_x, coord_y))
steps_increment = {}

while queue: # running after adding and visiting all pipes in queue
    
    print(queue)
    x, y, step = queue.popleft()    # rmb: x,y are coordinates/indices
    steps_increment[(x, y)] = step

    # # assume 'S' to be 'L' in this particular case only (after looking at the)
    if arrays[x][y] == 'S':
        current_pipe = 'L'
    else:
        current_pipe = arrays[x][y]

    for (change_x, change_y) in directions.get(current_pipe, []):

        # check new_x and new_y if it is legit accd. to rule
        new_x, new_y = x + change_x, y + change_y 

        if (new_x, new_y) not in visited and bool_adjacent_based_on_given_directions(x, y, new_x, new_y):
            visited.add((new_x, new_y))
            queue.append((new_x, new_y, step+1))

    # Find the maximum distance
max_distance = max(steps_increment.values())

print(max_distance) 