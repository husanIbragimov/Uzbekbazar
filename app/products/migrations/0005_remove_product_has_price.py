# Generated by Django 5.0 on 2024-08-16 21:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_product_has_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='has_price',
        ),
    ]
