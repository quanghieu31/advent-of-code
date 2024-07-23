#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
os.getcwd()

with open('example.txt', 'r') as f:
    example = [line.strip() for line in f.readlines()]

# split to get array of array or list of list (look like a matrix)
example_matrix = [list(line) for line in example]

example_matrix


# In[2]:


example_matrix[1][3]


# In[3]:


# default dict vs dict.setdefault()

from collections import defaultdict # handle unknown missing keys whereas dict.setdefault must specify what missing key is


# In[4]:


dic = defaultdict(set)

# example wanted result: dic = {'*': {467, 35}, '#': {633}}
dic


# In[5]:


x = [[1, 2, 3], [1, 2, 3], [1, 2, 3]]
x[5:6][1:3]

# So, always access x[i:i+1], if you want x[i]. You'll get a list with the required element if it exists. Otherwise, you get an empty list
# rmb: slicing results in the same list but reduced elements. for example: x = [1,2,3], x[1:2] = [2], instead of just 2
# if just index only => value (not a list like slicing)
# dont know if fast? but it works


# In[6]:


example_matrix


# In[7]:


len_row = len(example_matrix[0])
len_col = len(example_matrix)

def get_number_in_that_row(j, idx, row):

    numbers_string_list = []

    j1, j2 = j, j
    while j1 >= 0 and row[j1-1+idx].isdigit(): 
        numbers_string_list.insert(0, row[j1-1+idx])
        j1 -= 1

    while j2+1 < len_row and row[j2+idx].isdigit():
        numbers_string_list.append(row[j2+idx])
        j2 += 1

    number_integer = ''.join(numbers_string_list)

    return number_integer


def filter_slider(i, j):
    # slicing index instead of exact index

    all_numbers_list = []

    if i > 0:
        ups = example_matrix[i-1][max(j-1, 0):min(j+2, len_row)]
        for idx, up in enumerate(ups):
            all_up_row = example_matrix[i-1]
            if up.isdigit():
                number_integer = get_number_in_that_row(j, idx - (j - 1), all_up_row)
                if number_integer.isdigit():
                    all_numbers_list.append(int(number_integer))


    mids = example_matrix[i][max(j-1, 0):min(j+2, len_row)]
    for idx, mid in enumerate(mids):
        all_mid_row = example_matrix[i]
        if mid.isdigit():
            number_integer = get_number_in_that_row(j, idx - (j - 1), all_mid_row)
            if number_integer.isdigit():
                all_numbers_list.append(int(number_integer))


    if i < len_col - 1:
        bots = example_matrix[i+1][max(j-1, 0):min(j+2, len_row)]
        for idx, bot in enumerate(bots):
            all_bot_row = example_matrix[i+1]
            if bot.isdigit():
                number_integer = get_number_in_that_row(j, idx - (j - 1), all_bot_row)
                if number_integer.isdigit():
                    all_numbers_list.append(int(number_integer))

    print(all_numbers_list)
    return all_numbers_list


sum_dups = 0

for i, row in enumerate(example_matrix):
    for j, entry in enumerate(row):
        if not entry.isdigit() and entry != '.':
            print(entry)
            set_numbers_of_this_ij = filter_slider(i, j)
            sum_dups += sum(set_numbers_of_this_ij)
            

sum_dups


# In[29]:


len_row = len(example_matrix[0])
len_col = len(example_matrix)

def get_number_in_that_row(j, idx, row):
    numbers_string_list = []

    j1 = j + idx - 1
    while j1 >= 0 and row[j1].isdigit():
        numbers_string_list.insert(0, row[j1])
        j1 -= 1

    j2 = j + idx
    while j2 < len_row and row[j2].isdigit():
        numbers_string_list.append(row[j2])
        j2 += 1

    number_integer = ''.join(numbers_string_list)
    return number_integer

def filter_slider(i, j):
    all_numbers_list = []

    if i > 0:
        ups = example_matrix[i-1][max(j-1, 0):min(j+2, len_row)]
        for idx, up in enumerate(ups):
            all_up_row = example_matrix[i-1]
            if up.isdigit():
                number_integer = get_number_in_that_row(j, idx - 1, all_up_row)
                if number_integer.isdigit():
                    all_numbers_list.append(int(number_integer))

    mids = example_matrix[i][max(j-1, 0):min(j+2, len_row)]
    for idx, mid in enumerate(mids):
        all_mid_row = example_matrix[i]
        if mid.isdigit():
            number_integer = get_number_in_that_row(j, idx - 1, all_mid_row)
            if number_integer.isdigit():
                all_numbers_list.append(int(number_integer))

    if i < len_col - 1:
        bots = example_matrix[i+1][max(j-1, 0):min(j+2, len_row)]
        for idx, bot in enumerate(bots):
            all_bot_row = example_matrix[i+1]
            if bot.isdigit():
                number_integer = get_number_in_that_row(j, idx - 1, all_bot_row)
                if number_integer.isdigit():
                    all_numbers_list.append(int(number_integer))

    return all_numbers_list

