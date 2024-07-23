from collections import defaultdict, deque

#### read input
with open("2023/day25/input.in", "r") as f:
    lines = f.read().splitlines()

wires_map = defaultdict(set)

for wire in lines:
    wire, connected_wires = wire.strip().split(': ')
    
    for cw in connected_wires.split():
        wires_map[wire].add(cw)
        wires_map[cw].add(wire)


##### disconnect into 2 groups
# first group, second group - counting
group_1, group_2 = 1, 0


###### iteration:

first_wire = list(wires_map.keys())[0] # get first wire in map

for wire in list(wires_map.keys())[1:]:
    connections = 0
    checked_wires = {first_wire}

    # finds shortest path for considered wire
    # for each of starting wire without repeating used wire
    # THIS IS BFS
    for s_wire in wires_map[first_wire]:

        # explore paths from starting s_wire
        if s_wire == wire:
            connections += 1
            continue
        qed = set()
        q = deque()
        q.append((s_wire, [s_wire]))
        found = False

        while q and not found and connections < 4:

            # for each wi in the queue => check all its connected wires (w)
            wi, path = q.popleft()

            for w in wires_map[wi]:

                # if w is the target wire, increase connections, 
                # update checked_wires, and stop further search for this s_wire.
                if w == wire:
                    connections += 1
                    checked_wires.update(path)
                    found = True
                    break

                # If w is not checked yet and not in the current path, 
                # add it to the queue for next exploration.
                elif w not in qed and w not in path and w not in checked_wires:
                    q.append([w, path + [w]])
                    qed.add(w)

    # If it finds more than 3 unique ways to get to given wire then it is in group 1
    if connections >= 4:
        group_1 += 1
    else:
        group_2 += 1

print("part 1:", group_1 * group_2)