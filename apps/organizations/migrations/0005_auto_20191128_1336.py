# Generated by Django 2.2 on 2019-11-28 13:36

import DjangoUeditor.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('organizations', '0004_teacher_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courseorg',
            name='desc',
            field=DjangoUeditor.models.UEditorField(default='', verbose_name='描述'),
        ),
    ]
