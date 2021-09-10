# Looping over two collections

names = ['raymond', 'lucas', 'matthew']
colors = ['red', 'green', 'blue', 'yellow']

for name, color in zip(names, colors):
    print(name, '-->', color)


# custom sort order

print(sorted(colors, key=len))

# call a function until a sentinel value

from functools import cache, partial

blocks = []
with open('somefile.tmp', 'r') as f:
    for block in iter(partial(f.read, 32), ''):
        blocks.append(block)

# distinguishing multiple exit points in functions
'''
If/when a for loop ends, the else clause is called. It is not called if the loop is broken out of beforehand
'''
def find(seq, target):
    for i, value in enumerate(seq):
        if value == target:
            break
    else:
        return -1
    return i

# looping over dictionary keys & values
d = {}
for k in d:
    print(k,'-->', d[k])

for k,v in d.items():
    print(k, '-->', v)

# construct a dictionary from pairs

names = ['raymond', 'lucas', 'matthew']
colors = ['red', 'green', 'blue']

d = dict(zip(names,colors))

# counting with dictionaries

from collections import defaultdict

d = defaultdict(int)
for color in colors:
    d[color] += 1

# grouping with dictionaries

d = defaultdict(list)
for name in names:
    key = len(name)
    d[key].append(name)

# linking dictionaries (in order)

import os
from typing import ChainMap, ContextManager
defaults = {'color': 'red', 'user': 'guest'}
command_line_args = None

d = ChainMap(command_line_args, os.environ, defaults)

# better tuples - return with a name and value descriptions

from collections import namedtuple

TestResults = namedtuple('TestResults', ['failed', 'attempted'])

# higher level approach to updating multiple state variables (assign operations are read from right to left in python)

def fibonacci(n):
    x, y = 0, 1
    for _ in range(n):
        print(x)
        x, y = y, x+y

# deleting items from the front of large lists
'''
wrap the list in a deque, this will make the operation significantly more efficient
'''

from collections import deque

names = deque(['raymond', 'rachel', 'mark'])

del names[0]
names.popleft()
names.appendleft('michael')

# using decorators to factor-out administrative logic
'''
instead of writing your own "cache" logic and storing data, the function is made a lot more readable by using a decorator
'''
import urllib

@cache
def web_lookup(url):
    return urllib.urlopen(url).read()

# using locks

import threading

lock = threading.Lock()

with lock:
    print("critical section 1")
    print("critical section 2")

# quick error-handling

@ContextManager
def ignored(*exceptions):
    try:
        yield
    except exceptions:
        pass

with ignored(OSError):
    os.remove('somefile.tmp')