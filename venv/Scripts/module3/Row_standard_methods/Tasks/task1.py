s = str(input())
a = str(input())
b = str(input())
i = 0
while a in s:
    if a in b:
        i = "Impossible"
        break
    else:
        s = s.replace(a, b)
        i += 1
print(i)
# ababa
# b
# a
