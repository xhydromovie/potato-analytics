# Generated by Django 2.1.5 on 2019-02-10 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('potatoes', '0004_auto_20190210_1629'),
    ]

    operations = [
        migrations.AlterField(
            model_name='igrititem',
            name='date',
            field=models.DateTimeField(),
        ),
    ]