sum_dups = 0

for i, row in enumerate(example_matrix):
    for j, entry in enumerate(row):
        if not entry.isdigit() and entry != '.':
            set_numbers_of_this_ij = filter_slider(i, j)
            sum_dups += sum(set(set_numbers_of_this_ij))

sum_dups


# In[33]:


import os
os.getcwd()

with open('input.txt', 'r') as f:
    inpt = [line.strip() for line in f.readlines()]

# split to get array of array or list of list (look like a matrix)
inpt = [list(line) for line in inpt]


# In[100]:


len_row = len(inpt[0])
len_col = len(inpt)

def get_number_in_that_row(j, idx, row):
    numbers_string_list = []

    j1 = j + idx - 1
    while j1 >= 0 and row[j1].isdigit():
        numbers_string_list.insert(0, row[j1])
        j1 -= 1

    j2 = j + idx
    while j2 < len_row and row[j2].isdigit():
        numbers_string_list.append(row[j2])
        j2 += 1

    number_integer = ''.join(numbers_string_list)
    return number_integer

def filter_slider(i, j):
    all_numbers_list = []

    if i > 0:
        ups = inpt[i-1][max(j-1, 0):min(j+2, len_row)]
        for idx, up in enumerate(ups):
            all_up_row = inpt[i-1]
            if up.isdigit():
                number_integer = get_number_in_that_row(j, idx - 1, all_up_row)
                if number_integer.isdigit():
                    all_numbers_list.append(int(number_integer))
            

    mids = inpt[i][max(j-1, 0):min(j+2, len_row)]
    for idx, mid in enumerate(mids):
        all_mid_row = inpt[i]
        if mid.isdigit():
            number_integer = get_number_in_that_row(j, idx - 1, all_mid_row)
            if number_integer.isdigit():
                all_numbers_list.append(int(number_integer))


    if i < len_col - 1:
        bots = inpt[i+1][max(j-1, 0):min(j+2, len_row)]
        for idx, bot in enumerate(bots):
            all_bot_row = inpt[i+1]
            if bot.isdigit():
                number_integer = get_number_in_that_row(j, idx - 1, all_bot_row)
                if number_integer.isdigit():
                    all_numbers_list.append(int(number_integer))
    print(all_numbers_list)
    return all_numbers_list

sum_dups = 0

for i, row in enumerate(inpt):
    for j, entry in enumerate(row):
        if not entry.isdigit() and not entry == '.':
            print(entry)
            set_numbers_of_this_ij = filter_slider(i, j)
            sum_dups += sum(set(set_numbers_of_this_ij))

sum_dups


# In[86]:


555197 - 556057


# In[99]:


len_row = len(inpt[0])
len_col = len(inpt)

def get_number_in_that_row(j, idx, row):
    numbers_string_list = []

    j1 = j + idx - 1
    while j1 >= 0 and row[j1].isdigit():
        numbers_string_list.insert(0, row[j1])
        j1 -= 1

    j2 = j + idx
    while j2 < len_row and row[j2].isdigit():
        numbers_string_list.append(row[j2])
        j2 += 1

    number_integer = ''.join(numbers_string_list)
    return number_integer

def filter_slider(i, j):
    all_numbers_list = []

    if i > 0:
        ups = inpt[i-1][max(j-1, 0):min(j+2, len_row)]
        for idx, up in enumerate(ups):
            all_up_row = inpt[i-1]
            if up.isdigit():
                number_integer = get_number_in_that_row(j, idx - 1, all_up_row)
                if number_integer.isdigit():
                    all_numbers_list.append(int(number_integer))
            

    mids = inpt[i][max(j-1, 0):min(j+2, len_row)]
    for idx, mid in enumerate(mids):
        all_mid_row = inpt[i]
        if mid.isdigit():
            number_integer = get_number_in_that_row(j, idx - 1, all_mid_row)
            if number_integer.isdigit():
                all_numbers_list.append(int(number_integer))


    if i < len_col - 1:
        bots = inpt[i+1][max(j-1, 0):min(j+2, len_row)]
        for idx, bot in enumerate(bots):
            all_bot_row = inpt[i+1]
            if bot.isdigit():
                number_integer = get_number_in_that_row(j, idx - 1, all_bot_row)
                if number_integer.isdigit():
                    all_numbers_list.append(int(number_integer))

    return all_numbers_list

