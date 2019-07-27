
def descendant(Error_Derived, desc, parent):
    if desc in Error_Derived and parent in Error_Derived[desc]:
        return desc
    elif desc in Error_Derived and Error_Derived[desc] != []:
        for value in Error_Derived[desc]:
            x = descendant(Error_Derived, value, parent)
            if x != None:
                break # используя рекурсивную функцию
        return x

n, Classes_Str = int(input()), []
Error_Derived = {}
for i in range(n):
    Classes_Str = input().split()
    Error_Derived[Classes_Str[0]] = Classes_Str[2:]

m, exc = int(input()), []

for i in range(m):
    exc.append(input())

for i in range(len(exc)-1):
    j = 0
    while j <= exc.index(exc[i]):
        if descendant(Error_Derived, exc[i+1], exc[j]):
            print(exc[i+1])
            break
            #del exc[i+1]
        j += 1



