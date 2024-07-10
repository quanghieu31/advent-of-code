#!/usr/bin/env python
# coding: utf-8

# example


from collections import defaultdict



with open("example.txt", "r") as f:
    lines = [line.strip() for line in f.readlines()]

example_line = lines[0]

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

cards_score = total_points(lines)
cards_score, sum(cards_score.values())



with open("input.txt", "r") as f:
    lines = [line.strip() for line in f.readlines()]


cards_score = total_points(lines)
cards_score, sum(cards_score.values())





# ## Part 2

# ### Example


with open("example.txt", "r") as f:
    lines = [line.strip() for line in f.readlines()]

example_line = lines[0]

import re




# part 2
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

cards_win_cards = total_cards(lines)
cards_win_cards



counter = defaultdict(list)

for idx, cards_won in enumerate(cards_win_cards.values()):

    card_id = str(idx+1)

    # get the cards won for each card
    for idx_in_cards_won in range(idx + 1, idx + cards_won + 1):
        card_id_won = str(idx_in_cards_won + 1)
        counter[card_id].append(card_id_won)
        
counter



from collections import deque, defaultdict

def card_game(card_dict):
    # Initialize the card counts with the original cards
    card_counts = {
        '1': 1,
        '2': 1,
        '3': 1,
        '4': 1,
        '5': 1,
        '6': 1
    }
    
    # Queue to process cards
    queue = deque()
    
    # Add all initial cards to the queue
    for card in card_counts:
        if card in card_dict:
            queue.append((card, card_counts[card]))

    while queue:
        current_card, current_count = queue.popleft()

        # If the card exists in the dictionary, process its winnings
        if current_card in card_dict:
            for next_card in card_dict[current_card]:
                if next_card in card_counts:
                    card_counts[next_card] += current_count
                else:
                    card_counts[next_card] = current_count

                # Add the next card to the queue for processing
                if next_card in card_dict:
                    queue.append((next_card, current_count))

    return card_counts

# Call the function and print the result
final_card_counts = card_game(counter)
print(final_card_counts)

sum(final_card_counts.values())






# ### Input


with open("input.txt", "r") as f:
    lines = [line.strip() for line in f.readlines()]

cards_win_cards = total_cards(lines)
cards_win_cards.keys()




counter = defaultdict(list)

for idx, cards_won in enumerate(cards_win_cards.values()):

    card_id = str(idx+1)

    # get the cards won for each card
    for idx_in_cards_won in range(idx + 1, idx + cards_won + 1):
        card_id_won = str(idx_in_cards_won + 1)
        counter[card_id].append(card_id_won)
        
counter



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

    while queue:
        current_card, current_count = queue.popleft()

        # If the card exists in the dictionary, process its winnings
        if current_card in card_dict:
            for next_card in card_dict[current_card]:
                if next_card in card_counts:
                    card_counts[next_card] += current_count
                else:
                    card_counts[next_card] = current_count

                # Add the next card to the queue for processing
                if next_card in card_dict:
                    queue.append((next_card, current_count))

    return card_counts

# Call the function and print the result
final_card_counts = card_game(counter)

final_card_counts, sum(final_card_counts.values())


import re

with open('./input.txt', 'r') as file:
    lines = file.readlines()

    pattern = re.compile(r'Card\s+(\d+):\s+([\d\s]+)\s*\|\s*([\d\s]+)')
    pile_points = 0
    cards_instances = [1] * len(lines)
    for entry in lines:
        match = pattern.search(entry)
        
        card_num = int(match.group(1))
        group1_numbers = list(map(int, match.group(2).split()))
        group2_numbers = list(map(int, match.group(3).split()))

        common_elements_count = len(set(group1_numbers) & set(group2_numbers))
        pile_points += 2 ** (common_elements_count - 1) if common_elements_count >= 1 else 0

        for idx in range(common_elements_count):
            cards_instances[card_num + idx] += cards_instances[card_num - 1] 
    
    print(f"Part 1: {pile_points}")
    print(f"Part 2: {sum(cards_instances)}")

