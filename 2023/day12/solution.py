########################### prepare input ####################################

input_path = '2023/day12/example.in'
with open(input_path, "r") as f:
    lines = [line.strip().split(' ') for line in f.readlines()]

records = {}
for row, values in enumerate(lines):
    info_row = {}
    springs, group_size = list(values[0]), list(map(lambda x: int(x), values[1].split(',')))
    info_row["springs"] = springs
    info_row["group_size"] = group_size

    records[row] = info_row

#################### 

# see current group of contiguous #'s and how many #'s of each group
def check_current_contiguous_damaged(springs):
    groups = []
    current_group_length = 0

    for s in springs:
        if s == '#':
            current_group_length += 1
        else:
            if current_group_length > 0:
                groups.append(current_group_length)
                # reset current length group:
                current_group_length = 0

    if current_group_length > 0:
        groups.append(current_group_length)

    return groups

for v in records.values():
    print(check_current_contiguous_damaged(v["springs"]))

