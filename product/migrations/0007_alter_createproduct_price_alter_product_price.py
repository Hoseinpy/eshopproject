# Generated by Django 5.0.2 on 2024-02-23 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0006_remove_product_slug_createproduct_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='createproduct',
            name='price',
            field=models.DecimalField(decimal_places=0, max_digits=20),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=0, max_digits=20),
        ),
    ]
