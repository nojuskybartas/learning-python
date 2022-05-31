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

# Concurrency

## Multiprocessing

Multiprocessing goes around the GIL by spawning completely different processes, however that means there is no shared memory.

**Basic use:**

`p1 = multiprocessing.Process(target = func, *args)`

`p1.start()`

`p1.join()`

**Queue:**

```
import multiprocessing

q = multiprocessing.Queue()

q.put()
q.get()
```

## Threading

Interlieved computation

**Basic use:**

`t = threading.Thread(target = func, *args)`

`t.start()`

`t.join()`

`t.is_alive()`

**Custom thread:**

```
import threading

class myThread(threading.Thread): #we inherit from Thread class

    def __init__(self, message):

        threading.Thread.__init__(self)
        self.message = message

    #We need to override the run method of Thread
    def run(self):
        for _ in range(20):
            print(self.message) #note: access to the arguments of the target goes through class attributes

m = myThread("Hello, world!")
m.start() #use .start() to start a new thread. If you use .run() the method will not be executed in a different thread.
print('we can run other code on the meantime')
m.join()
print('done')
```

**Queues**: useful for thread communication. Similar to a list, but aditionally provides methods to ensure thread safety.

```
from queue import Queue

q = Queue()     # create a queue

q.join()        # start the queue process

                # then

q.put('Object') # add to queue
q.get()         # read from the queue
q.task_done()   # unblock the element and allow .join() to finish
q.empty()       # return boolean
```

## `Lock()`

```
x_lock = threading.Lock()  # also available in multiprocessing


x_lock.acquire()    # lock
x += 1              # do some stuff
x_lock.release()    # release


with x_lock:        # or better way!
    x += 1
```

**Note:** a _Deadlock_ may occur when two processes are dependent on one another to finish, which causes them to wait for each other indefinitely.

Solution: try to prevent having two mutex locks open in the same thread at the same time.

## `RLock()`

Quite similar to `Lock()` but can be used by one thread multiple times.

## `Semaphore()`

Synchronizes code based on counters.

```
userLimit = 3
s = threading.Semaphore(userLimit)

def threadedFunction():
    with s:
        # Do something with a maximum of 3 active threads
```

## `Event()`

Used when you need multiple threads to wait for one signal.

```
signal = threading.Event()      # create event
signal.clear()                  # initialize the signal

                                # then...

signal.set()                    # signal the other algorithms
                                # and
signal.wait()                   # wait for the signal
```

# Numpy

## `np.zeros(shape: tuple)`

## `np.ones(shape: tuple)`

## `np.eye(size: int)`

## `np.arange(start, stop, step)`

returns a list between the start and stop

## `np.linspace(start, stop, number)`

return a list between the start and stop of given length number

## `np.random.random(shape: tuple)`

return random float array of given shape

## `np.diag(values: list)`

returns a diagonal matrix

## `np.reshape(array, shape: tuple)`

## `np.vectorize(func)`

returns a vectorized_func which can now take (np) arrays as arguments

## `np.random.seed(i: int)`

```
twoD = np.random.random((4,3))

id_min = np.unravel_index(twoD.argmin(), twoD.shape)    # index (row, col) of minimum value

def softmax(a):                                         # softmax function
    return np.exp(a) / np.sum(np.exp(a))
```

# Pandas

DataFrame (rows x cols)

Series (rows x 1)

#

- Ceating dataframes/series
  - **pd.DataFrame(dict)** - from a dict, keys for columns names, values for data as lists
  - **pd.DataFrame(np.random.rand(20,5))** - 20 rows and 5 columns of random floats
  - **pd.Series(my_list)** - creates a series from an iterable my_list
  - etc...
- Read from file
  - **pd.read_csv(filename)** - from a csv file
  - **pd.read_table(filename)** - from a delimited text file (like TSV)
  - **pd.read_excel(filename)** - from an Excel file
- Indexing/selecting
  - **df[col]** or **df.col**- returns column with label col as Series
  - **df[[col1, col2]]** - returns Columns as a new DataFrame
  - **s.iloc[0]** - selection by position (integer position based)
  - **s.loc[0]** - selection by index (label based)
  - **df.loc[:, :]** and **df.iloc[:, :]** - First argument represents the number of rows and the second for columns
  - etc...
