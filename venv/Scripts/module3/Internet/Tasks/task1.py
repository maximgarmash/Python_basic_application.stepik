import requests
import re

urlA = input()
# urlB = str(input())
resA = requests.get(urlA)
# resB = requests.get(urlB)
print(resA.status_code)

# pattern = r"\b<a href="+urlA
# print(pattern)