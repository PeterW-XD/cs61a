def minimum_mewtations(typed, source, limit):

    if limit < 0:
        return 1
    elif typed == '' or source == '': # Base cases should go here, you may add more base cases as needed.
        # BEGIN
        "*** YOUR CODE HERE ***"
        return abs(len(typed) - len(source))
        # END
    # Recursive cases should go below here
    if typed[0] == source[0]: # Feel free to remove or add additional cases
        # BEGIN
        "*** YOUR CODE HERE ***"
        return minimum_mewtations(typed[1:], source[1:], limit)
        # END
    else:
        add = source[0] + typed
        remove = typed[1:]
        substitute = source[0] + typed[1:]
        # BEGIN
        "*** YOUR CODE HERE ***"
        min1 = 1 + minimum_mewtations(add[1:], source[1:], limit-1)
        min2 = 1 + minimum_mewtations(remove, source, limit-1) # removed should be checked again
        min3 = 1 + minimum_mewtations(substitute[1:], source[1:], limit-1)
        return min(min1, min2, min3)
    
minimum_mewtations('drest', 'drwt', 1) > 1

print([minimum_mewtations('drest', 'drwt', k) > k for k in range(5)])