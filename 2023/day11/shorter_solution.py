input_file = '2023/day11/input.in'

# To match the format of input files for the Basilisk.
q = { 11: open(input_file).read() }

######################### PART 1: MULTI-LINE SOLUTION #########################
galaxies = [(x, y) for y, row in enumerate(q[11].strip().split()) for x, col in enumerate(row) if col == '#']

max_x = max(galaxies, key=lambda x: x[0])[0]
max_y = max(galaxies, key=lambda x: x[1])[1]

empty_rows = [y for y in range(max_y+1) if not any([y == g[1] for g in galaxies])]
empty_cols = [x for x in range(max_x+1) if not any([x == g[0] for g in galaxies])]

galaxies = [(g[0] + len([x for x in empty_cols if x < g[0]]), g[1] + len([y for y in empty_rows if y < g[1]])) for g in galaxies]

shortest_paths = {}
for g1 in galaxies:
    for g2 in galaxies:
        if g1 != g2 and (g2, g1) not in shortest_paths:
            shortest_paths[(g1, g2)] = abs(g1[0] - g2[0]) + abs(g1[1] - g2[1])
            
print('Day 11 Part 1:',sum(shortest_paths.values()))



######################## PART 2: MULTI-LINE SOLUTION ##########################
galaxies = [(x, y) for y, row in enumerate(q[11].strip().split()) for x, col in enumerate(row) if col == '#']

max_x = max(galaxies, key=lambda x: x[0])[0]
max_y = max(galaxies, key=lambda x: x[1])[1]

empty_rows = [y for y in range(max_y+1) if not any([y == g[1] for g in galaxies])]
empty_cols = [x for x in range(max_x+1) if not any([x == g[0] for g in galaxies])]

galaxies = [(g[0] + (len([x for x in empty_cols if x < g[0]]) * 999999), g[1] + (len([y for y in empty_rows if y < g[1]]) * 999999)) for g in galaxies]

shortest_paths = {}
for g1 in galaxies:
    for g2 in galaxies:
        if g1 != g2 and (g2, g1) not in shortest_paths:
            shortest_paths[(g1, g2)] = abs(g1[0] - g2[0]) + abs(g1[1] - g2[1])
print('Day 11 Part 2:',sum(shortest_paths.values()))
