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

Day 4: 96 hours
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

Day 5: seems hard
this is niche
```python
for i in range(range_length):
    start = third_list[1]
    destination = third_list[0]
    soil_ferti[start + i] = destination + i
```