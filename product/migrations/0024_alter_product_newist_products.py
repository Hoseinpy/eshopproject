# Generated by Django 5.0.2 on 2024-02-24 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0023_alter_product_newist_products'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='newist_products',
            field=models.BooleanField(default=True),
        ),
    ]
