import requests

api_url = "http://api.openweathermap.org/data/2.5/weather"

city = input("City? ")

params = {
    'q': city,
    'appid': '80ec6ee8d577a3f58cad01500a890ebc',
    'units': 'metric'
}

res = requests.get(api_url, params=params)
print(res.status_code)
print(res.headers["Content-Type"])
# print(res.json())  # returns json.loads(res.text) :)

data = res.json()
# print(data["main"]["temp"])
template = 'Current temperature in {} is {}'
print(template.format(city, data["main"]["temp"]))
