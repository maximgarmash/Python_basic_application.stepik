import re
import sys
for line in sys.stdin:
    line = line.strip()
    # if re.search(r"human", line):
    #     print(re.sub(r"human", "computer", line))
    print(re.sub(r"human", "computer", line))