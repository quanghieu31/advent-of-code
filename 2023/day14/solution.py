############ read input
input_file = "2023/day14/input.in"
with open(input_file, "r") as f:
    lines = f.read().splitlines() # still get a list and without the \n break

############ parse grid => no need to parse grid in this case

############ tilt north

transposed = ["".join(row) for row in list(map(list, zip(*lines)))]
tilted_list = []

for col in transposed:
    col = list(col)  # string to list for mutable operationss

    for idx in range(1, len(col)):

        if col[idx] == 'O':
            
            while idx > 0 and col[idx-1] == '.':

                col[idx-1], col[idx] = col[idx], col[idx-1]  # swap 'O' with '.' 
                # => must be same code line, not different code line
                idx -= 1  # check further left

    tilted = "".join(col)
    tilted_list.append(tilted)

############ sum load

sum_loads = 0

for col in tilted_list:
    range_reverse = range(len(col), 0, -1)

    for load, entry in zip(range_reverse, col):
        if entry == "O":
            sum_loads += load

print(sum_loads)

# part 1: 109755
# part 2: it's a little bit complicated, involving recursion and 100000 cycles