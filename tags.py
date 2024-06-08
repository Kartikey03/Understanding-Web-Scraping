import requests
from bs4 import BeautifulSoup
with open("sample.html", "r") as f:
    html_doc = f.read() #the content of the sample html file will now be stored in string format in this variable


soup = BeautifulSoup(html_doc, 'html.parser')
# print(soup.prettify())
print(soup.title.string)