sum_dups = 0

for i, row in enumerate(inpt):
    for j, entry in enumerate(row):
        if not entry.isdigit() and not entry == '.':
            set_numbers_of_this_ij = filter_slider(i, j)
            sum_dups += sum(set(set_numbers_of_this_ij))

sum_dups


# example try

# In[20]:


import os
os.getcwd()

with open('input.txt', 'r') as f:
    inpt = [line.strip() for line in f.readlines()]

# split to get array of array or list of list (look like a matrix)
inpt = [list(line) for line in inpt]


# In[24]:


len_row = len(inpt[0])
len_col = len(inpt)

def get_number_in_that_row(j, idx, row):
    numbers_string_list = []

    j1 = j + idx - 1
    while j1 >= 0 and row[j1].isdigit():
        numbers_string_list.insert(0, row[j1])
        j1 -= 1

    j2 = j + idx
    while j2 < len_row and row[j2].isdigit():
        numbers_string_list.append(row[j2])
        j2 += 1

    number_integer = ''.join(numbers_string_list)
    return number_integer

def filter_slider(i, j):
    all_numbers_list = []

    if i > 0:
        ups_start = max(j-1, 0)
        ups_end = min(j+2, len_row)
        ups = list(inpt[i-1][ups_start:ups_end])  # Convert to list to modify elements
        for idx, up in enumerate(ups):
            all_up_row = inpt[i-1]
            if up.isdigit():
                number_integer = get_number_in_that_row(j, idx - 1, all_up_row)
                if number_integer.isdigit():
                    all_numbers_list.append(int(number_integer))
                    for k in range(len(number_integer)):
                        if 0 <= idx - 1 + k < len(ups):
                            ups[idx - 1 + k] = '.'

    mids_start = max(j-1, 0)
    mids_end = min(j+2, len_row)
    mids = list(inpt[i][mids_start:mids_end])  # Convert to list to modify elements
    for idx, mid in enumerate(mids):
        all_mid_row = inpt[i]
        if mid.isdigit():
            number_integer = get_number_in_that_row(j, idx - 1, all_mid_row)
            if number_integer.isdigit():
                all_numbers_list.append(int(number_integer))
                for k in range(len(number_integer)):
                    if 0 <= idx - 1 + k < len(mids):
                        mids[idx - 1 + k] = '.'

    if i < len_col - 1:
        bots_start = max(j-1, 0)
        bots_end = min(j+2, len_row)
        bots = list(inpt[i+1][bots_start:bots_end])  # Convert to list to modify elements
        for idx, bot in enumerate(bots):
            all_bot_row = inpt[i+1]
            if bot.isdigit():
                number_integer = get_number_in_that_row(j, idx - 1, all_bot_row)
                if number_integer.isdigit():
                    all_numbers_list.append(int(number_integer))
                    for k in range(len(number_integer)):
                        if 0 <= idx - 1 + k < len(bots):
                            bots[idx - 1 + k] = '.'

    print(all_numbers_list)
    return all_numbers_list

sum_dups = 0

for i, row in enumerate(inpt):
    for j, entry in enumerate(row):
        if not entry.isdigit() and not entry == '.':
            set_numbers_of_this_ij = filter_slider(i, j)
            sum_dups += sum(set(set_numbers_of_this_ij))

sum_dups


# part 2

# In[40]:


# example first
import math

len_row = len(example_matrix[0])
len_col = len(example_matrix)

def get_number_in_that_row(j, idx, row):
    numbers_string_list = []

    j1 = j + idx - 1
    while j1 >= 0 and row[j1].isdigit():
        numbers_string_list.insert(0, row[j1])
        j1 -= 1

    j2 = j + idx
    while j2 < len_row and row[j2].isdigit():
        numbers_string_list.append(row[j2])
        j2 += 1

    number_integer = ''.join(numbers_string_list)
    return number_integer

def filter_slider(i, j):
    all_numbers_list = []

    if i > 0:
        ups = example_matrix[i-1][max(j-1, 0):min(j+2, len_row)]
        for idx, up in enumerate(ups):
            all_up_row = example_matrix[i-1]
            if up.isdigit():
                number_integer = get_number_in_that_row(j, idx - 1, all_up_row)
                if number_integer.isdigit():
                    all_numbers_list.append(int(number_integer))

    mids = example_matrix[i][max(j-1, 0):min(j+2, len_row)]
    for idx, mid in enumerate(mids):
        all_mid_row = example_matrix[i]
        if mid.isdigit():
            number_integer = get_number_in_that_row(j, idx - 1, all_mid_row)
            if number_integer.isdigit():
                all_numbers_list.append(int(number_integer))

    if i < len_col - 1:
        bots = example_matrix[i+1][max(j-1, 0):min(j+2, len_row)]
        for idx, bot in enumerate(bots):
            all_bot_row = example_matrix[i+1]
            if bot.isdigit():
                number_integer = get_number_in_that_row(j, idx - 1, all_bot_row)
                if number_integer.isdigit():
                    all_numbers_list.append(int(number_integer))

    return all_numbers_list

