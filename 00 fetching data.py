import bs4 
import requests

def fetch(url, path):
    r = requests.get(url)
    with open(path, "w") as f:
        f.write(r.text)
url = "https://timesofindia.indiatimes.com/city"

fetch(url, "data/times.html")