# Generated by Django 2.2.13 on 2023-01-24 20:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_profession_professionimage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profession',
            name='header',
        ),
        migrations.RemoveField(
            model_name='professionimage',
            name='owner',
        ),
    ]
