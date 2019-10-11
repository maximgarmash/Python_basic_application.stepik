"""
Напишите простой интерпретатор математического выражения.
На вход подаётся строка с выражением, состоящим из двух чисел, объединённых бинарным оператором:
a operator b, где вместо operator могут использоваться следующие слова: plus, minus, multiply, divide для,
соответственно, сложения, вычитания, умножения и целочисленного деления.

Формат ввода:
Одна строка, содержащая выражение вида a operator b, 0≤a,b≤1000.
Оператор может быть plus, minus, multiply, divide.

Формат вывода:
Строка, содержащая целое число − результат вычисления.

Sample Input 1:

45 plus 8
Sample Output 1:

53
Sample Input 2:

12 minus 42
Sample Output 2:

-30
Sample Input 3:

451 multiply 2
Sample Output 3:

902
Sample Input 4:

13 divide 3
Sample Output 4:

4             plus, minus, multiply, divide
"""

# Solution 1
#
# def operation(expr):
#     if str(expr[1]) == 'plus':
#         return int(expr[0]) + int(expr[2])
#     if str(expr[1]) == 'minus':
#         return int(expr[0]) - int(expr[2])
#     if str(expr[1]) == 'multiply':
#         return int(expr[0]) * int(expr[2])
#     if str(expr[1]) == 'divide':
#         if int(expr[2]) != 0:
#             return int(expr[0]) // int(expr[2])
#         else:
#             return None
#
#
# print(operation(input().split()))

# Solution 2
import operator


operation = {'plus': operator.add, 'minus': operator.sub, 'multiply': operator.mul, 'divide': operator.floordiv}
expr = input().split()
try:
    print(operation[str(expr[1])](int(expr[0]), int(expr[2])))
except ZeroDivisionError:
    print(None)
