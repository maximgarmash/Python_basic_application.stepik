from datetime import date, timedelta

(y,m,d) = [int(n) for n in input().split()]
new_date = date(y, m, d) + timedelta(int(input()))
print(new_date.year, new_date.month, new_date.day)
