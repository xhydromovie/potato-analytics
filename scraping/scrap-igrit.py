import requests
from bs4 import BeautifulSoup

url = 'https://www.igrit.pl/kategoria/gielda-ziemniakow-42?category=gielda-ziemniakow-42&page=1'

page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')

items = soup.find_all(class_="article-list")

parsed_items = {}

# print(date, item_type, number, " ".join(price)
for item in items:
    print("petla")
    date = item.find(class_="created-at").string
    item_type = item.find(class_="type").string
    price = item.find(class_="price").string.split()
    localization = item.find(class_="addressInfo").find("p").contents[2].split(",")
    name = localization[0].split()
    voivodeship = localization[1].split()
    city = localization[2].split()
    print(name, voivodeship, city)
    try:
        number = item.find(class_="phoneNumber").attrs["data-phone"]
    except KeyError:
        number = "Brak numeru"

    parsed_item = {
        "date": date,
        "item_type": item_type,
        "phone_number": number,
        "price": price,
        }
    
    print(parsed_item)
    parsed_items[date] = parsed_item

