# Generated by Django 2.2 on 2019-10-17 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0004_coursetag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coursetag',
            name='tag',
            field=models.CharField(max_length=100, verbose_name='标签'),
        ),
    ]
