import requests
import re
# link_pattern = re.compile(r'<a[^>]*?href="(.*?)"[^>]*?>')
link_pattern = re.compile(r'''<a[^>]*?href=["'](.*?)["'][^>]*?>''')
site_pattern = re.compile(r'\b[^.]*?(://)?([^/:]+)[/:]?')
# site_pattern = re.compile(r'//(.*?)/')
site_lst = set()

file_url = "https://stepic.org/media/attachments/lesson/24472/sample0.html"
file_text = requests.get(file_url).text
file_text = '<a href="http://neerc.ifmo.ru:1345">'
# file_text = '<a href="www.ya.ru">'
# file_text = '<a href="http://neerc.ifmo.ru">'
# with open("file_site.txt", "w+") as f:
#     f.write(file_text)
#     f.seek(0)
for url in link_pattern.findall(file_text):
    site = site_pattern.search(url)
    print(site.groups())
    site_lst.add(site.group(2))
    print(site_lst)


