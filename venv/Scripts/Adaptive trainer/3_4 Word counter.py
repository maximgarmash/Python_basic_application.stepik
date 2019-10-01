"""
Когда Антон прочитал «Войну и мир», ему стало интересно, сколько слов и
в каком количестве используется в этой книге.
Помогите Антону написать упрощённую версию такой программы, которая сможет подсчитать слова,
разделённые пробелом и вывести получившуюся статистику.

Программа должна выводить для каждого уникального слова число его повторений (без учёта регистра).

Формат ввода:
Одна строка, содержащая последовательности символов через пробел

Формат вывода:
Набор строк, каждая из которых содержит слово и, через пробел, число − количество раз,
которое слово использовалось во входной строке. Регистр слов не важен,
слова в выводе не должны повторяться, порядок слов произвольный.

Sample Input:

a aa abC aa ac abc bcd a
Sample Output:

bcd 1
ac 1
aa 2
a 2
abc 2
"""
from collections import Counter

cntr = Counter(input().lower().split())
for key in cntr:
    print(key, cntr[key])


# list_world = [word.lower() for word in input().split()]
# dict_word = {word: list_world.count(word) for word in list_world}
# for key, value in dict_word.items():
#     print(key, value)


# a = input().lower().split()
# b = list(set(a))
# for i in range(len(b)):
#     print(b[i], a.count(b[i]))

"""
>>> import collections
>>> c = collections.Counter()
>>> for word in ['spam', 'egg', 'spam', 'counter', 'counter', 'counter']:
...     c[word] += 1
...
>>> print(c)
Counter({'counter': 3, 'spam': 2, 'egg': 1})
>>> print(c['counter'])
3
>>> print(c['collections'])
0

https://pythonworld.ru/moduli/modul-collections.html

dgsg
"""

