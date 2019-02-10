from django.db import models
from datetime import datetime

# Create your models here.
class IgritItem(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateTimeField()
    price = models.IntegerField()
    is_price = models.BooleanField()
    path = models.CharField(max_length=100, default="") # e.g "/ogloszenie/ziemniaki-fioletowe-901593"
    voivodeship = models.CharField(max_length=100, default="")
    city = models.CharField(max_length=100, default="")
    item_type = models.CharField(max_length=20, default="")
    phone_number = models.CharField(max_length=20, default="")

    def __str__(self):
        return str(self.id)