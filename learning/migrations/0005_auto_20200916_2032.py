# Generated by Django 2.2 on 2020-09-16 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learning', '0004_auto_20200913_1649'),
    ]

    operations = [
        migrations.CreateModel(
            name='IMG',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img_url', models.ImageField(upload_to='img')),
            ],
        ),
        migrations.DeleteModel(
            name='Photo',
        ),
    ]