########## read input
import re
from collections import defaultdict

input_file = '2023/day15/example.in'
with open(input_file, 'r') as f:
    sequence = f.read().split(',')

# part 1 is too easy, part 2 is building a hashmap, more complicated

########### hash algo
def hash(key, label_letters):

    hash_bucket = 0

    for char in label_letters:
        ascii_code = ord(char)
        hash_bucket += ascii_code
        hash_bucket *= 17
        hash_bucket %= 256

    return hash_bucket


############ build hash map
hash_map = defaultdict(list)

for key in sequence:
    
    # bucket code
    label_letters = "".join(re.findall('[A-Za-z]', key))
    bucket_code = hash(key, label_letters)
    # non-letter characters
    non_letters = re.findall('[^A-Za-z]', key)

    # - operation
    if '-' in non_letters:
        if hash_map.get(bucket_code, 0):
            for member in hash_map[bucket_code]:
                if label_letters in member:
                    hash_map[bucket_code].remove(member)
    
    # = operation
    elif '=' in non_letters:
        focal_length = non_letters[-1]
        
        if hash_map.get(bucket_code, 0):

            if any(label_letters in x for x in hash_map[bucket_code]) is False:
                new_member = f"{label_letters} {focal_length}"
                hash_map[bucket_code].append(new_member)

            else:
                for idx, member in enumerate(hash_map[bucket_code]):
                    if label_letters in member:
                        new_member = label_letters + ' ' + focal_length
                        hash_map[bucket_code].insert(idx, new_member)
                        hash_map[bucket_code].remove(member)
                        break

        else:
            new_member = label_letters + ' ' + focal_length
            hash_map[bucket_code].append(new_member)


############# compute power

s2 = 0
for hash_code, members in hash_map.items():
    for idx, member in enumerate(members):
        power = (hash_code+1) * (idx+1) * int(re.findall('\d+', member)[0])
        s2 += power

# part 1: 508552
# part 2: 265462


