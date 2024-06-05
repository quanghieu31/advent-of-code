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

