# Generated by Django 3.1.4 on 2021-01-30 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0008_announcement_foydalanuvchi'),
    ]

    operations = [
        migrations.AlterField(
            model_name='announcement',
            name='location',
            field=models.CharField(max_length=30),
        ),
    ]
