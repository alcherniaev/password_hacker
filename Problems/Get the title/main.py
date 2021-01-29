import requests

from bs4 import BeautifulSoup


article = input()
r = requests.get(article)
soup = BeautifulSoup(r.content, 'html.parser')
print(soup.find('h1').text)

