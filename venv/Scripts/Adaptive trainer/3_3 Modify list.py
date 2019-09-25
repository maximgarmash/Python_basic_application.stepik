"""
Напишите функцию modify_list(l), которая принимает на вход список целых чисел, удаляет из него все нечётные значения,
а чётные нацело делит на два. Функция не должна ничего возвращать, требуется только изменение переданного списка,
"""


# def modify_list(lst):
#     i = 0
#     while i < len(lst):
#         if lst[i] % 2 == 0:
#             lst[i] = int(lst[i] / 2)
#             i += 1
#         else:
#             lst.remove(lst[i])

def modify_list(lst):
    lst[:] = [int(n / 2) for n in lst if n % 2 == 0]


lst = [4, 3, 5, 8, 11, 18]
modify_list(lst)
print(lst)
