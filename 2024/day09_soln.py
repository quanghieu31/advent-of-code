from utils import read_raw_input

with open(read_raw_input("day09"), 'r') as f:
    rawinput = f.read()

# unpushed = []
# idn = "0"
# for idx, num in enumerate(rawinput):
#     if idx % 2 == 0:
#         unpushed.append(idn * int(num))
#         idn = str(int(idn) + 1)
#     elif idx % 2 == 1:
#         unpushed.append('.' * int(num))

# full = list(''.join(unpushed))
# reversed_full = list(reversed(full))

# for idx, num1 in enumerate(reversed_full):
#     if num1 != ".":
#         full[-idx-1] = "."
#         for idx, num2 in enumerate(full):
#             if num2 == ".":
#                 full[idx] = num1
#                 break

# checksum = 0
# for idx, num in enumerate(full):
#     if num != '.':
#         checksum += idx * int(num)
    
# print(checksum)


from collections import deque

lengths = [int(num) for num in rawinput]

filled_grid = deque()
moved_grid = deque()
gaps = deque()

cur_pos = 0
for i,num in enumerate(lengths):
    if i%2 == 0:
        filled_grid.append([i//2,cur_pos,num])
    else:
        if num > 0:
            gaps.append([cur_pos,num])
    cur_pos += num

while True:
    gap_pos,gap_len = gaps.popleft()
    file_id,file_pos,file_len = filled_grid.pop()
    if gap_pos > file_pos:
        filled_grid.append([file_id,file_pos,file_len])
        break
    if gap_len > file_len:
        moved_grid.append([file_id,gap_pos,file_len])
        gaps.appendleft([gap_pos+file_len,gap_len-file_len])
    elif gap_len == file_len:
        moved_grid.append([file_id,gap_pos,file_len])
    else:
        moved_grid.append([file_id,gap_pos,gap_len])
        filled_grid.append([file_id,file_pos,file_len-gap_len])
    
final_grid = filled_grid + moved_grid
checksum = sum(num*(start*length+(length*(length-1))//2) for num,start,length in final_grid) # (start) + (start+1) + ... + (start+length-1)
print(checksum)