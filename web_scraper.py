import requests
import string
from collections import Counter
from bs4 import BeautifulSoup

url = "https://www.bbc.com/news"
response = requests.get(url) #downloaded web page

site_html = response.text
soup = BeautifulSoup(site_html, 'html.parser')
articles = soup.findAll('a')

for article in articles:
    link = article.get("href")

    if link.startswith("/news/world/europe"):
        print(link)