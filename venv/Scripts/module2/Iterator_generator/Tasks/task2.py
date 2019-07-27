import itertools

def primes():
    n = 1
    while True:
        n += 1
        d, simple = 2, True
        while d**2 <= n:
            if n%d == 0:
                simple = False
            d += 1
        if simple:
            yield n

print(list(itertools.takewhile(lambda x: x <= 51, primes())))
