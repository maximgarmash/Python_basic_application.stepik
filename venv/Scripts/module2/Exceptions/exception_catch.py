
try:
    x = [1, 2, 'abc', 7]
    x.sort()
    print(x)
except TypeError:
    print("Type error :(")

print("I can catch")