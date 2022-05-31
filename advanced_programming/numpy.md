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
