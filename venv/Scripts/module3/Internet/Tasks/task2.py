import requests
import re
link_pattern = re.compile(r'''<a[^>]*?href=["'](.*?)["'][^>]*?>''')
site_pattern = re.compile(r'(\S+://)?([^/:]+)[/:]?')
site_set = set()

file_url = input()
file_text = requests.get(file_url).text

# with open("file_site.txt", "w+") as f:
#     f.write(file_text)
#     f.seek(0)

for url in link_pattern.findall(file_text):
    site = site_pattern.search(url)
    if site.group(2) != '..':
        site_set.add(site.group(2))

for i in sorted(site_set):
    print(i)


