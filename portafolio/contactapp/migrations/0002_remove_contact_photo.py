# Generated by Django 5.0.6 on 2024-06-11 01:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contactapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='photo',
        ),
    ]