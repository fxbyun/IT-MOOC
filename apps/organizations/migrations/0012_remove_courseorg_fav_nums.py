# Generated by Django 2.2 on 2019-12-11 19:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('organizations', '0011_remove_courseorg_tag'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='courseorg',
            name='fav_nums',
        ),
    ]
