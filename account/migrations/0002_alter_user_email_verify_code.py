# Generated by Django 5.0.2 on 2024-02-22 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email_verify_code',
            field=models.CharField(max_length=100),
        ),
    ]
