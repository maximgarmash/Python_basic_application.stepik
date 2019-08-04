import re

# pattern = r"((abc)|(test|text)*)"
# string = "abc"
# match = re.match(pattern, string)
# print(match)
# print(match.groups())
pattern = r"((\w+)-\2)"
string = "test-test chow-chow"
print(re.match(pattern, string))
print(re.findall(pattern, string))
duplicates = re.sub(pattern, r"\1", string)
# duplicates = re.findall(pattern, string)
print(duplicates)
