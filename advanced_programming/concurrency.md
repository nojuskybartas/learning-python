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
