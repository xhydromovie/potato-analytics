import requests
import os
import sys

from bs4 import BeautifulSoup
from datetime import datetime
from django.core.wsgi import get_wsgi_application
from django.utils import timezone
from django.conf import settings
from django.apps import apps

def parse_price(value):
    if value[0] != "Do":
        value[0] = float(value[0].replace(",", "."))
    
    if value[1] == "zł/worek":
        return round(value[0]/15, 2)
    elif value[1] == "zł/kilogram":
        return value[0]
    elif value[1] == "zł/tona":
        return round(value[0]/1000, 2)
    elif value[1] == "zł/sztuka":
        return value[0]
    else:
        return "Do uzgodnienia"

proj_path = os.path.split(os.path.abspath(os.path.dirname(__file__)))[0]
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "potato.settings")
sys.path.append(proj_path)
 
# load your settings.py
os.chdir(proj_path)

# In essence you are actually loading up all the django components and settings
# so we gain access to djangos ORM
application = get_wsgi_application()

IgritItem = apps.get_model('potatoes', 'IgritItem')

url = 'https://www.igrit.pl/kategoria/gielda-ziemniakow-42?category=gielda-ziemniakow-42&page=1'

page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')
tablica = []
items = soup.find_all(class_="article-list")

latest_item = IgritItem.objects.latest('id')

for item in items:
    path = item.find("a").attrs["href"]
    print(path)
    print(latest_item.path)
    if path != latest_item.path:

        item_type = item.find(class_="type").string
        price = item.find(class_="price").string.split()
        
        price_value = parse_price(price)
        is_price = False

        if price_value == "Do uzgodnienia" or price_value > 4:
            is_price = False
            price_value = 0
        else:
            is_price = True

        date = item.find(class_="created-at").string
        date = datetime.strptime(date, '%d.%m.%Y %H:%M')

        text = item.find(class_="description").get_text().split()
        text = " ".join(text)[:-10]
        
        localization = item.find(class_="addressInfo").find("p").contents[2].split(",")
        name = " ".join(localization[0].split())
        voivodeship = " ".join(localization[1].split())
        city = " ".join(localization[2].split())

        path = item.find("a").attrs["href"]

        try:
            number = item.find(class_="phoneNumber").attrs["data-phone"]
        except KeyError:
            number = "Brak numeru"

        tablica.append(IgritItem(
        date=date,
        price=price_value,
        price_bool=is_price,
        item_type=item_type,
        voivodeship=voivodeship.capitalize(),
        city=city,
        phone_number=number,
        path=path,
        ))

    else:
        print("[LOG] No new data!")
        break
if bool(tablica):
    counter = 0
    for item in reversed(tablica):
        counter += 1
        item.save()
        print("[LOG] SAVED {} inputs ...".format(counter))