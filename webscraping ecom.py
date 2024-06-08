import requests
from bs4 import BeautifulSoup
with open("sample.html", "r") as f:
    html_doc = f.read()

proxies = {
  'http': 'http://10.10.1.10:3128',
  'https': 'http://10.10.1.10:1080',
}

url = "https://www.amazon.in/s?k=macbook&ref=nb_sb_noss_2"

r = requests.get(url)

soup = BeautifulSoup(r.text, 'html.parser')

print(soup.prettify())