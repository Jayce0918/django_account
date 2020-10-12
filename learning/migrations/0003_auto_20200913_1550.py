# Generated by Django 2.2 on 2020-09-13 07:50

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('learning', '0002_message'),
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='image/')),
                ('upload_date', models.DateField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.DeleteModel(
            name='Message',
        ),
    ]
