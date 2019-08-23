import re
import sys
lst = []
for line in sys.stdin:
    line = line.strip()
    if len(re.findall(r"cat", line)) >= 2:
        lst.append(line)
for i in lst:
    print(i)

# for line in sys.stdin:
#     line = line.strip()
#     if re.search(r"cat.*cat", line):
#         print(line)

