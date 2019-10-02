"""
Напишите программу, которая принимает на вход список целых чисел и выводит на экран значения,
которые повторяются в нём более одного раза.

Для решения задачи может пригодиться метод sort списка.

Формат ввода:
Одна строка с целыми числами, разделёнными пробелом.

Формат вывода:
Строка, содержащая числа, разделённые пробелом. Числа не должны повторяться,
порядок вывода может быть произвольным.

Sample Input:

6 6 6 7 9 9 0 5 5
Sample Output:

0 3 4

"""
# Solution 1

# lst_dig = input().split()
# for dig in set(lst_dig):
#     if lst_dig.count(dig) > 1:
#         print(dig, end=" ")

# Solution 2

from collections import Counter

cntr = Counter(input().split())
for dig in cntr:
    if cntr[dig] > 1:
        print(dig, end=' ')

# Solution 3
#
# lst_dig = input().split()
# lst_dig.sort()
# i = 0
# while i <= len(lst_dig) - 1:
#     if lst_dig.count(lst_dig[i]) > 1:
#         print(lst_dig[i], end=' ')
#         i += lst_dig.count(lst_dig[i])
#     else:
#         i += 1


