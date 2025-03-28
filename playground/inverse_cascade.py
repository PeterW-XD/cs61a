def inverse_cascade(n):
    grow(n)
    print(n)
    shrink(n)

def grow(n):
    if n // 10:
        grow(n // 10)
        print(n // 10)

def shrink(n):
    if n // 10:
        print(n // 10)
        shrink(n // 10)

def cascade(n):
    if n < 10:
        print(n)
    else:
        print(n % 10)
        cascade(n // 10)
        print(n % 10)

def inverse_cascade2(n):
    if n < 10:
        print(n)
    else:
        inverse_cascade2(n // 10)
        print(n)

def cascade2(n):
    if n < 10:
        print(n)
    else:
        print(n)
        cascade2(n // 10)
        print(n)
