lst = [int(i) for i in input().split()]
n = int(input())
if n not in lst:
    print("None")
else:
    for dig in lst:
        if dig == n:
            print(lst.index(dig), end=" ")
            lst[lst.index(dig)] = dig + 1