sum_dups = 0

for i, row in enumerate(example_matrix):
    for j, entry in enumerate(row):
        if entry == "*":
            set_numbers_of_this_ij = filter_slider(i, j)
            if len(set(set_numbers_of_this_ij)) == 2:
                sum_dups += math.prod(set(set_numbers_of_this_ij))

sum_dups


# In[78]:


len_row = len(inpt[0])
len_col = len(inpt)

def get_number_in_that_row(j, idx, row):
    numbers_string_list = []

    j1 = j + idx - 1
    while j1 >= 0 and row[j1].isdigit():
        numbers_string_list.insert(0, row[j1])
        j1 -= 1

    j2 = j + idx
    while j2 < len_row and row[j2].isdigit():
        numbers_string_list.append(row[j2])
        j2 += 1

    number_integer = ''.join(numbers_string_list)
    return number_integer

def filter_slider(i, j):
    all_numbers_list = []

    if i > 0:
        ups = inpt[i-1][max(j-1, 0):min(j+2, len_row-1)]
        for idx, up in enumerate(ups):
            all_up_row = inpt[i-1]
            if up.isdigit():
                number_integer = get_number_in_that_row(j, idx - 1, all_up_row)
                if number_integer.isdigit():
                    all_numbers_list.append(int(number_integer))
                break

    mids = inpt[i][max(j-1, 0):min(j+2, len_row-1)]
    for idx, mid in enumerate(mids):
        all_mid_row = inpt[i]
        if mid.isdigit():
            number_integer = get_number_in_that_row(j, idx - 1, all_mid_row)
            if number_integer.isdigit():
                all_numbers_list.append(int(number_integer))
            break

    if i < len_col - 1:
        bots = inpt[i+1][max(j-1, 0):min(j+2, len_row-1)]
        for idx, bot in enumerate(bots):
            all_bot_row = inpt[i+1]
            if bot.isdigit():
                number_integer = get_number_in_that_row(j, idx - 1, all_bot_row)
                if number_integer.isdigit():
                    all_numbers_list.append(int(number_integer))
                break

    return all_numbers_list

sum_dups = 0

for i, row in enumerate(inpt):
    for j, entry in enumerate(row):
        if not entry.isdigit() and not entry == '.':
            set_numbers_of_this_ij = filter_slider(i, j)
            if len(set(set_numbers_of_this_ij)) == 2:
                sum_dups += math.prod(set(set_numbers_of_this_ij))

sum_dups


# In[79]:


69192889 - 82824352


# In[63]:


import re
from typing import List, Tuple

# Open the file and read the lines into a list
lines: List[str] = open("./input.txt").read().splitlines()


def is_symbol(char: str) -> bool:
    """
    Checks if a character is a symbol.

    Parameters:
    char (str): The character to check.

    Returns:
    bool: True if the character is a symbol, False otherwise.
    """
    return char != "." and not char.isdigit()


def get_parts() -> List[List[Tuple[int, int, int]]]:
    """
    Extracts the parts from the lines.

    Returns:
    List[List[Tuple[int, int, int]]]: A list of parts for each line.
    """
    parts: List[List[Tuple[int, int, int]]] = []
    for i, line in enumerate(lines):
        parts.append([])

        # Find all numbers in the line
        for match in re.finditer(r"\d+", line):
            start_index = match.start(0) - 1
            end_index = match.end(0)
            number = int(match.group(0))
            part = (start_index, end_index, number)
            parts[i].append(part)

    return parts


count = 0
parts: List[List[Tuple[int, int, int]]] = get_parts()

for i, line in enumerate(lines):
    for j, char in enumerate(line):
        if char != "*":
            continue

        adjacent_parts: List[int] = []

        # Loop over the line above, the current line, and the line below
        for k in range(-1, 2):
            # Check if the line exists
            if i + k < 0 or i + k > len(lines):
                continue

            # Loop over each part in the line
            for start_index, end_index, number in parts[i + k]:
                if start_index <= j <= end_index:
                    adjacent_parts.append(number)

        # If there are two adjacent parts, multiply them and add to the count
        if len(adjacent_parts) == 2:
            count += adjacent_parts[0] * adjacent_parts[1]

print(count)

