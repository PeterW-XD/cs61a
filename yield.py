def binary_counter():
    yield "1"
    for prefix in binary_counter():
        yield prefix + "0"
        yield prefix + "1"

# for value in binary_counter():
#     print(f"value: {value}")
#     if value == "1000":
#         break

def prefixs(s):
    if s:
        yield from prefixs(s[:-1])
        yield s

list(prefixs('both'))