#!/usr/bin/env python
# coding: utf-8

# # Part 1

# In[14]:


def process_input(file):

    with open(file, "r") as f:
        lines = [list(map(int, line.strip().split())) for line in f.readlines()]
        
    return lines


# ## Example

# In[228]:


histories = process_input('example.in')

def diff(lst):
    lst3 = []
    lst1 = lst[:-1] # cannot have lst1, lst2 = lst[:-1], lst[1:] for some reason
    lst2 = lst[1:]
    for a, b in zip(lst1, lst2):
        diff = b - a
        lst3.append(diff)
    return lst3


def get_sequences_for_one_history(hist):
    zero = False # flag for first assumption: there is no zeros
    sequence = hist
    all_sequences_incl_hist = [hist]

    while zero is False:

        sequence = diff(sequence)
        all_sequences_incl_hist.append(sequence)
        # zero = reduce(lambda a, b: b-a, sequence)
        # zero = sum(sequence)   # not work because it could stop early aka sum(-1,1,-1,1) = 0 while we need (0,0,0,0)
        zero = all(x == 0 for x in sequence)

    return all_sequences_incl_hist


def extrapolate(hist):
    # extrapolate next value for each history

    all_sequences_incl_hist = get_sequences_for_one_history(hist)
    extrapolated = all_sequences_incl_hist

    if len(all_sequences_incl_hist) > 1: # meaning there are zeros
        last_ele_prev_seq = 0

        for idx, seq in reversed(list(enumerate(all_sequences_incl_hist))):  # No copy is created, the elements are reversed on the fly while traversing

            fill_placeholder = seq[-1] + last_ele_prev_seq
            extrapolated[idx].append(fill_placeholder)

            # after placeholder, update last_ele_prev_seq for later sequence update:
            last_ele_prev_seq = fill_placeholder

    extrapolated_element = extrapolated[0][-1]

    return extrapolated_element


def result(histories):
    sums = 0
    for hist in histories:
        next_value_in_history = extrapolate(hist)
        sums += next_value_in_history
    return sums

result(histories)


# ## Input

# In[229]:


histories = process_input("input.in")
result(histories)


# # Part 2

# ## Example

# In[235]:


histories = process_input('example.in')

def diff(lst):
    lst3 = []
    lst1 = lst[:-1] # cannot have lst1, lst2 = lst[:-1], lst[1:] for some reason
    lst2 = lst[1:]
    for a, b in zip(lst1, lst2):
        diff = b - a
        lst3.append(diff)
    return lst3


def get_sequences_for_one_history(hist):
    zero = False # flag for first assumption: there is no zeros
    sequence = hist
    all_sequences_incl_hist = [hist]

    while zero is False:

        sequence = diff(sequence)
        all_sequences_incl_hist.append(sequence)
        # zero = reduce(lambda a, b: b-a, sequence)
        # zero = sum(sequence)   # not work because it could stop early aka sum(-1,1,-1,1) = 0 while we need (0,0,0,0)
        zero = all(x == 0 for x in sequence)

    return all_sequences_incl_hist



###### Adjust for part 2

def extrapolate(hist):
    # extrapolate next value for each history

    all_sequences_incl_hist = get_sequences_for_one_history(hist)
    extrapolated = all_sequences_incl_hist

    if len(all_sequences_incl_hist) > 1: # meaning there are zeros
        last_ele_prev_seq = 0

        for idx, seq in reversed(list(enumerate(all_sequences_incl_hist))):  # No copy is created, the elements are reversed on the fly while traversing

            fill_placeholder = seq[0] - last_ele_prev_seq   # main adjust for Part 2
            extrapolated[idx].insert(0, fill_placeholder)   # O(n)

            # after placeholder, update last_ele_prev_seq for later sequence update:
            last_ele_prev_seq = fill_placeholder

    extrapolated_element = extrapolated[0][0]

    return extrapolated_element


def result(histories):
    sums = 0
    for hist in histories:
        next_value_in_history = extrapolate(hist)
        sums += next_value_in_history
    return sums

result(histories)


# ## Input

# In[237]:


histories = process_input("input.in")
result(histories)


# ## Deque for inserting O(1)

# In[238]:


# deque for inserting to beginning takes O(1)

histories = process_input('input.in')

def diff(lst):
    lst3 = []
    lst1 = lst[:-1] # cannot have lst1, lst2 = lst[:-1], lst[1:] for some reason
    lst2 = lst[1:]
    for a, b in zip(lst1, lst2):
        diff = b - a
        lst3.append(diff)
    return lst3


def get_sequences_for_one_history(hist):
    zero = False # flag for first assumption: there is no zeros
    sequence = hist
    all_sequences_incl_hist = [hist]

    while zero is False:

        sequence = diff(sequence)
        all_sequences_incl_hist.append(sequence)
        # zero = reduce(lambda a, b: b-a, sequence)
        # zero = sum(sequence)   # not work because it could stop early aka sum(-1,1,-1,1) = 0 while we need (0,0,0,0)
        zero = all(x == 0 for x in sequence)

    return all_sequences_incl_hist



###### Adjust for part 2 DEQUE

from collections import deque

def extrapolate(hist):
    # extrapolate next value for each history

    all_sequences_incl_hist = get_sequences_for_one_history(hist)
    extrapolated = [deque(seq) for seq in all_sequences_incl_hist]

    if len(all_sequences_incl_hist) > 1: # meaning there are zeros
        last_ele_prev_seq = 0

        for idx, seq in reversed(list(enumerate(all_sequences_incl_hist))):  # No copy is created, the elements are reversed on the fly while traversing

            fill_placeholder = seq[0] - last_ele_prev_seq    
            
            extrapolated[idx].appendleft(fill_placeholder)   # O(1)

            last_ele_prev_seq = fill_placeholder

    extrapolated_element = extrapolated[0][0]

    return extrapolated_element


def result(histories):
    sums = 0
    for hist in histories:
        next_value_in_history = extrapolate(hist)
        sums += next_value_in_history
    return sums

result(histories)

