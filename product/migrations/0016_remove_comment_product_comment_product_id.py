# Generated by Django 5.0.2 on 2024-02-24 10:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0015_comment_product'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='product',
        ),
        migrations.AddField(
            model_name='comment',
            name='product_id',
            field=models.ForeignKey(auto_created=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='product.product', verbose_name='محصول'),
        ),
    ]
