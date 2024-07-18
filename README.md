My solutions to https://adventofcode.com/2023.

### Day 1: 1 hour
- find digits in string: re.findall("\d+", line) = a list
- do the loop iteration carefully, especially with indices inside string

### Day 2: 2 hours
- read the prompt carefully
- use a flag=True and if a violation is met, the flag=False => deal with the violation or break the loop (think about how many loops needed to be broken for optimization)
- dict.get(key, 0) is very helpful
- helpful reduce functools i.e. def mul(x,y) then reduce(mul, [1,2,3])
- always start from some examples to understand

### Day 3: 36 hours
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

### Day 4: 96 hours
- two-pointer technique
- Stack: LIFO (push O(1), pop O(1), find O(n)), Queue: FIFO (enqueue O(1), dequeue O(1), find O(n))
- Dequeue: EIEIO (Enforce in-order execution of I/O)
    - insertLeft(element): insert element into leftmost position ~ push() O(1)
    - insertRight(element): insert element into rightmost position ~ push() O(1)
    - deleteLeft(): removes and returns the leftmost element ~ pop() O(1)
    - deleteRight(): removes and returns the rightmost element ~ pop() O(1)
    - lookup O(n)
- Deque implementation:
    - Using doubly linked list DS:
        - A node has two pointers (pointing to previous node and next node), the first node's prev pointer pointing to 'null'
        - or `head` and `tail` pointers
        - appendLeft, append, popLeft, pop = all is O(1)
    - Using dynamic array:
        - Just a list operation (insert(0, element) ~ O(n) due shifting elements, append(element) ~ O(1), pop(0) ~ O(n) due to shifting, pop() ~ O(1))
- When to use deque:
    - sliding window problems - eficiently add and remove elements from both ends in a fixed-size window.
    - palindrome checking: compare elements from both ends to check for palindromes.
    - maintaining order with quick access: access elements at both ends while maintaining order efficiently.
    - BFS - manage the list of nodes to be explored next in graph traversal.
    - implement cache with limited size - manage cache with operations at both ends (e.g., LRU cache).
