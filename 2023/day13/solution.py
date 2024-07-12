####### read input
input_file = 'input.in'
with open(input_file, "r") as f:
    blocks = [line.split("\n") for line in f.read().split("\n\n")]

############### test
block1, block2 = blocks[0], blocks[1]

# ##################### reflection
def reflection_row(block: list[str]) -> int:
    n_rows, n_cols = len(block), len(block[0])

    for idx in range(1, n_rows):
        up = block[:idx]
        bot = block[idx:]
        if all(l == r for l, r in zip(reversed(up), bot)):
            return idx

    return 0

def reflection_column(block: list[str]) -> int:

    transposed_list = list(map(list, zip(*block)))
    transposed_strings = ["".join(row) for row in transposed_list]

    return reflection_row(transposed_strings)

#######################
def calculate(block):
    a, b = reflection_row(block), reflection_column(block)
    s = 0
    if a:
        s += 100*a
    if b:
        s += b
    return s

final_s = 0
for block in blocks:
    final_s += calculate(block)

print(final_s) # 27202