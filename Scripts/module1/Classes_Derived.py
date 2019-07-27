import sys
sys.stdin = open("input.txt", "r")

def parent(Classes_Derived, key, desc): # Описываем функцию для определения является ли предком один класс для другого
    if key == desc or (desc in Classes_Derived and key in Classes_Derived[desc]): # проверяется условие A = B и  
        return 'Yes'                                                              # A - прямой предок B и если да то Yes 
    elif desc in Classes_Derived and Classes_Derived[desc] != []: #проверяется условие
        for value in Classes_Derived[desc]:                                           # случай когда проверяется существует такой класс C, что C - прямой предок B и A - предок C
            x = parent(Classes_Derived, key, value)                                   # используя рекурсивную функцию
            if x == 'Yes':                                                            
                break
        return x
    else:
        return 'No'         # если не выполняется никакие другие условия то NO
n, Classes_Str = int(input()), []   # Создаем словарь с описанием наследственности классов
Classes_Derived = {}
for i in range(n):
    Classes_Str = input().split()
    Classes_Derived[Classes_Str[0]] = Classes_Str[2:]

q, get_str = int(input()), []
Gets_Answer = []

for i in range(q):                        # Создаем список с результатами проверки на наследственность для каждого запроса
    get_str = input().split()
    Gets_Answer.append(parent(Classes_Derived, get_str[0], get_str[1]))
for i in Gets_Answer: # Выводим результат
    print(i) 
