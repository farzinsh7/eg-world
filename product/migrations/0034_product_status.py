# Generated by Django 5.0.1 on 2024-02-06 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0033_remove_variant_image_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='status',
            field=models.CharField(choices=[('d', 'Draft'), ('p', 'Publish')], max_length=1, null=True),
        ),
    ]
