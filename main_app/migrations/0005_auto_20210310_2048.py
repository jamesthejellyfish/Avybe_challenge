# Generated by Django 3.1.7 on 2021-03-11 01:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_auto_20210310_2036'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='image',
            options={'ordering': ('date_created',)},
        ),
        migrations.AlterField(
            model_name='image',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 10, 20, 48, 39, 779031)),
        ),
        migrations.AlterField(
            model_name='image',
            name='date_modified',
            field=models.DateTimeField(default=datetime.datetime(2021, 3, 10, 20, 48, 39, 779983)),
        ),
    ]
