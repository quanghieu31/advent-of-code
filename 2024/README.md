### Day 1
(30 mins)
- sorting takes O(nlogn) runtime, but running through the nested loop for two list takes O(n^2) which is not very good
- better way to deal with O(n^2):
    - `collection.Counter` only takes O(n) (why? Counter is just a subclass of dict. Constructing it is O(n), because it has to iterate over the input, but operations on individual elements remain O(1).)

### Day 2
(1 hour)
- if there are multiple conditions, a brute force way is to check each condition by condition
- `all`, `map`, `lambda` are very useful for conditional checking
- reuse while manipulating an object:
```python
    for idx in range(len(line)):
        # ln = line.copy()
        # ln.remove(line[idx])
        ln = line[:idx] + line[idx+1:]
```
| `.copy() + .remove()`                         | Slicing (`[:idx] + [idx+1:]`)           |
|-----------------------------------------------|-----------------------------------------|
| Modifies a copy of the list in-place          | Creates a new list                      |
| Removes the first occurrence of the value     | Removes the element by index            |
| \( O(n) \), slower for large lists with duplicates | \( O(n) \), faster for index removal|


### Day 3
(30 mins)
I knew regex would appear at some point-- still a regex noob. `mul\((\d+),(\d+)\)`

- `mul\(`: matches the text "mul(" 
- `(\d+)`: captures one or more digits as the first group
- `,`: matches a comma
- `(\d+)`: captures one or more digits as the second group
- `\)`: matches the closing parenthesis

### Day 4
(1 hour)
- If can't think of better way, brute force but with <u>**careful conditions**</u>:
    - If there is no X at the starting index, ignore immediately
    - 8 directions (2 for rows, 2 for cols, and 4 for diagonal)
- A possible better way:
```python
directions = [
    (0, 1), (0, -1),                    # horizontal
    (1, 0), (-1, 0),                    # vertical
    (1, 1), (-1, -1), (1, -1), (-1, 1)  # diagonal
]
```

### Day 5
(45 mins)
- Brute force with three `for` loops again worked but not efficiently as look-up runtime is $O(M×L×O)$ and lots of redundant operations
- Set look up is only O(1). https://stackoverflow.com/a/44080017/19562762

### Day 6 
(1 hour) 
- Brute force with lots of inherent logics/conditions to think about. Using a `history` list to keep track of the previous values, but not sure if this is optimal
- A more intuitve way to write direction (vertical and horizontally only) => as a dictionary
```python
directions = {
    "^": (-1, 0),
    ">": (0, 1),
    "v": (1, 0),
    "<": (0, -1),
}
```
- Convert a list of lists into a numpy grid that we can get/set/del with `grid[i, j]`: `np.array([list(line) for line in f.read().split()])`
- unpacking: `grid[*(i, j)]`
