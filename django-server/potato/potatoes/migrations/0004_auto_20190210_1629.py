# Generated by Django 2.1.5 on 2019-02-10 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('potatoes', '0003_igrititem_path'),
    ]

    operations = [
        migrations.AddField(
            model_name='igrititem',
            name='city',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='igrititem',
            name='item_type',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='igrititem',
            name='phone_number',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='igrititem',
            name='voivodeship',
            field=models.CharField(default='', max_length=100),
        ),
    ]
