import requests
import re
link_pattern = re.compile(r'<a[^>]*?href="(.*?)"[^>]*?>')
site_pattern = re.compile()

file_url = "https://stepic.org/media/attachments/lesson/24472/sample0.html"
file_text = requests.get(file_url).text
with open("file_site.txt", "w+") as f:
    f.write(file_text)
    f.seek(0)
    for url in link_pattern.findall(file_text):
        print(url)


