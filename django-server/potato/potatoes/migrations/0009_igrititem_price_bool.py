# Generated by Django 2.1.5 on 2019-02-10 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('potatoes', '0008_remove_igrititem_is_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='igrititem',
            name='price_bool',
            field=models.BooleanField(default=False),
        ),
    ]
