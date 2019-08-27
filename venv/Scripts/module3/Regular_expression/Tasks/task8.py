import re
import sys
for line in sys.stdin:
    line = line.strip()
    print(re.sub(r"\b(\w)(\w)", r"\2\1", line))