# Original solution


```python
from collections import defaultdict
import re
```

## Part 1


```python
def process_one_line(line):
    # split :
    card, nums = line.split(":")
    winning, having = nums.split("|")
    winning = sorted([int(ele) for ele in winning.split(" ") if ele.isdigit()]) # O(nlogn)
    having = sorted([int(ele) for ele in having.split(" ") if ele.isdigit()]) # O(nlogn)

    return card, [winning, having]

def get_cards_dict(lines):
    cards = {}

    for line in lines:
        card, nums = process_one_line(line)
        cards[card] = nums

    return cards

def total_points(lines):
    cards_score = {}

    # all_cards
    cards = get_cards_dict(lines)

    # two-pointer technique
    for card, nums in cards.items():
        # for a card
        winning, having = nums[0], nums[1]

        # pointer start from 0
        i = 0
        j = 0
        matches = []

        while i < len(winning) and j < len(having):
            if winning[i] < having[j]:
                i += 1
            elif winning[i] > having[j]:
                j += 1
            else:
                matches.append(having[j])
                i += 1
                j += 1

        # count
        if matches:
            cards_score[card] = 2 ** (len(matches)-1)
        else:
            cards_score[card] = 0

    return cards_score

with open("input.txt", "r") as f:
    lines = [line.strip() for line in f.readlines()]

cards_score = total_points(lines)
sum(cards_score.values())
```




    21105



## Part 2


```python
def process_one_line(line):
    # split :
    card, nums = line.split(":")
    card = re.sub("[^0-9]", "", card)
    winning, having = nums.split("|")
    winning = sorted([int(ele) for ele in winning.split(" ") if ele.isdigit()]) # O(nlogn)
    having = sorted([int(ele) for ele in having.split(" ") if ele.isdigit()]) # O(nlogn)

    return card, [winning, having]

def get_cards_dict(lines):
    cards = {}

    for line in lines:
        card, nums = process_one_line(line)
        cards[card] = nums

    return cards

def total_cards(lines):
    cards_win_cards = {}

    # all_cards
    cards = get_cards_dict(lines)

    # two-pointer technique
    for card, nums in cards.items():
        # for a card
        winning, having = nums[0], nums[1]

        # pointer start from 0
        i = 0
        j = 0
        matches = []

        while i < len(winning) and j < len(having):
            if winning[i] < having[j]:
                i += 1
            elif winning[i] > having[j]:
                j += 1
            else:
                matches.append(having[j])
                i += 1
                j += 1

        # count
        cards_win_cards[card] = len(matches)

    return cards_win_cards


   
from collections import deque, defaultdict
def card_game(card_dict):
    # Initialize the card counts with the original cards
    card_counts = defaultdict(int)

    for card in cards_win_cards.keys():
        card_counts[card] = 1
    
    # Queue to process cards
    queue = deque()
    
    # Add all initial cards to the queue
    for card in card_counts:
        if card in card_dict:
            queue.append((card, card_counts[card]))

    print(card_counts)
    print("first: ", queue)

    print("card_dict: ", card_dict)

    while queue:
        current_card, current_count = queue.popleft()
        print(current_card, current_count)
        # If the card exists in the dictionary, process its winnings
        if current_card in card_dict:
            print(card_dict[current_card])
            for next_card in card_dict[current_card]:
                card_counts[next_card] += current_count

                # Add the next card to the queue for processing
                if next_card in card_dict:
                    queue.append((next_card, current_count))

        print("card_counts: ", card_counts)
        print("queue: ", queue)

    return card_counts


with open("example.txt", "r") as f:
    lines = [line.strip() for line in f.readlines()]

cards_win_cards = total_cards(lines)

counter = defaultdict(list)
for idx, cards_won in enumerate(cards_win_cards.values()):
    card_id = str(idx+1)
    # get the cards won for each card
    for idx_in_cards_won in range(idx + 1, idx + cards_won + 1):
        card_id_won = str(idx_in_cards_won + 1)
        counter[card_id].append(card_id_won)

# Call the function and print the result
final_card_counts = card_game(counter)

```

    defaultdict(<class 'int'>, {'1': 1, '2': 1, '3': 1, '4': 1, '5': 1, '6': 1})
    first:  deque([('1', 1), ('2', 1), ('3', 1), ('4', 1)])
    card_dict:  defaultdict(<class 'list'>, {'1': ['2', '3', '4', '5'], '2': ['3', '4'], '3': ['4', '5'], '4': ['5']})
    1 1
    ['2', '3', '4', '5']
    card_counts:  defaultdict(<class 'int'>, {'1': 1, '2': 2, '3': 2, '4': 2, '5': 2, '6': 1})
    queue:  deque([('2', 1), ('3', 1), ('4', 1), ('2', 1), ('3', 1), ('4', 1)])
    2 1
    ['3', '4']
    card_counts:  defaultdict(<class 'int'>, {'1': 1, '2': 2, '3': 3, '4': 3, '5': 2, '6': 1})
    queue:  deque([('3', 1), ('4', 1), ('2', 1), ('3', 1), ('4', 1), ('3', 1), ('4', 1)])
    3 1
    ['4', '5']
    card_counts:  defaultdict(<class 'int'>, {'1': 1, '2': 2, '3': 3, '4': 4, '5': 3, '6': 1})
    queue:  deque([('4', 1), ('2', 1), ('3', 1), ('4', 1), ('3', 1), ('4', 1), ('4', 1)])
    4 1
    ['5']
    card_counts:  defaultdict(<class 'int'>, {'1': 1, '2': 2, '3': 3, '4': 4, '5': 4, '6': 1})
    queue:  deque([('2', 1), ('3', 1), ('4', 1), ('3', 1), ('4', 1), ('4', 1)])
    2 1
    ['3', '4']
    card_counts:  defaultdict(<class 'int'>, {'1': 1, '2': 2, '3': 4, '4': 5, '5': 4, '6': 1})
    queue:  deque([('3', 1), ('4', 1), ('3', 1), ('4', 1), ('4', 1), ('3', 1), ('4', 1)])
    3 1
    ['4', '5']
    card_counts:  defaultdict(<class 'int'>, {'1': 1, '2': 2, '3': 4, '4': 6, '5': 5, '6': 1})
    queue:  deque([('4', 1), ('3', 1), ('4', 1), ('4', 1), ('3', 1), ('4', 1), ('4', 1)])
    4 1
    ['5']
    card_counts:  defaultdict(<class 'int'>, {'1': 1, '2': 2, '3': 4, '4': 6, '5': 6, '6': 1})
    queue:  deque([('3', 1), ('4', 1), ('4', 1), ('3', 1), ('4', 1), ('4', 1)])
    3 1
    ['4', '5']
    card_counts:  defaultdict(<class 'int'>, {'1': 1, '2': 2, '3': 4, '4': 7, '5': 7, '6': 1})
    queue:  deque([('4', 1), ('4', 1), ('3', 1), ('4', 1), ('4', 1), ('4', 1)])
    4 1
    ['5']
    card_counts:  defaultdict(<class 'int'>, {'1': 1, '2': 2, '3': 4, '4': 7, '5': 8, '6': 1})
    queue:  deque([('4', 1), ('3', 1), ('4', 1), ('4', 1), ('4', 1)])
    4 1
    ['5']
    card_counts:  defaultdict(<class 'int'>, {'1': 1, '2': 2, '3': 4, '4': 7, '5': 9, '6': 1})
    queue:  deque([('3', 1), ('4', 1), ('4', 1), ('4', 1)])
    3 1
    ['4', '5']
    card_counts:  defaultdict(<class 'int'>, {'1': 1, '2': 2, '3': 4, '4': 8, '5': 10, '6': 1})
    queue:  deque([('4', 1), ('4', 1), ('4', 1), ('4', 1)])
    4 1
    ['5']
    card_counts:  defaultdict(<class 'int'>, {'1': 1, '2': 2, '3': 4, '4': 8, '5': 11, '6': 1})
    queue:  deque([('4', 1), ('4', 1), ('4', 1)])
    4 1
    ['5']
    card_counts:  defaultdict(<class 'int'>, {'1': 1, '2': 2, '3': 4, '4': 8, '5': 12, '6': 1})
    queue:  deque([('4', 1), ('4', 1)])
    4 1
    ['5']
    card_counts:  defaultdict(<class 'int'>, {'1': 1, '2': 2, '3': 4, '4': 8, '5': 13, '6': 1})
    queue:  deque([('4', 1)])
    4 1
    ['5']
    card_counts:  defaultdict(<class 'int'>, {'1': 1, '2': 2, '3': 4, '4': 8, '5': 14, '6': 1})
    queue:  deque([])
    


