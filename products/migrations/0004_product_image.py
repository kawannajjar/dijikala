# Generated by Django 5.1.6 on 2025-02-23 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_alter_category_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='Image',
            field=models.ImageField(blank=True, null=True, upload_to='category_images', verbose_name='Image'),
        ),
    ]
