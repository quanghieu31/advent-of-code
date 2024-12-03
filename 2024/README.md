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

