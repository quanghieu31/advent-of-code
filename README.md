My solutions to https://adventofcode.com/2023.

Day 1: 1 hour
- find digits in string: re.findall("\d+", line) = a list
- do the loop iteration carefully, especially with indices inside string

Day 2: 2 hours
- read the prompt carefully
- use a flag=True and if a violation is met, the flag=False => deal with the violation or break the loop (think about how many loops needed to be broken for optimization)
- dict.get(key, 0) is very helpful
- helpful reduce functools i.e. def mul(x,y) then reduce(mul, [1,2,3])
- always start from some examples to understand

Day 3: 36 hours
- adjacency index is hard
- my approach (not sure if it is the most optimized)
    - I consider the input as array of arrays or list of lists where each list/array is a line in input
    - Run a loop with a filter slider: check each entry if the entry is not a period or not a digit.
    - For each entry: the filter slider checks 8 points surrounding it (3 ups, 2 beside mids, 3 bots). 
- well utilized: 
    - `enumerate(array)` to use both indices and values
    - sliding a list to avoid out of range error: given (i,j) where j represents column indices, for example, check 3 numbers (up, bot) and 2 numbers (mid), utilize the left edge which is 0 or right edge is len_row, then max or min:
        - `ups = inpt[i-1][max(j-1, 0):min(j+2, len_row)]`
        - `bots = inpt[i+1][max(j-1, 0):min(j+2, len_row)]`
        - `inpt[i][max(j-1, 0):min(j+2, len_row)]`
    - keep original ordering with `lst.insert(0, value)`
- struggled
    - My answer is lower than expected one. I think the reason is likely because of this `* [897, 897, 847, 847]` from the full input. More than 1 hour failing to fix this. Skip for now. 

Day 4:    
Two-pointer technique