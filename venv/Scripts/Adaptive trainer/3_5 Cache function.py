def f(x):
    return x * 2 + 1

res = {}
ans = []
n = int(input())
for x in range(n):
    i = int(input())
    if i not in res:
        res[i] = f(i)
        ans.append(str(res[i]))
    else:
        ans.append(str(res[i]))

print("\n".join(ans))