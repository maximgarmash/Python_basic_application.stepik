import requests

res = requests.get("https://docs.python.org/3.5/")
res = requests.get("https://docs.python.org/3.5/_static/py.png")
res = requests.get("https://yandex.ru/search/",
                    params={
                        "text": "Stepic",
                        "test": "test1",
                        "name": "Name With Spaces",
                        "list": ["test1", "test2"]
                   })
print(res.status_code)
print(res.headers['Content-Type'])
print(res.url)
print(res.content)
# print(res.text)

# with open("python.png", "wb") as f:
#     f.write(res.content)

















# print(res.content)
#
# with open("python.png", "wb") as f:
#     f.write(res.content)

# print(res.text)

