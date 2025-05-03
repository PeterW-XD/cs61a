def tree(label, branches=[]):
    for branch in branches:
        assert is_tree(branch), 'branch must be trees'
    return [label] + list(branches)

def label(tree):
    return tree[0]

def branches(tree):
    return tree[1:]

def is_tree(tree):
    if type(tree) != list or len(tree) < 1:
        return False
    for branch in branches(tree):
        if not is_tree(branch):
            return False
    return True

def is_leaf(tree):
    return not branches(tree)

def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n-1)

def fact_times(n, k):
    "Return k * n * n-1 * ... * 1"
    if n == 0:
        return k
    else:
        return fact_times(n-1, n*k)