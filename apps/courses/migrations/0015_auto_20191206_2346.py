# Generated by Django 2.2 on 2019-12-06 23:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0014_auto_20191206_2321'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='username',
            new_name='userid',
        ),
    ]
