# Generated by Django 5.1.6 on 2025-02-25 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_remove_product_image_alter_image_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productprice',
            name='create_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Datetime create'),
        ),
        migrations.AlterField(
            model_name='productprice',
            name='update_at',
            field=models.DateTimeField(auto_now=True, verbose_name='Datetime Update'),
        ),
    ]
