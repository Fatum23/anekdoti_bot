import requests
from bs4 import BeautifulSoup as Soup

header = {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "cache-control": "no-cache",
    "dnt": "1",
    "pragma": "no-cache",
    "sec-fetch-mode": "navigate",
    "sec-fetch-site": "none",
    "sec-fetch-user": "?1",
    "upgrade-insecure-requests": "1",
    "user-agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36",
}

session = requests.Session()
session.headers = header


def parse_anekdotes():
    url = "https://newaneki.ru/"
    url2 = "https://newaneki.ru/page/2"
    res = session.get(url)
    res2 = session.get(url2)
    data = res.text
    data2 = res2.text

    bs = Soup(data, "html")
    bs2 = Soup(data2, "html")

    divs = bs.findAll("div", "blog-entry-summary clr")
    divs2 = bs2.findAll("div", "blog-entry-summary clr")
    with open("anekdotes.txt", "w+", encoding="utf-8") as f:
        for div in divs:
            p = div.find("p")
            if p.text != "":
                f.write(p.text + "*****")
        for div in divs2:
            p = div.find("p")
            if p.text != "":
                f.write(p.text + "*****")
