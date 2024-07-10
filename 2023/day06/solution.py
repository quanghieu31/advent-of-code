#!/usr/bin/env python
# coding: utf-8

# # Part 1

# ## Example

import re # \d+ find integers

with open('example.in', 'r') as f:
    lines = [line.strip().split() for line in f.readlines()]
    total_times, record_distances = list(map(int, lines[0][1:])), list(map(int, lines[1][1:]))

margins = 1

for total_time, record_distance in zip(total_times, record_distances):
    count_beat_record = 0
    for hold_time in range(total_time + 1):
        speed = hold_time
        remain_time = total_time - hold_time
        distance_travelled = remain_time * speed
        if distance_travelled > record_distance:
            count_beat_record += 1
    margins *= count_beat_record

margins


# ## Input

import re # \d+ find integers

with open('input.in', 'r') as f:
    lines = [line.strip().split() for line in f.readlines()]
    total_times, record_distances = list(map(int, lines[0][1:])), list(map(int, lines[1][1:]))

margins = 1

for total_time, record_distance in zip(total_times, record_distances):
    count_beat_record = 0
    for hold_time in range(total_time + 1):
        speed = hold_time
        remain_time = total_time - hold_time
        distance_travelled = remain_time * speed
        if distance_travelled > record_distance:
            count_beat_record += 1
    margins *= count_beat_record

margins


# # Part 2

with open('input.in', 'r') as f:
    lines = [line.strip().split() for line in f.readlines()]
    total_time, record_distance = int(''.join(lines[0][1:])), int(''.join(lines[1][1:]))

margins = 1
count_beat_record = 0

for hold_time in range(total_time + 1):
    speed = hold_time
    remain_time = total_time - hold_time
    distance_travelled = remain_time * speed
    if distance_travelled > record_distance:
        count_beat_record += 1
margins *= count_beat_record

margins   # 8s

