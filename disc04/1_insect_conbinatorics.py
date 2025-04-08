def paths(m, n):
    """Return the number of paths from one corner of an
    M by N grid to the opposite corner.

    >>> paths(2, 2)
    2
    >>> paths(5, 7)
    210
    >>> paths(117, 1)
    1
    >>> paths(1, 157)
    1
    """
    "*** YOUR CODE HERE ***"
    # Bountry cases + trust function

    # Think of it 1 -> n*m
    def helper(cur):
        # When the insect hits the right bountry
        if cur % n == 0:
            return 1
        # When the insect hits the top bountry
        elif cur // n == m - 1:
            return 1
        else:
            return helper(cur+1) + helper(cur+n)
    
    return helper(1)