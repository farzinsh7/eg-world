# Generated by Django 4.2.17 on 2025-01-19 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='title',
            field=models.CharField(default='آدرس پستی', max_length=255),
        ),
        migrations.AddField(
            model_name='useraddress',
            name='title',
            field=models.CharField(default='آدرس پستی', max_length=255),
        ),
    ]
