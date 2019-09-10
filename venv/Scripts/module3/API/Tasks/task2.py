import requests
import json

input_file = "dataset_24476_4.txt"
artists = dict()
headers = {"X-Xapp-Token" : 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJyb2xlcyI6IiIsImV4cCI6MTU2ODYyNDQ3MywiaWF0IjoxNTY4MDE5NjczLCJhdWQiOiI1ZDc2MDZhODI4MTc2OTAwMTFhZDE2ZTAiLCJpc3MiOiJHcmF2aXR5IiwianRpIjoiNWQ3NjE0ZDk4MWFkZGEwMDExZWFlMGZiIn0.zpIEdsJoxmyfS0Zq2LlJcDKZ5s-RiOWYFrcPANtv2HI'}
# инициируем запрос с заголовком

with open(input_file) as in_f:
    for artist_id in in_f.readlines():
        res = requests.get("https://api.artsy.net/api/artists/"+artist_id.rstrip(), headers=headers)
        data = json.loads(res.text)
        birthday = data['birthday']
        if artists.get(birthday):
            artists[birthday].append(data['sortable_name'])
        else:
            artists[birthday] = [data['sortable_name']]

for birth in sorted(artists.keys()):
    for art in sorted(artists[birth]):
        print(art)

# for birthday in sorted(artists.values()):
#     print(birthday)

