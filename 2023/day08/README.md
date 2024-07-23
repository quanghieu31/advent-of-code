# Part 1


```python
# define funcs

from collections import defaultdict
import re

def process_input(file):
    with open(file, 'r') as f:
        network_dict = defaultdict(tuple)
        lines = [line.strip() for line in f.readlines()]

        instruction = lines[0]
        network = lines[2:]

        for line in network:
            k = line.split('=')[0].strip()
            bracket = line.split('=')[1].split(',')
            instr = tuple(''.join(re.findall("\w", element)) for element in bracket)
            network_dict[k] += instr

    return instruction, network_dict
```

## Example 1


```python
instruction, network = process_input('example1.in')
instruction, network
```




    ('RL',
     defaultdict(tuple,
                 {'AAA': ('BBB', 'CCC'),
                  'BBB': ('DDD', 'EEE'),
                  'CCC': ('ZZZ', 'GGG'),
                  'DDD': ('DDD', 'DDD'),
                  'EEE': ('EEE', 'EEE'),
                  'GGG': ('GGG', 'GGG'),
                  'ZZZ': ('ZZZ', 'ZZZ')}))




```python
start = 'AAA'
step_counter = 0 

for i in instruction:
    if i == 'L':
        new_start = network[start][0]
        step_counter += 1
        if new_start == 'ZZZ':
            print(step_counter)
        else:
            start = new_start
    elif i == 'R':
        new_start = network[start][1]
        step_counter += 1
        if new_start == 'ZZZ':
            print(step_counter)
        else:
            start = new_start
```

    2
    

## Example 2


```python
instruction, network = process_input('example2.in')

instruction, network
```




    ('LLR',
     defaultdict(tuple,
                 {'AAA': ('BBB', 'BBB'),
                  'BBB': ('AAA', 'ZZZ'),
                  'ZZZ': ('ZZZ', 'ZZZ')}))




```python
def count_steps():

    step_counter = 0 
    start = 'AAA'

    while start != 'ZZZ':
        for i in instruction:
            
            if i == 'L':
                new_start = network[start][0]
                step_counter += 1
                if new_start == 'ZZZ':
                    return step_counter
                start = new_start

            elif i == 'R':
                new_start = network[start][1]
                step_counter += 1
                if new_start == 'ZZZ':
                    return step_counter
                start = new_start

count_steps()
```




    6



## Input


```python
instruction, network = process_input('input.in')
count_steps()
```




    21883



# Part 2

## Example 3


```python
instruction, network = process_input('example3.in')
instruction, network
```




    ('LR',
     defaultdict(tuple,
                 {'11A': ('11B', 'XXX'),
                  '11B': ('XXX', '11Z'),
                  '11Z': ('11B', 'XXX'),
                  '22A': ('22B', 'XXX'),
                  '22B': ('22C', '22C'),
                  '22C': ('22Z', '22Z'),
                  '22Z': ('22B', '22B'),
                  'XXX': ('XXX', 'XXX')}))




```python
nodes_end_A = tuple(element for element in network.keys() if element[-1] == 'A')
nodes_end_A
```




    ('11A', '22A')




```python
def count_steps():

    nodes_end_A = tuple(element for element in network.keys() if element[-1] == 'A')


    start_nodes = nodes_end_A
    count_nodes_end_Z = 0
    count_nodes_end_A = len(start_nodes)

    step_counter = 0

    while count_nodes_end_Z != count_nodes_end_A:

        for i in instruction:

            new_start_nodes = list()

            for node in start_nodes:
                new_start_nodes.append(network[node][0]) if i == 'L' else new_start_nodes.append(network[node][1])

            step_counter += 1

            in_loop_count_nodes_end_Z = len([element[-1] for element in new_start_nodes
                                            if element[-1] == 'Z'])

            
            if in_loop_count_nodes_end_Z == count_nodes_end_A:
                return step_counter

            count_nodes_end_Z = in_loop_count_nodes_end_Z
            start_nodes = tuple(new_start_nodes)

count_steps()
```




    6



## Input

There is no brute force solution that works. Let's try least common multiplier (LCM) or BFS.

Bless this subreddit: https://www.reddit.com/r/adventofcode/comments/18dtmin/comment/kckf5jg/?utm_source=share&utm_medium=web3x&utm_name=web3xcss&utm_term=1&utm_content=share_button


```python
instruction, network = process_input('input.in')
count_steps() # more than 5 mins
```


    ---------------------------------------------------------------------------

    KeyboardInterrupt                         Traceback (most recent call last)

    Cell In[139], line 2
          1 instruction, network = process_input('input.in')
    ----> 2 count_steps() # more than 5 mins
    

    Cell In[138], line 50, in count_steps()
         47 in_loop_count_nodes_end_Z = len([element[-1] for element in new_start_nodes if element[-1] == 'Z'])
         49 # Write to the file
    ---> 50 with open('output.txt', 'a') as file:
         51     file.write(f"{new_start_nodes}, {in_loop_count_nodes_end_Z}\n")
         53 # Update ghost information
    

    KeyboardInterrupt: 

