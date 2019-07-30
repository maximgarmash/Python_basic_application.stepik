x = input().split()
print(x)
# n, k = map(int, x)
# print(n + k)

# map_obj = map(int, x)
# print(type(map_obj))
# n = next(map_obj)
# k = next(map_obj)
# print(n+k)

n, k = (int(i) for i in x)
print(n + k)