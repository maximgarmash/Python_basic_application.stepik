# x = [-2, -1, 0, 1, 2]
# y = [i**2 for i in x if i>0]
# print(y)

z = [(x, y) for x in range(3) for y in range(3) if y >= x]

print(z)

z = ((x, y) for x in range(3) for y in range(3) if y >= x)

print(z)

a = [i for i in range(5)][1:]
print(a)