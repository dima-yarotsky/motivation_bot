from bs4 import BeautifulSoup
import requests
from bs4 import BeautifulSoup as BSHTML
import urllib

from pip._internal.cli.cmdoptions import src

import main

listImagesUrl = {}


def parse():
    url = 'https://bipbap.ru/pictures/motiviruyushhie-kartinki-na-uspeh-210-kartinok.html?ysclid=lfuttcg3uz176413004'
    page = requests.get(url)
    print(page.status_code)
    soup = BeautifulSoup(page.text, "html.parser")
    images = soup.find_all('img')
    num = 0
    for img in images:
        if img.has_attr('src'):
            listImagesUrl[num] = img['src']
            num += 1
    print(listImagesUrl)


