# Advanced programming (python) course summary

**Higher order functions** : functions that accept functions as an argument or return a function

**\*args** : allows you to pass a desired number of arguments to the function

**\*kwargs** : stands for keyword arguments. The only difference from args is that it uses keywords and returns the values in the form of a dictionary

**Decorators** : By using the functionality of decorators, we can decouple certain features and tasks and keep eg. actual functionality, and decorative elements, separate.

**Currying** : The process of turning multiargument functions into a composition of single-argument functions.

**Lambda** expressions create anonymous functions

# Useful Functions

## `lambda`

```
f = (lambda *x: print(x))
f(1, 2, 3)
```

## `map(func, *iterables)`

Make an iterator that computes the function using arguments from each of the iterables. Stops when the shortest iterable is exhausted.

```
lambda *x: list(map(print, [y for y in x]))(1, 2, 3)
```

## `reduce(func, sequence)`

```
reduce(lambda x, y: x+y, [1, 2, 3, 4, 5])
```

calculates
`((((1+2)+3)+4)+5)`

## `filter(func, iterable)`

Takes a lambda function together with a list as the arguments.

```
filtered_list = list(filter(lambda num: (num > 7), numbers_list))
```

# Specialized Functions

## `curry(number of arguments to curry, func)`

```
from pymonad.tools import curry

@curry(3) #3 is the number of arguments we want to curry
def f(x,y,z):
    return (x+y)*z
```

## `partial(func, *args)`

Returns a new function with a partial implementation of the given arguments and keywords

```
from functools import partial

def add1(x):
    return add(1, x)

add1 = partial(add, 1)
```

## Closures

```
def pop_up(message):
    def inner():
        print(message)
    return inner

greeter=pop_up('Hello!')
checkpoint=pop_up('Passing by')

greeter()
checkpoint()

print('Content of the closure:', greeter.__closure__[0].cell_contents)
```

## Iterables

Objects, that one can iterate over. It generates an Iterator when passed to `iter()` method.

All iterables have an `__iter__` method and we can check the methods of an object with dir(object)

```
Integer: False
List: True
Dict: True
String: True
1-character string: True
Tuple: True
Integer: False
List Comprehension: True
Generator Expression: True
Lambda function: False
Function with return: False
Function with yield: True
```

## Iterators

Objects, which are used to iterate over an iterable object using the `__next__()` method.

The fastest way to find the length of a generator is converting it to a list, and using the len func: `len(list(generator))`

## Lazy loading

Generators and list comprehensions look similar but list comprehensions are _eager_ while generators are _lazy_

The main reason behind using generators is that with large data, it can be difficult to store a whole list in memory, and the program may crash. When using a generator, this problem is solved because you can access X amount of data at a time, without overflooding your RAM. On the other hand, the list comprehension may be slightly faster. So it's a trade-off between speed and memory capacity.

## [Concurrency](concurrency.md)

## [NumPy](numpy.md)

## [Pandas](pandas.md)
