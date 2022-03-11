# -*- coding: UTF-8 -*-
import requests
from bs4 import BeautifulSoup
from urllib.request import urlretrieve
from itertools import chain

url = requests.get('https://www.nike.com/tw/launch?s=upcoming')
soup = BeautifulSoup(url.text, 'html.parser')


def sample_responses(input_text):
    user_message = str(input_text).lower()

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
    if user_message in ("Show", "show",):
        for title in all_product:
            i += 1

            ssr = title.h3.text
            ssk = "https://nike.com" + title.a.get("href")

            snk_name.append(title.h3.text)
            snk_link.append("https://nike.com" + title.a.get("href"))
            str(snk_name)
            str(snk_link)

    return list(chain.from_iterable(zip(snk_name, snk_link)))
