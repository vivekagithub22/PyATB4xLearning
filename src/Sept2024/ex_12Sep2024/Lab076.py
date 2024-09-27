"""
Collections in Python -

Why we the data structure :
1. Store
2. update, search them
3. Play with them, manipulate.

Basic Data Structure

1. List
2. Set
3. Tuple
4. Dict

**Advance Collections**

1. deque - Queue -> it's a better version of list
    1. `# deque - double-ended queue`
    2. `# FIFO - bus stand queue, airport queue`
    3. `# A list-like sequence optimized for data accesses near its endpoints.`
2. defaultDict
3. Counter
4. OrderedDict
    1. `# OrderedDict# Dictionary that remembers insertion order'`
5. ChainMap
6. nametuple

"""

# deque - double-ended queue
# FIFO - bus stand queue, airport queue
# A list-like sequence optimized for data accesses near its endpoints.

from collections import deque

# create a deque
# d = deque()
d = deque([1, 2, 3])
print(d)

d.append(4) # Item
print(d)

# Add an element to the left end
d.appendleft(0)
print(d)

# Extend(list) the deque
d.extend([5,6])
print(d)

print(d.pop()) # removes End value
print(d.popleft())  # removes Start value

d.reverse()
print(d)