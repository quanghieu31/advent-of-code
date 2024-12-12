from utils import read_raw_input

with open(read_raw_input("day05"), 'r') as f:
    raw = f.read().split("\n\n")
    s1, s2 = raw[0], raw[1]

# preprocess
list_orders = [order.split("|") for order in s1.split("\n")]
orders = [(int(order[0]), int(order[1])) for order in list_orders]
manuals = [list(map(int, manual.split(","))) for manual in s2.split("\n")]


# brute force
sum_mids = 0

for manual in manuals:
    all_correct = []

    for idx in range(len(manual) - 1):
        correct_order = False

        for order in orders:
            if order[0] == manual[idx] and order[1] == manual[idx + 1]:
                correct_order = True
                break # escape the for order in orders loop

        all_correct.append(correct_order)
        
    if all(all_correct):
        mid = manual[len(manual) // 2]
        sum_mids += mid

print("brute force O(M x N x O):", sum_mids)        


##########################################

# more efficient

# O(1) to look up
orders = set(tuple(map(int, order.split("|"))) for order in s1.split("\n")) 

sum_mids = 0

for manual in manuals: # O(M)
    correct_orders = True

    for idx in range(len(manual) - 1): # O(N)
        # instead of indexing the tuples, just check the tuple as a whole
        if (manual[idx], manual[idx + 1]) not in orders: 
            correct_orders = False
            break  # stop checking this manual if any order pair is invalid (even just one!)

    if correct_orders:
        sum_mids += manual[len(manual) // 2]

print("only O(M x N):", sum_mids)   