# Generated by Django 2.2 on 2019-12-08 00:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0030_coursehomeworkdetail'),
    ]

    operations = [
        migrations.AddField(
            model_name='coursehomeworkdetail',
            name='course',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='courses.Course'),
        ),
        migrations.AlterField(
            model_name='coursehomeworkdetail',
            name='homework',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='courses.CourseHomework', verbose_name='所属作业'),
        ),
    ]
