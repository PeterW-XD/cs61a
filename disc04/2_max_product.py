def max_product(s):
    """Return the maximum product of non-consecutive elements of s.

    >>> max_product([10, 3, 1, 9, 2])   # 10 * 9
    90
    >>> max_product([5, 10, 5, 10, 5])  # 5 * 5 * 5
    125
    >>> max_product([])                 # The product of no numbers is 1
    1
    """
    "*** YOUR CODE HERE ***"
    # To track index in the list
    """ I need to compare with the element and without the element
    """

    if s == []:
        return 1
    elif len(s) == 1:
        return s[0]
    else:
        with_e = s[0] * max_product(s[2:])
        without_e = max_product(s[1:])

        return max(with_e, without_e)