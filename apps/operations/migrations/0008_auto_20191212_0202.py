# Generated by Django 2.2 on 2019-12-12 02:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('operations', '0007_auto_20191211_2057'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userfavorite',
            name='fav_type',
            field=models.IntegerField(choices=[(1, '课程'), (2, '讲师')], default=1, verbose_name='收藏类型'),
        ),
    ]
