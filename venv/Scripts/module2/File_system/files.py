f = open("test.txt", "r")
# x = f.read()
# print(x)
# x = x.splitlines()
# print(x)

# y = f.readline().rstrip()
# print(repr(y))
# y = f.readline()
# print(repr(y))

# x = f.readlines()
# print(x)

for line in f:
    line = line.rstrip()
    print(repr(line))
x = f.read()
print(repr(x))
f.close