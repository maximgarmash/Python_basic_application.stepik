"""
Поле для игры сапёр представляет собой сетку размером n×m.
В ячейке сетки может находиться или отсутствовать мина.

Напишите программу, которая выводит "решённое" поле, т.е. для каждой ячейки,
не являющейся миной, указывается число мин, находящихся в соседних ячейках
(учитывая диагональные направления)

Формат ввода:
На первой строке указываются два натуральных числа 1≤n,m≤100,
после чего в n строках содержится описание поля в виде последовательности
точек '.' и звёздочек '*', где точка означает пустую ячейку, а звёздочка − ячейку с миной.

Формат вывода:
n строк поля, в каждой ячейке которого будет либо число от 0 до 8,
либо мина (обозначенная символом "*"), при этом число означает количество мин
в соседних ячейках поля.

Sample Input:

4 4
..*.
**..
..*.
....
Sample Output:

23*1
**32
23*1
0111
"""

n, m = map(int, input().split())
mines_field = [[j for j in str(input())] for i in range(n)]
x, y = 1, 1
if n == 1:
    n += 1
    x = 2
if m == 1:
    m += 1
    y = 2
format_mines_field = [[0 for j in range(m)] for i in range(n)]
i = 0
for row in mines_field:
    j = 0
    for cell in row:
        if cell == '*':
            format_mines_field[i][j] = 1
        j += 1
    i += 1

# print(mines_field)
# print(format_mines_field)
cleared_field = [[0 for j in range(m)] for i in range(n)]

i = 0
for row in mines_field:
    j = 0
    if i == 0:
        for cell in row:
            if j == 0:
                if cell == '*':
                    cleared_field[i][j] = '*'
                else:
                    cleared_field[i][j] = format_mines_field[i+1][j] + format_mines_field[i+1][j+1] + format_mines_field[i][j+1]
            elif j != m-1:
                if cell == '*':
                    cleared_field[i][j] = '*'
                else:
                    cleared_field[i][j] = format_mines_field[i][j-1] +format_mines_field[i+1][j-1] + format_mines_field[i+1][j] + format_mines_field[i+1][j+1] + format_mines_field[i][j+1]
            else:
                if cell == '*':
                    cleared_field[i][j] = '*'
                else:
                    cleared_field[i][j] = format_mines_field[i][j-1] + format_mines_field[i+1][j-1] + format_mines_field[i+1][j]
            j += 1
    elif i != n-1:
        for cell in row:
            if j == 0:
                if cell == '*':
                    cleared_field[i][j] = '*'
                else:
                    cleared_field[i][j] = format_mines_field[i-1][j] + format_mines_field[i-1][j+1] + format_mines_field[i][j+1] + format_mines_field[i+1][j+1] + format_mines_field[i+1][j]
            elif j != m-1:
                if cell == '*':
                    cleared_field[i][j] = '*'
                else:
                    cleared_field[i][j] = format_mines_field[i-1][j-1] + format_mines_field[i-1][j] + format_mines_field[i-1][j+1] + format_mines_field[i][j+1] + format_mines_field[i+1][j+1] + format_mines_field[i+1][j] + format_mines_field[i+1][j-1] + format_mines_field[i][j-1]
            else:
                if cell == '*':
                    cleared_field[i][j] = '*'
                else:
                    cleared_field[i][j] = format_mines_field[i-1][j] + format_mines_field[i-1][j-1] + format_mines_field[i][j-1] + format_mines_field[i+1][j-1] + format_mines_field[i+1][j]
            j += 1
    else:
        for cell in row:
            if j == 0:
                if cell == '*':
                    cleared_field[i][j] = '*'
                else:
                    cleared_field[i][j] = format_mines_field[i-1][j] + format_mines_field[i-1][j+1] + format_mines_field[i][j+1]
            elif j != m - 1:
                if cell == '*':
                    cleared_field[i][j] = '*'
                else:
                    cleared_field[i][j] = format_mines_field[i][j-1] + format_mines_field[i-1][j-1] + format_mines_field[i-1][j] + format_mines_field[i-1][j+1] + format_mines_field[i][j+1]
            else:
                if cell == '*':
                    cleared_field[i][j] = '*'
                else:
                    cleared_field[i][j] = format_mines_field[i][j-1] + format_mines_field[i-1][j-1] + format_mines_field[i-1][j]
            j += 1
    i += 1

if x == 2:
    del cleared_field[1]
if y == 2:
    i = 0
    for row in cleared_field:
        del cleared_field[i][1]
        i += 1

print('\n'.join([''.join([str(cell) for cell in row]) for row in cleared_field]))







#
#
# print(cleared_field)
