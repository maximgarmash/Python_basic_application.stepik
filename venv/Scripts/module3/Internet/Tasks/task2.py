import requests
import re

link_pattern = re.compile(r'''<a[^>]*?href=["'](.*?)[?"'][^>]*?>''')
site_pattern = re.compile(r'(\S+://)?([^/:]+)[/:]?')
site_set = set()

file_url = input()
file_text = requests.get(file_url).text

for url in link_pattern.findall(file_text):
    site = site_pattern.search(url)
    if site.group(2) != '..':
        site_set.add(site.group(2))

print("\n".join(sorted(site_set)))


