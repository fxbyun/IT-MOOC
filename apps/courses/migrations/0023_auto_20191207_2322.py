# Generated by Django 2.2 on 2019-12-07 23:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0022_auto_20191207_2321'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='coursehomework',
            name='asthr',
        ),
        migrations.RemoveField(
            model_name='coursehomework',
            name='astwo',
        ),
        migrations.RemoveField(
            model_name='coursehomework',
            name='jxthr',
        ),
        migrations.RemoveField(
            model_name='coursehomework',
            name='jxtwo',
        ),
        migrations.RemoveField(
            model_name='coursehomework',
            name='qsthr',
        ),
        migrations.RemoveField(
            model_name='coursehomework',
            name='qstwo',
        ),
    ]