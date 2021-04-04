# Generated by Django 3.1.4 on 2021-03-31 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0002_announcement_person_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='announcement',
            name='Price',
            field=models.FloatField(choices=[('5000', '5000'), ('10000', '10000'), ('50000', '50000'), ('100000', '100000'), ('200000', '200000'), ('300000', '300000'), ('400000', '400000'), ('500000', '500000'), ('600000', '600000'), ('700000', '500000'), ('800000', '800000'), ('900000', '900000'), ('1000000', '1000000'), ('2000000', '2000000')]),
        ),
    ]