- Viewing
  - **df.head(n)** - first n rows of the DataFrame [__replace head with tail__, you know what you will get]
  - **df.shape** - number of rows and columns
  - **df.info()** - index, datatype and memory
  - **df.describe()** - summary statistics for numerical columns
  - etc...
- Renaming

  - **df.columns = ['a','b','c']** - Renames columns

- Data cleaning

  - **df.drop([col1, col2, col3], inplace = True, axis=1)** - Remove set of column(s)
  - **df.isnull()** - Checks for null Values, Returns Boolean DataFrame
  - **df.isnull().any()** - Returns boolean value for each column, gives True if any null value detected corresponding to that column
  - **df.isnull().sum()** - Returns number of missing values for each column
  - **df.dropna()** - Drops all rows that contain null values
  - **df.dropna(axis=1)** - Drops all columns that contain null values
  - **df.fillna(x)** - Replaces all null values with x
  - **s.replace(1,'one')** - Replaces all values equal to 1 with 'one'
  - **s.replace([1,3], ['one','three'])** - Replaces all 1 with 'one' and 3 with 'three'
  - **df.rename(columns = lambda x: x + '\_1')** - Mass renaming of columns
  - **df.rename(columns = {'old_name': 'new_name'})** - Selective renaming
  - **df.rename(index = lambda x: x + 1)** - Mass renaming of index
  - **df[new_col] = df.col1 + ', ' + df.col2** - Add two columns to create a new column in the same DataFrame

- Apply & Filter
  - **df[df[col] > 0.5]** - Rows where the values in col > 0.5
  - **df[(df[col] > 0.5) & (df[col] < 0.7)]** - Rows where 0.7 > col > 0.5
  - **df[col].apply(lambda x)** - applies a transformation to each item in a column
  - **df.apply(np.mean)** - Applies a function across each column
  - **df.apply(np.max, axis=1)** - Applies a function across each row
  - **df.applymap(lambda arg(s): expression)** - Apply the expression on each value of the DataFrame
  - **df[col].map(lambda arg(s): expression)** - Apply the expression on each value of the column col
  - **Query** - eg: `sortedApps = df.query('Rating >= 1 and Rating < 2')`
- Sort
  - **df.sort_values(col1)** - Sorts values by col1 in ascending order
  - **df.sort_values(col2,ascending=False)** - Sorts values by col2 in descending order
  - **df.sort_values([col1,col2],ascending=[True,False])** - Sorts values by col1 in ascending order then col2 in descending order
- Group by
  - **df.groupby(col)** - Returns a groupby object for values from one column
  - **df.groupby([col1,col2])** - Returns a groupby object values from multiple columns
  - **df.groupby(col1)[col2].mean()** - (Aggregation) Returns the mean of the values in col2, grouped by the values in col1
  - **df.pivot_table(index=col1,values=[col2,col3],aggfunc=mean)** - Creates a pivot table that groups by col1 and calculates the mean of col2 and col3
- Joining & Merging
  - **df1.append(df2)** - Adds the rows in df1 to the end of df2 (columns should be identical)
  - **pd.concat([df1, df2], axis=1)** - Adds the columns in df1 to the end of df2 (rows should be identical)
  - **pd.merge(left, right, how='inner', on=None, left_on=None, right_on=None, left_index=False, right_index=False, sort=True)** - where
    - left − A DataFrame object.
    - right − Another DataFrame object.
    - how − One of 'left', 'right', 'outer', 'inner'. Defaults to inner. Each method has been described below.
    - on − Columns (names) to join on. **Must be found in both** the left and right DataFrame objects.
    - left_on − Columns from the left DataFrame to use as keys.
    - right_on − Columns from the right DataFrame to use as keys.
    - left_index − If True, use the index (row labels) from the left DataFrame as its join key(s). In case of a DataFrame with a MultiIndex (hierarchical), the number of levels must match the number of join keys from the right DataFrame.
    - right_index − Same usage as left_index for the right DataFrame.
    - sort − Sort the result DataFrame by the join keys in _lexicographical order_. Defaults to True, setting to False will improve the performance substantially in many cases.
