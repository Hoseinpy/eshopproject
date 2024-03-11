# Generated by Django 5.0.2 on 2024-02-29 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField(blank=True, max_length=500)),
                ('priority', models.IntegerField(default=1)),
                ('is_done', models.BooleanField()),
            ],
            options={
                'db_table': 'todos',
            },
        ),
    ]