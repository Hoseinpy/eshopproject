# Generated by Django 5.0.2 on 2024-02-27 14:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0029_visitedproduct'),
    ]

    operations = [
        migrations.RenameField(
            model_name='visitedproduct',
            old_name='user',
            new_name='user_id',
        ),
    ]
