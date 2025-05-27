"A generator is an iterator that is returned by calling a generator function"

# Using the generator pattern (an iterable)
class first_n(object):
    def __init__(self, n):
        self.n = n
        self.num = 0

    def __iter__(self):
        return self

    # Python 3 compatibility
    def __next__(self):
        return self.next()

    def next(self):
        if self.num < self.n:
            cur, self.num = self.num, self.num+1
            return cur
        raise StopIteration()

# a generator that yields items instead of returning a list
def firstn(n):
    num = 0
    while num < n:
        yield num
        num += 1

sum_of_first_n = firstn(1000000)

# Doubles is a generator
doubles = (2 * n for n in range(50))

# Q1
def gen_fib():
    n, add = 0, 1
    while True:
        yield n
        n, add = n + add, n

print(next(filter(lambda n: n > 2025, gen_fib())))

# Q2
def differences(t):
    """Yield the differences between adjacent values from iterator t.

    >>> list(differences(iter([5, 2, -100, 103])))
    [-3, -102, 203]
    >>> next(differences(iter([39, 100])))
    61
    """
    "*** YOUR CODE HERE ***"
    prev = next(t)
    for curr in t:
        yield curr - prev
        prev = curr

# Q3
def partition_gen(n, m):
    """Yield the partitions of n using parts up to size m.

    >>> for partition in sorted(partition_gen(6, 4)):
    ...     print(partition)
    1 + 1 + 1 + 1 + 1 + 1
    1 + 1 + 1 + 1 + 2
    1 + 1 + 1 + 3
    1 + 1 + 2 + 2
    1 + 1 + 4
    1 + 2 + 3
    2 + 2 + 2
    2 + 4
    3 + 3
    """
    assert n > 0 and m > 0
    if n == m:
        yield str(n)
    if n - m > 0:
        "*** YOUR CODE HERE ***"
        for p in partition_gen(n-m, m):
            yield str(p) + ' + ' + str(m)
    if m > 1:
        "*** YOUR CODE HERE ***"
        yield from partition_gen(n, m-1)

# for partition in partition_gen(4, 3):
#     print(partition)