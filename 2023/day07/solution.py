#!/usr/bin/env python
# coding: utf-8

# # Part 1

# In[1]:


card_strengths = {
    '2': 0,
    '3': 1,
    '4': 2,
    '5': 3,
    '6': 4,
    '7': 5,
    '8': 6,
    '9': 7,
    'T': 8,
    'J': 9,
    'Q': 10,
    'K': 11,
    'A': 12
}   

# co the ko can
hand_type = {
    'High card': 0,
    'One pair': 1,
    'Two pair': 2,
    'Three of a kind': 3,
    'Full house': 4,
    'Four of a kind': 5,
    'Five of a kind': 6
}

def get_hand_type(hand):
    hand_tuple = tuple(hand)

    # high card
    hand_set = set(hand_tuple)
    if len(hand_set) == 5:
        return hand_type['High card']

    # count
    count_pairs = len([i for i in hand_set if hand_tuple.count(i) == 2])
    count_three = len([i for i in hand_set if hand_tuple.count(i) == 3])
    count_four = len([i for i in hand_set if hand_tuple.count(i) == 4])
    count_five = len([i for i in hand_set if hand_tuple.count(i) == 5])

    if count_five == 1:
        return hand_type['Five of a kind']
    elif count_four == 1:
        return hand_type['Four of a kind']
    elif count_three == 1 and count_pairs == 1:
        return hand_type['Full house']
    elif count_three == 1:
        return hand_type['Three of a kind']
    elif count_pairs == 2:
        return hand_type['Two pair']
    elif count_pairs == 1:
        return hand_type['One pair']

def convert_hand_cards_to_strength(hand):
    strength = tuple()
    for card in hand:
        strength = strength + (card_strengths[card],)
    return strength


# ## Example

# In[2]:


import pandas as pd

with open('example.in', 'r') as f:
    hands_bids = {}
    for line in f.readlines():
        line = line.strip().split()
        hands_bids[line[0]] = int(line[1])

df = pd.DataFrame(list(hands_bids.items()), columns=['hand', 'bid'])

df['hand_type'] = df['hand'].apply(get_hand_type)
df['hand_strength'] = df['hand'].apply(convert_hand_cards_to_strength)
df = df.sort_values(by=['hand_type', 'hand_strength'], ascending=False)
len_df = len(df)
df['rank'] = [i for i in range(len_df, 0, -1)]
df['bid_value'] = df['bid'] * df['rank']

sum(df['bid_value'])


# ## Input

# In[3]:


import pandas as pd

with open('input.in', 'r') as f:
    hands_bids = {}
    for line in f.readlines():
        line = line.strip().split()
        hands_bids[line[0]] = int(line[1])

df = pd.DataFrame(list(hands_bids.items()), columns=['hand', 'bid'])
len_df = len(df)

df['hand_type'] = df['hand'].apply(get_hand_type)
df['hand_strength'] = df['hand'].apply(convert_hand_cards_to_strength)

df.sort_values(by=['hand_type', 'hand_strength'], ascending=False, inplace=True)

df['rank'] = range(len_df, 0, -1)
df['bid_value'] = df['bid'] * df['rank']

sum(df['bid_value'])


# # Part 2

# Part 2 is a little bit hard
