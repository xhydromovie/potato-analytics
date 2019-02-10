import os
import sys
 
from django.core.wsgi import get_wsgi_application
from django.utils import timezone
from django.conf import settings
from django.apps import apps
 
# derive location to your django project setting.py
proj_path = os.path.split(os.path.abspath(os.path.dirname(__file__)))[0]
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "potato.settings")
sys.path.append(proj_path)
 
# load your settings.py
os.chdir(proj_path)

# In essence you are actually loading up all the django components and settings
# so we gain access to djangos ORM
application = get_wsgi_application()
IgritItem = apps.get_model('potatoes', 'IgritItem')

print(IgritItem.objects.all())
 
# run your custom script here
