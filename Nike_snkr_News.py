import requests
from bs4 import BeautifulSoup
from urllib.request import urlretrieve

url = requests.get('https://www.nike.com/tw/launch?s=upcoming')
soup = BeautifulSoup(url.text, 'html.parser')



product_pic = soup.find_all('a', {'class': 'card-link d-sm-b'})
all_product = soup.find_all('figure', {'class': 'd-md-h ncss-col-sm-12 va-sm-t pb0-sm prl0-sm'})

z = 0
i = 0
'''
    for pic in product_pic:
    if pic.img is None:
        continue
    z += 1
    pic_src = pic.img.get('src')
    file_name = (str(z) + '.jpeg')
    urlretrieve(pic_src, file_name)

print()
'''
snk_name = []
snk_link = []

for title in all_product:
    i += 1
        
    ssr = title.h3.text
    ssk = "https://nike.com" + title.a.get("href")
    snk_name.append(title.h3.text)
    snk_link.append("https://nike.com" + title.a.get("href"))

print(snk_name)
print(snk_link)