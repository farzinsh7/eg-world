# Generated by Django 4.2.17 on 2025-01-24 12:14

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_alter_product_discount_percent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='description',
            field=tinymce.models.HTMLField(),
        ),
    ]
