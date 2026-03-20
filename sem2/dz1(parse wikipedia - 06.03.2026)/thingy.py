"""
import requests
headers = {
    "User-Agent": "Mozilla/5.0 (SeminarScraper/1.0; +https://example.org/)",
    "Accept": "text/html,application/xhtml+xml",
    "Accept-Language": "ru,en;q=0.8",
}

session = requests.Session()
session.headers.update(headers)

resp = session.get("https://ru.wikipedia.org", timeout=20)

from bs4 import BeautifulSoup

soup = BeautifulSoup(resp.text, "lxml")  # если lxml не установлен, используйте "html.parser"


# Найдём все блоки цитат
links = soup.find(id='main-dyk')#soup.select("a")

for link in links:
    print(link)
"""
import requests
from urllib.parse import urljoin
from bs4 import BeautifulSoup
import random

BASE = "https://ru.wikipedia.org"

headers = {
    "User-Agent": "Mozilla/5.0 (SeminarScraper/1.0; +https://example.org/)",
    "Accept": "text/html,application/xhtml+xml",
    "Accept-Language": "ru,en;q=0.8",
}

session = requests.Session()
session.headers.update(headers)

resp = session.get("https://ru.wikipedia.org/api/rest_v1/page/random/summary", timeout=20)
"""
from bs4 import BeautifulSoup

soup = BeautifulSoup(resp.text, "lxml")  # если lxml не установлен, используйте "html.parser"

dyk = soup.find(id='main-dyk')
link = dyk.find_all("a", href=True)[2]["href"]

article_url = urljoin(BASE, link)

print(article_url)

headers = {
    "User-Agent": "Mozilla/5.0 (SeminarScraper/1.0; +https://example.org/)",
    "Accept": "text/html,application/xhtml+xml",
    "Accept-Language": "ru,en;q=0.8",
}

session = requests.Session()
session.headers.update(headers)

resp_article = session.get(article_url, headers=headers, timeout=20)

soup_article = BeautifulSoup(resp_article.text, "lxml")
title = soup_article.find("h1").get_text(strip=True)
print(title)
"""

Page0 = resp.json()["content_urls"]["desktop"]["page"]


resp = session.get(Page0, timeout=20)


from bs4 import BeautifulSoup

soup = BeautifulSoup(resp.text, "lxml")  # если lxml не установлен, используйте "html.parser"

T0 = soup.find("title").text
link = random.choice(soup.find_all("a", href=True))["href"]
article_url = urljoin(BASE, link)
"""
dyk = soup.find(id='main-dyk')
link = dyk.find_all("a", href=True)[2]["href"]

article_url = urljoin(BASE, link)


print(article_url, T0)
"""
print(Page0, T0)
Page1 = article_url
resp = session.get(Page1, timeout=20)

soup = BeautifulSoup(resp.text, "lxml")  # если lxml не установлен, используйте "html.parser"

T1 = soup.find("title").text
print(Page1, T1)

link = random.choice(soup.find_all("a", href=True))["href"]
Page2 = urljoin(BASE, link)

resp = session.get(Page2, timeout=20)

soup = BeautifulSoup(resp.text, "lxml")  # если lxml не установлен, используйте "html.parser"

T2 = soup.find("title").text
print(Page2, T2)

"""
headers = {
    "User-Agent": "Mozilla/5.0 (SeminarScraper/1.0; +https://example.org/)",
    "Accept": "text/html,application/xhtml+xml",
    "Accept-Language": "ru,en;q=0.8",
}

session = requests.Session()
session.headers.update(headers)

resp_article = session.get(article_url, headers=headers, timeout=20)

soup_article = BeautifulSoup(resp_article.text, "lxml")
title = soup_article.find("h1").get_text(strip=True)
print(title)
"""