# Generated by Django 4.2.2 on 2023-06-14 21:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='content',
            name='category_name',
        ),
    ]
