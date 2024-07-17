######## read input
input_file = '2023/day16/example.in'
with open(input_file, 'r') as f:
    arrays = [list(x) for x in f.read().splitlines()]

######## parse grid

# GridPoint = tuple[int, int]
# Grid = dict[GridPoint, str]
grid = {}
for row, array in enumerate(arrays):
    for col, entry in enumerate(array):
        grid[(row, col)] = entry

grid_track = grid

######## beamming rules

# check starting beam rule
 
# TODO: could be many current coords? 
cur_coord = tuple()
next_coord = tuple()

for k, v in grid.items():
    if v == '.':
        grid_track[k] = '#'
        cur_coord = k
    else:
        grid_track[k] = '#'
        next_coord = k
        break

# rules
while True: # TODO

    if grid[next_coord] == '|':
        pass

    elif grid[next_coord] == '-':
        pass

    elif grid[next_coord] == '/':
        pass

    elif grid[next_coord] == "\\":
        
        if not cur_coord:
            grid_track[next_coord] = '#'

        else:
            if cur_coord < next_coord:
                grid_track[next_coord] = '#'

                cur_coord = next_coord
                next_coord = (next_coord[0]+1, next_coord[1])


    elif grid[next_coord] == '.':
            if grid[cur_coord] == '|':
                next_coord = (cur_coord[0]+1, cur_coord[1])
            elif grid[cur_coord] == '-':
                next_coord = (cur_coord[0], cur_coord[1]+1)
            elif grid[cur_coord] == '/':
                next_coord = (cur_coord[0], cur_coord[1]+1)
            elif grid[cur_coord] == "\\":
                pass

            
