# Generated by Django 2.2 on 2019-12-10 14:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0038_auto_20191209_1740'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='is_banner',
        ),
        migrations.RemoveField(
            model_name='course',
            name='is_classics',
        ),
        migrations.RemoveField(
            model_name='course',
            name='teacher_tell',
        ),
        migrations.RemoveField(
            model_name='course',
            name='youneed_know',
        ),
    ]
