# Generated by Django 2.2 on 2019-12-10 14:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('organizations', '0006_auto_20191203_1744'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='courseorg',
            name='tag',
        ),
    ]