- Dynamic programming (DP)
    - bottom-up approach: i.e., initialize `card_instances` with all ones, then `cards_instances[card_num + idx] += cards_instances[card_num - 1]`
    - when to use:
        - overlapping subproblems (i.e. Fibo - $F(n-1)+F(n-2)$ subproblems overlap)
        - optimal structure (i.e. shortest path using Dijkstra where the shortest path to a node can be found using shortest paths to its neighbors)
        - memoization (top down - default dictionary): store results of expensive function calls and return cached result when same inputs occur again (recursion)
        - tabulation (bottom up - fill in table): build a table of solutions to subprobs iteratively (for loop)
        - sequential decision-making (i.e. knapsack or edit distance)
    - examples:
        - substring/subsequence problem (longest common subsequence)
        - combinatorial probs (counting no. ways of doing sth: climb stairs using 1 or 2-step)
        - optimization (longest increasing subsequences in an array)
        - partition (divide a set into subsets to satisfy certain conditions, i.e. 2 subsets of equal sum)
        - pathfinding (left corner to right top corner...)
    - (1) define subprobs, (2) base cases, (3) recurrences of different cases (0 or 1) 
        - define: $dp[i][w]$ is the max value of $i$-th items given limit of the knapsack of $w$ kg.
        - i.e. $dp[i][w] = max(dp[i-1][w], dp[i-1][w-weight_of_item[i]] + value[i]$
        - base case: $dp[0][w] = 0$ for all $w$
- **Please use regex for pattern recognition**
- Brilliant, simple to get the common/shared elements with set operations: `common_elements_count = len(set(group1_numbers) & set(group2_numbers))`

### Day 5: seems hard
this is niche
```python
for i in range(range_length):
    start = third_list[1]
    destination = third_list[0]
    soil_ferti[start + i] = destination + i
```
- `str.split()` is almost in every problem so far => might need a better way to optimize this?
- `defaultdict` and `dict.get()` always come in handy and nice
- really understanding the problem is important (the wording is a bit challenging to me) 
    - start from example and really make sure you got the correct example solution
- my solution for part was too slow (4 minutes) -> fixed:
    - instead of creating a nested dictionary that I had (with intent to retrieve)
    - I checked if the given seed is in the range from source_start to source_end (=source_start+range) or not
        - if yes, nice! go fetch the next source (soil), and so on
        - if no, keep it as it, aka soil=seed
- utilize `map` for function utility
- beware of range and index (my weakness)
- Sometimes, building everything-then-retrieve solution is much slower than given-input-to-check-and-then-result
- Part 2 took too much time! => need to optimize

### Day 6: Surprisingly easy

### Day 7: 
- a dataframe's column can be sorted by tuples
- Python automatically sorts by elements (i.e. first then second then next)
- multi-dimensional data may be best handled with a dataframe as a data structure
- TODO: my current solution will be optimized and part 2 will be done soon

### Day 8:
- again, `defaultdict` is amazing
- to organize code better, do three things consecutively: process_input(), functions learned from example, and input simply
- if there is a `for` loop in `while` loop, the `while` loop continues to run a new iteration of `for` loop if it still does not reach the false condition.
- Part 2: no way brute force gives a fast result. I think a BFS or LCM solution might work, part 2 surprisingly takes so much time
<details>

<summary>Reddit's suggested ideas for using least common multiplier assumptions and solutions</summary>

source: https://www.reddit.com/r/adventofcode/comments/18dtmin/comment/kckf5jg/?utm_source=share&utm_medium=web3x&utm_name=web3xcss&utm_term=1&utm_content=share_button

## Observations:

### Cycle Detection:
Each ghost will eventually reach a cycle. The system's state can be described as (currentNode, instructionIndex). When the same state repeats, the ghost is on a cycle since the directions and nodes will repeat identically. Finite nodes and instructions guarantee this repetition.

### Ghost Convergence:
If two ghosts starting from different locations meet at the same node simultaneously, they enter the same cycle and will follow identical future paths. This allows for an optimization: post-meeting, one ghost can be disregarded in calculations, as their states will be identical.

## Assumptions:

### Existence of a Solution:
A solution exists where each ghost’s cycle includes at least one destination. If a ghost reaches the destination before entering its cycle, the problem becomes trivial and solvable by brute force.

### Single Destination in Cycle:
Each ghost’s cycle has one destination. This holds for the given input, though it can be relaxed for more complex solutions.

## Reformulated Problem:
Each ghost $G_i$ reaches the destination within its cycle for the first time after $S_i$ steps, repeating with a cycle length $L_i$. The smallest number $N$ such that $N = S_i + L_i \times x_i$ for each ghost $i$ (where $x_i$ is the number of cycle loops) is the solution.

## Special Case Analysis:

### $S_i = 0$:
If $S_i = 0$ for every ghost $i$, $N$ is an integer multiple of every cycle length $L_i$. The minimum $N$ is the least common multiple (LCM) of the cycle lengths.

### $S_i = k_i \times L_i$:
When $S_i = k_i \times L_i$ (with integer $k_i$), $N$ can be expressed as $L_i \times (x + k_i)$, making $N$ an integer multiple of the cycle length.

For the given problem, $S_i = L_i$, making the LCM the correct answer. If the starting offset isn't an integer multiple of the cycle length, the solution might require the Chinese Remainder Theorem or similar methods.

</details>

### Day 9: 
- I tried using `reduce(lambda a,b: b-a, sequence)` but it turns out to be inefficient and incorrect. We need to check all elements in sequence are 0, and `all(x == 0 for x in sequence)` works.
- `while` loop comes in handy and remember to do the flag carefully
- `for idx, seq in reversed(list(enumerate(all_sequences_incl_hist)))`: No copy is created, the elements are reversed on the fly while traversing => very efficient
- `deque` for inserting to beginning which takes O(1) with `appendleft(ele)`

### Day 10:
- Try: 
    - Find connected components from these elements
    - Then see which one has a cycle?
    - First: Cycle detection - find all cycles/loops in this graph (start and end at same vertex) using BFS/DFS
        - Then: Got a cycle, find the path from S to the farthest point possible (how)
    - Second: Cycle detection but with topological sorting
- please look at solution on this day, very important, [here](https://github.com/quanghieu31/adventofcode/blob/main/2023/day10/solution.py) and reference to [this one](https://advent-of-code.xavd.id/writeups/2023/day/10/)
- **Note the grid data structure** = a map of coordinate (indices of row and column) and its value

### Day 11: 
- "Shortest path": first thought - Dijkstra's Algo
    - but seems not necessary in this case because the path is just up/down/left/right and so the shortest path can be i.e. all steps down then all steps right
    - so, the problem should be about visualizing a rectangle based on the two points on grid and sum the one width and one height
    - this is also called the Manhattan distance
- transpose a list of list (rows of cols) into ("cols" of "rows"): `transposed = list(map(list, zip(*rows)))`
    - transpose a 2d array (list of list) 
    - the `*` unpacks the elements inside the main list or the inner lists
    - `zip` pairs up the elements consequentially from each inner list into tuples: i.e. `[[a, b, c], [d, e, f], [g, h, i]]` then zip the pairs consequentially like (a,d,g) as first pair, then (b,e,h) second, so on, and result is `[(a, d, g), (b, e, h), (c, f, i)]`
- build a grid from 2d array (very efficiently)
    ```python
    GridPoint = tuple[int, int]     # a tuple of two integers = cooridinate
    Grid = dict[GridPoint, str]     # the keys are GridPoints and the values are strings

    def parse_grid(array2d: list[list]) -> Grid:
        grid_dict = {}
        for row, line in enumerate(array2d):
            for col, ele in enumerate(line):
                grid_dict[(row, col)] = ele

        # assign unique_number for galaxy (for this Day puzzle only)
        unique_number = 1
        for k, v in grid_dict.items():
            if v == "#":
                grid_dict[k] = unique_number
                unique_number += 1

        return grid_dict
    ```
- find shortest Manhattan path if the only movement is 1-step increment on a grid
    ```python
    # shortest_path function between two given coords on a grid
    def shortest_path(coord_g1, coord_g2):
        height = coord_g1[0] - coord_g2[0]
        width = coord_g1[1] - coord_g2[1]
        shortest_steps = abs(height) + abs(width)
        return shortest_steps
    ```
- Day 2 needs better way to handle the iterations and looping 1,000,000 empty rows/cols (instead of manually creating all, just assign the incremented coordinate for non-empty rows, cols). Review [this one](https://github.com/quanghieu31/adventofcode/blob/main/2023/day11/shorter_solution.py).

### Day 12:
- This puzzle is the hardest I ever seen. Reddit says it involves recursion and DP but honestly I need to figure out how!

### Day 13:
- A great code for checking reflection between rows using generator (cost efficient). `zip` pairs elements from two lists together until the shorter one is exhausted.
    ```python
    def reflection_row(block: list[str]) -> int:
        n_rows, n_cols = len(block), len(block[0])

        for idx in range(1, n_rows):
            up = block[:idx]
            bot = block[idx:]
            if all(l == r for l, r in zip(reversed(up), bot)):
                return idx

        return 0

    def reflection_column(block: list[str]) -> int:

        transposed_list = list(map(list, zip(*block)))
        transposed_strings = ["".join(row) for row in transposed_list]

        return reflection_row(transposed_strings)
    ```
- Again, tranposing is handy: `transposed = list(map(list, zip(*rows)))`

### Day 14:
- It seems doing things in rows is more comfortable than in columns given a grid puzzle!
- Remember:
    ```python
    while idx > 0 and col[idx-1] == '.':
        col[idx-1], col[idx] = col[idx], col[idx-1]  # swap 'O' with '.' 
        # => must be same code line, not different code line
        idx -= 1  # check further left
    ```
- `zip` is again very helpful for transposing, or want to something parallel given two iterables


### Day 15:
- Two stars easily, this one is simply building a hashmap carefully following the instruction:
- Remember: extracting characters with regex is helpful with `re.findall(pattern, string)` and (`\d+`, `[a-zA-Z]`,...). 


### Day 16: Skip for now


### Day 17: It's Dijkstra, my old friend!
- read references and help with this puzzle