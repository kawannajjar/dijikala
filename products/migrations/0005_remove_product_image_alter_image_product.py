# Generated by Django 5.1.6 on 2025-02-23 09:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_product_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='Image',
        ),
        migrations.AlterField(
            model_name='image',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product', verbose_name='Product'),
        ),
    ]
