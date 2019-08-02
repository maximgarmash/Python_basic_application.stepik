s = str(input())
t = str(input())
i = 0
while s.find(t) != -1:
    i += 1
    s = s[s.find(t)+1:]
print(i)
