# Generated by Django 5.0.2 on 2024-02-23 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SiteSetting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('site_name', models.CharField(max_length=100)),
                ('site_address', models.CharField(max_length=100)),
                ('site_domain', models.CharField(max_length=100)),
                ('site_about', models.TextField(max_length=200)),
                ('site_logo', models.ImageField(upload_to='files/site_logo')),
                ('site_phone', models.TextField(blank=True, max_length=20, null=True)),
                ('site_email', models.EmailField(blank=True, max_length=100, null=True)),
                ('is_main_setting', models.BooleanField()),
            ],
            options={
                'verbose_name': 'تنظیمات سایت',
                'verbose_name_plural': 'تنظیمات سایت',
            },
        ),
    ]
