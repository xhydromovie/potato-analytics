from django.db import models
from datetime import datetime

# Create your models here.
class IgritItem(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateField()
    price = models.IntegerField()

    def __str__(self):
        return str(self.id)