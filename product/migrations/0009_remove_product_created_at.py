# Generated by Django 5.0.2 on 2024-02-23 21:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0008_product_created_at_delete_createproduct'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='created_at',
        ),
    ]
