#!/usr/bin/env python
# coding: utf-8

# ## Solution part 1

# ### Original

# In[44]:


with open('input.txt', 'r') as f:
    lines = [line.strip() for line in f.readlines()]

map_names = ["seed-to-soil map:", "soil-to-fertilizer map:", "fertilizer-to-water map:", "water-to-light map:", "light-to-temperature map:", "temperature-to-humidity map:", "humidity-to-location map:"]

seeds = [int(ele) for ele in lines[0].split(' ')[1:]]
lines = lines[2:]

# construct maps info
from collections import defaultdict
maps_info = defaultdict(list)
len_lines = len(lines)

for idx, val in enumerate(lines):
    if val in map_names:
        next_idx = idx + 1
        while next_idx < len_lines and lines[next_idx]:
            info = tuple(map(int, lines[next_idx].split()))
            maps_info[val].append(info)
            next_idx += 1

# create actual maps from maps info
def get_maps(maps_info):

    almanac = defaultdict(dict)

    for key, val in maps_info.items():
        # each map has:
        map_dict_for_this_key = defaultdict(int)

        for lst in val:
            # in each list, has
            range_length = lst[2]
            start = lst[1]
            desti = lst[0]
            for step in range(range_length):
                map_dict_for_this_key[start + step] = desti + step

        # done with this
        almanac[key] = map_dict_for_this_key

    return almanac


# In[45]:


maps_info


# In[ ]:


almanac = get_maps(maps_info)


# ```
# ---------------------------------------------------------------------------
# KeyboardInterrupt                         Traceback (most recent call last)
# Cell In[46], line 1
# ----> 1 almanac = get_maps(maps_info)
# 
# Cell In[44], line 37
#      35     desti = lst[0]
#      36     for step in range(range_length):
# ---> 37         map_dict_for_this_key[start + step] = desti + step
#      39 # done with this
#      40 almanac[key] = map_dict_for_this_key
# 
# KeyboardInterrupt: 
# ```

# ### Cl

# In[ ]:


from collections import defaultdict

def read_input(file_path):
    with open(file_path, 'r') as f:
        lines = [line.strip() for line in f]
    
    seeds = [int(ele) for ele in lines[0].split()[1:]]
    return seeds, lines[2:]

def parse_maps(lines):
    maps_info = defaultdict(list)
    current_map = None
    
    for line in lines:
        if line.endswith("map:"):
            current_map = line
        elif line and current_map:
            dest_start, source_start, range_length = map(int, line.split())
            maps_info[current_map].append((source_start, dest_start, range_length))
    
    return maps_info




def apply_mapping(value, mappings):
    for source_start, dest_start, range_length in mappings:
        if source_start <= value < source_start + range_length:
            return dest_start + (value - source_start)
    return value

def process_seed(seed, almanac):
    for map_name in ["seed-to-soil map:", "soil-to-fertilizer map:", "fertilizer-to-water map:", 
                     "water-to-light map:", "light-to-temperature map:", "temperature-to-humidity map:", 
                     "humidity-to-location map:"]:
        seed = apply_mapping(seed, almanac[map_name])
    return seed

def find_lowest_location(seeds, almanac):
    return min(process_seed(seed, almanac) for seed in seeds)


seeds, lines = read_input('input.txt')
almanac = parse_maps(lines)
lowest_location = find_lowest_location(seeds, almanac)
print(f"Lowest location number: {lowest_location}")


# ### Fixed for faster
# 
# Not use nested dictionary, instead=get results directly

# In[ ]:


with open('input.txt', 'r') as f:
    lines = [line.strip() for line in f.readlines()]

    seeds = [int(ele) for ele in lines[0].split(' ')[1:]]
    lines = lines[2:]

map_names = ["seed-to-soil map:", "soil-to-fertilizer map:", "fertilizer-to-water map:", "water-to-light map:", "light-to-temperature map:", "temperature-to-humidity map:", "humidity-to-location map:"]

# construct maps info
from collections import defaultdict
maps_info = defaultdict(list)
len_lines = len(lines)
for idx, val in enumerate(lines):
    if val in map_names:
        next_idx = idx + 1
        while next_idx < len_lines and lines[next_idx]:
            rules_mapping = tuple(map(int, lines[next_idx].split()))
            maps_info[val].append(rules_mapping)
            next_idx += 1


# create maps inside these temporarily
def get_location(seed):

    chosen_source = seed

    # loop over dictionary of list of tuples of rules_mapping
    for lst in maps_info.values():

        # loop over list of tuples of rules_mapping
        for rules_mapping in lst:
        
            desti_bat_dau, source_bat_dau, range_length = rules_mapping
            if source_bat_dau <= chosen_source < source_bat_dau + range_length:
                # distance
                dist_betw_source_and_source_bat_dau = chosen_source - source_bat_dau
                # desti_bat_dau + distance
                chosen_source = desti_bat_dau + dist_betw_source_and_source_bat_dau  # update source
                
                # if there is a satisfying value, exit the rules_mapping loop (for rules_mapping in lst:), and go to next lst (map)
                break

    return chosen_source

min(map(get_location, seeds))


# ## Solution part 2

# In[47]:


with open('input.txt', 'r') as f:
    lines = [line.strip() for line in f.readlines()]

    seeds = [int(ele) for ele in lines[0].split(' ')[1:]]
    lines = lines[2:]

map_names = ["seed-to-soil map:", "soil-to-fertilizer map:", "fertilizer-to-water map:", "water-to-light map:", "light-to-temperature map:", "temperature-to-humidity map:", "humidity-to-location map:"]


# In[1]:


from collections import defaultdict

with open('input.txt', 'r') as f:
    lines = [line.strip() for line in f.readlines()]

    seed_ranges = [int(ele) for ele in lines[0].split()[1:]]
    lines = lines[2:]

map_names = ["seed-to-soil map:", "soil-to-fertilizer map:", "fertilizer-to-water map:", "water-to-light map:", "light-to-temperature map:", "temperature-to-humidity map:", "humidity-to-location map:"]

# construct maps info
maps_info = defaultdict(list)
len_lines = len(lines)
for idx, val in enumerate(lines):
    if val in map_names:
        next_idx = idx + 1
        while next_idx < len_lines and lines[next_idx]:
            rules_mapping = tuple(map(int, lines[next_idx].split()))
            maps_info[val].append(rules_mapping)
            next_idx += 1

def get_location(seed):
    chosen_source = seed

    for lst in maps_info.values():
        for rules_mapping in lst:
            desti_bat_dau, source_bat_dau, range_length = rules_mapping
            if source_bat_dau <= chosen_source < source_bat_dau + range_length:
                dist_betw_source_and_source_bat_dau = chosen_source - source_bat_dau
                chosen_source = desti_bat_dau + dist_betw_source_and_source_bat_dau
                break

    return chosen_source

def find_lowest_location(seed_ranges):
    lowest_location = float('inf')
    for i in range(0, len(seed_ranges), 2):
        start, length = seed_ranges[i], seed_ranges[i+1]
        for seed in range(start, start + length):
            location = get_location(seed)
            lowest_location = min(lowest_location, location)
    return lowest_location

lowest_location = find_lowest_location(seed_ranges)
print(f"Lowest location number: {lowest_location}")

