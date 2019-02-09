import requests
from bs4 import BeautifulSoup

url = 'https://www.igrit.pl/kategoria/gielda-ziemniakow-42?category=gielda-ziemniakow-42&page=1'

page = requests.get(url)

print(page.text[:240])