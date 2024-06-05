# Part 1

input = '2023\day2\input.txt'
with open(input, 'r') as f:
    lines = [line.strip() for line in f.readlines()]

sum_game_ids = 0

for line in lines:
    # split game id vs rest
    game_id = int(line.split(':')[0].split(' ')[-1])

    # split different sets of cubes
    subsets_string = line.split(':')[1].strip()
    subsets_list = subsets_string.split(';')

    subset_qualification = True

    for subset in subsets_list:
        subset = [s.strip() for s in subset.split(',')]

        # in this subset (among many subsets in the game id)
        for cube in subset: 
            count, color = int(cube.split(' ')[0]), cube.split(' ')[1]

            if color == 'red' and count > 12 or color == 'green' and count > 13 or color == 'blue' and count > 14:
                subset_qualification = False
                break # violation: exit the for cube in subset: the subset is done, 
                        # meaning: entire subsets_list is done => bye
            
        # then move on to check the subset_qualification for this subset
        # to break entirely the subsets_list iteration
        # If false, done with this subsets_list => move on to next game_id
        # if still true, not break the subset_list iteration yet and continue with next subset
        if not subset_qualification: 
            break

    if subset_qualification:
        sum_game_ids += game_id

print("Part 1: ", sum_game_ids)


# Part 2

from functools import reduce
def mul(x, y):
    return x * y

power_all_games = 0

for line in lines:

    # split different sets of cubes
    subsets_string = line.split(':')[1].strip()
    subsets_list = subsets_string.split(';')

    cube_color_min = {}
    for subset in subsets_list:
        subset = [s.strip() for s in subset.split(',')]

        # in this subset (among many subsets in the game id)
        for cube in subset: 
            cur_count, color = int(cube.split(' ')[0]), cube.split(' ')[1]
            prev_count = cube_color_min.get(color, 0)
            cube_color_min[color] = max(prev_count, cur_count)

    power_all_games += reduce(mul, cube_color_min.values())

print("Part 2: ", power_all_games)


