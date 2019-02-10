import requests
from bs4 import BeautifulSoup
from datetime import datetime
from .. import django-server

url = 'https://www.igrit.pl/kategoria/gielda-ziemniakow-42?category=gielda-ziemniakow-42&page=1'

page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')

# items = soup.find_all(class_="article-list")

# parsed_items = {}

# # Get data
# for item in items:
#     print("petla")
#     date = item.find(class_="created-at").string
#     date = datetime.strptime(date, '%d.%m.%Y %H:%M')
#     item_type = item.find(class_="type").string
#     price = item.find(class_="price").string.split()
#     localization = item.find(class_="addressInfo").find("p").contents[2].split(",")
#     name = " ".join(localization[0].split())
#     voivodeship = " ".join(localization[1].split())
#     city = " ".join(localization[2].split())

#     try:
#         number = item.find(class_="phoneNumber").attrs["data-phone"]
#     except KeyError:
#         number = "Brak numeru"

#     parsed_item = {
#         "date": date,
#         "item_type": item_type,
#         "phone_number": number,
#         "price": price,
#         }
    
#     print(parsed_item)
#     parsed_items[date] = parsed_item

n = soup.find_all(class_="article-list")[0]
date = n.find(class_="created-at").string
date = datetime.strptime(date, '%d.%m.%Y %H:%M')
price = 1



# datetime.strptime(date_string, '%d.%m.%Y %H:%M')