```python
final_card_counts, sum(final_card_counts.values())
```




    (defaultdict(int, {'1': 1, '2': 2, '3': 4, '4': 8, '5': 14, '6': 1}), 30)



## Why deque (double-end queue)?

# Part 2 - DP

source: https://github.com/samyuh/advent-of-code/blob/main/2023/day_4.py


```python
import re

with open('./example.txt', 'r') as file:
    lines = file.readlines()

    pattern = re.compile(r'Card\s+(\d+):\s+([\d\s]+)\s*\|\s*([\d\s]+)')
    pile_points = 0
    cards_instances = [1] * len(lines)
    for entry in lines:
        print("entry:", entry)
        match = pattern.search(entry)
        print("match: ", match)
        
        card_num = int(match.group(1))
        print("card number: ", card_num)

        group1_numbers = list(map(int, match.group(2).split()))
        group2_numbers = list(map(int, match.group(3).split()))

        common_elements_count = len(set(group1_numbers) & set(group2_numbers))
        pile_points += 2 ** (common_elements_count - 1) if common_elements_count >= 1 else 0

        print("common_elements_count:", common_elements_count)
        for idx in range(common_elements_count):
            cards_instances[card_num + idx] += cards_instances[card_num - 1] 

        print("cards_instance count:", cards_instances)
        print("----")
    
    print(f"Part 1: {pile_points}")
    print(f"Part 2: {sum(cards_instances)}")
```

    entry: Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
    
    match:  <re.Match object; span=(0, 49), match='Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53\>
    card number:  1
    common_elements_count: 4
    cards_instance count: [1, 2, 2, 2, 2, 1]
    ----
    entry: Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
    
    match:  <re.Match object; span=(0, 49), match='Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19\>
    card number:  2
    common_elements_count: 2
    cards_instance count: [1, 2, 4, 4, 2, 1]
    ----
    entry: Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
    
    match:  <re.Match object; span=(0, 49), match='Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1\>
    card number:  3
    common_elements_count: 2
    cards_instance count: [1, 2, 4, 8, 6, 1]
    ----
    entry: Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
    
    match:  <re.Match object; span=(0, 49), match='Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83\>
    card number:  4
    common_elements_count: 1
    cards_instance count: [1, 2, 4, 8, 14, 1]
    ----
    entry: Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
    
    match:  <re.Match object; span=(0, 49), match='Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36\>
    card number:  5
    common_elements_count: 0
    cards_instance count: [1, 2, 4, 8, 14, 1]
    ----
    entry: Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11
    match:  <re.Match object; span=(0, 48), match='Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11'>
    card number:  6
    common_elements_count: 0
    cards_instance count: [1, 2, 4, 8, 14, 1]
    ----
    Part 1: 13
    Part 2: 30
    

## Why? How?
