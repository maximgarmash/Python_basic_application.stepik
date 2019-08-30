import re
import sys
for line in sys.stdin:
    line = line.strip()
    pat = re.match(r"\A[01]+\Z", line)
    if pat:
        number = pat.string[::-1]
        sum_even, sum_odd = 0, 0
        for i in range(len(number)):
            if i % 2 == 0:
                sum_even += int(number[i])
            else:
                sum_odd += int(number[i])
        if (sum_even - sum_odd) % 3 == 0:
            print(line)

