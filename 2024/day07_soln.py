from utils import read_raw_input

with open(read_raw_input("day07"), 'r') as f:
    raw = [line.split(":") for line in f.read().split("\n")]
    data = {int(line[0]): list(map(int, line[1].strip().split(" "))) for line in raw}

# test
# each of the in-between positions has 2 choices 
test = [81, 40, 27]
n_operators = len(test) - 1
n_combinations = n_operators * 2

# => generate list of possible combinations, then apply to the numbers themselves
# https://docs.python.org/3/library/itertools.html#itertools.product
def product(*iterables, repeat=1):
    # product('ABCD', 'xy') → Ax Ay Bx By Cx Cy Dx Dy
    # product(range(2), repeat=3) → 000 001 010 011 100 101 110 111

    pools = [tuple(pool) for pool in iterables] * repeat

    result = [[]]
    for pool in pools:
        result = [x+[y] for x in result for y in pool]

    for prod in result:
        yield tuple(prod)


###############################################################################

def get_value_comb(operators, numbers, key):
    n_operators = len(numbers) - 1
    combinations = list(product(operators, repeat=n_operators))

    for comb in combinations:
        value_comb = numbers[0]
        for idx, operator in enumerate(comb):
            if operator == '*':
                value_comb *= numbers[idx + 1]
            elif operator == '+':
                value_comb += numbers[idx + 1]
            elif operator == '||':
                value_comb = int(str(value_comb) + str(numbers[idx + 1]))

        if value_comb == key:
            return key

    return None

sum_wanted_keys = 0
for key, numbers in data.items():
    result = get_value_comb(['*', '+'], numbers, key)
    if result is not None:
        sum_wanted_keys += result

print(sum_wanted_keys)


###############################################################################


sum_wanted_keys = 0
for key, numbers in data.items():
    result = get_value_comb(['*', '+', '||'], numbers, key)
    if result is not None:
        sum_wanted_keys += result

print(sum_wanted_keys)