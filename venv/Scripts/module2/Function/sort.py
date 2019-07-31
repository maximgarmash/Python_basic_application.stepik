import operator as op
from functools import partial
x = [
    ("Guido", "van", "Rossum" ),
    ("Haskell", "Curry"),
    ("John", "Backus")
]

# def length(name):
#     return len(" ".join(name))
#
# name_lengths = [length(name) for name in x]
# print(name_lengths)
#
# x.sort(key=length)
# print(x)

# Эквивалентная запись

x.sort(key=lambda name: len(" ".join(name)))
print(x)

x.sort(key=op.itemgetter(-1))
print(x)

f = op.attrgetter("sort")
x = [2, 6, 1]
f(x)()
print(x)

x = [
    ("Guido", "van", "Rossum" ),
    ("Haskell", "Curry"),
    ("John", "Backus")
]

sort_by_last = partial(list.sort, key = op.itemgetter(-1))
print(x)
sort_by_last(x)
print(x)

y = ["abc", "cba", "abb"]
sort_by_last(y)
print(y)