### Day 1
(30 mins)
- sorting takes O(nlogn) runtime, but running through the nested loop for two list takes O(n^2) which is not very good
- better way to deal with O(n^2):
    - `collection.Counter` only takes O(n) (why? Counter is just a subclass of dict. Constructing it is O(n), because it has to iterate over the input, but operations on individual elements remain O(1).)