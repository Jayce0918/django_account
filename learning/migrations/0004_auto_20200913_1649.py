# Generated by Django 2.2 on 2020-09-13 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learning', '0003_auto_20200913_1550'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='image',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
