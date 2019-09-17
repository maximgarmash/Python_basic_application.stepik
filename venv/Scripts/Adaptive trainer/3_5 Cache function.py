from functools import lru_cache

@lru_cache(maxsize=None)
def f(x):
    return x * 2 + 1

n = int(input())
res = [str(f(int(input()))) for i in range(n)]
print("\n".join(res))

print(f.cache_info())