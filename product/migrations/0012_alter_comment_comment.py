# Generated by Django 5.0.2 on 2024-02-24 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0011_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='comment',
            field=models.TextField(blank=True, max_length=500, null=True, verbose_name='کامنت'),
        ),
    ]
