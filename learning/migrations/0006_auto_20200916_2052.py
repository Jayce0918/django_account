# Generated by Django 2.2 on 2020-09-16 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learning', '0005_auto_20200916_2032'),
    ]

    operations = [
        migrations.AlterField(
            model_name='img',
            name='img_url',
            field=models.ImageField(upload_to='images'),
        ),
    ]
