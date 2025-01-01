# Generated by Django 4.2.17 on 2024-12-31 15:22

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_alter_product_options_product_short_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='discount_percent',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)]),
        ),
    ]