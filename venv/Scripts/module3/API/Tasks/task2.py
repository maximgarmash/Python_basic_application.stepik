import requests
import json

headers = {"X-Xapp-Token" : 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJyb2xlcyI6IiIsImV4cCI6MTU2ODYyNDQ3MywiaWF0IjoxNTY4MDE5NjczLCJhdWQiOiI1ZDc2MDZhODI4MTc2OTAwMTFhZDE2ZTAiLCJpc3MiOiJHcmF2aXR5IiwianRpIjoiNWQ3NjE0ZDk4MWFkZGEwMDExZWFlMGZiIn0.zpIEdsJoxmyfS0Zq2LlJcDKZ5s-RiOWYFrcPANtv2HI'}
# инициируем запрос с заголовком

input_file = "input2.txt"
with open(input_file) as in_f, open("output2.txt", "w", encoding='UTF-8') as out_f:
    for artist_id in in_f.readlines():
        res = requests.get("https://api.artsy.net/api/artists/"+artist_id.rstrip(), headers=headers)
        data = json.loads(res.text)
        out_f.write(data['sortable_name'] + ' ' + data['birthday'] + '\n')


# разбираем ответ сервера
# j = json.loads(r.text)
# print(j['sortable_name'], j['birthday'])

