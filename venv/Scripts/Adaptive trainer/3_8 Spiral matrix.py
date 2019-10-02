"""Выведите таблицу размером n×n, заполненную целыми числами от 1 до n2 по спирали,
выходящей из левого верхнего угла и закрученной по часовой стрелке, как показано в примере.

Формат ввода:
Одна строка, содержащая одно целое число n, n>0.

Формат вывода:
Таблица из n строк, значения в строках разделены пробелом.

Sample Input:

5
Sample Output:

1 2 3 4 5
16 17 18 19 6
15 24 25 20 7
14 23 22 21 8
13 12 11 10 9

"""


def spiral(n, matrix, a, x):
    for i in range(a, n):
        matrix[a][i] = str(x)
        x += 1
    for i in range(a + 1, n):
        matrix[i][n - 1] = str(x)
        x += 1
    for i in range(n - 2, a - 1, -1):
        matrix[n - 1][i] = str(x)
        x += 1
    for i in range(n - 2, a, -1):
        matrix[i][a] = str(x)
        x += 1
    n -= 1
    a += 1
    if n > 1:
        spiral(n, matrix, a, x)
    return matrix


n = int(input())
matrix = [[0 for j in range(n)] for i in range(n)]
x, a = 1, 0

ans_matrix = spiral(n, matrix, a, x)
for i in range(n):
    print(' '.join(ans_matrix[i]))
