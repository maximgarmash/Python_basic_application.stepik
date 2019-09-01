import requests
import re

# urlA = "https://stepic.org/media/attachments/lesson/24472/sample1.html"
# urlB = "https://stepic.org/media/attachments/lesson/24472/sample2.html"
urlA = str(input())
urlB = str(input())
answer = "No"
pattern1 = r'<a href="'+urlB+r'">.*\n*</a>'
pattern2 = r'<a href="(.*)">.*\n*</a>'
resA = requests.get(urlA)
lst_url = re.findall(pattern2, resA.text)
for url in lst_url:
    resC = requests.get(url)
    if re.search(pattern1, resC.text):
        answer = "Yes"
        break
print(answer)




# print(resA.content)
# print(type(resA.text))
# print(type(resA.content))
# pattern = r"\b<a href="+urlA
# print(pattern)