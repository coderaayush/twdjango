# Generated by Django 3.1.6 on 2021-07-29 22:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0002_auto_20210729_2251'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='likes',
            field=models.IntegerField(default=0),
        ),
    ]
