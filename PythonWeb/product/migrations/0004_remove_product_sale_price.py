# Generated by Django 2.1.7 on 2019-02-21 09:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_product_sale_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='sale_price',
        ),
    ]
