# Generated by Django 3.0.4 on 2020-04-21 21:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('neuralmain', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photorequest',
            name='photo_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 22, 0, 6, 46, 679559), verbose_name='Дата загрузки фото'),
        ),
    ]
