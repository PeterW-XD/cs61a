def recursive(n):
    """Returns the sum of the first n integers
    >>> recursive(5)
    15
    """
    if n == 0:
        return 0
    else:
        return n + recursive(n-1)