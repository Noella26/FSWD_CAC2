# Generated by Django 5.0.2 on 2024-05-03 09:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='author',
            name='biography',
        ),
        migrations.RemoveField(
            model_name='book',
            name='isbn',
        ),
    ]