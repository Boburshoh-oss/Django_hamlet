# Generated by Django 3.1.4 on 2021-02-01 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0010_auto_20210130_1940'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='announcement',
            name='Property_Type',
        ),
        migrations.AddField(
            model_name='announcement',
            name='date',
            field=models.DateField(auto_now=True),
        ),
    ]
