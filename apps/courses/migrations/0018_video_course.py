# Generated by Django 2.2 on 2019-12-07 19:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0017_auto_20191207_1825'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='course',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='courses.Course'),
        ),
    ]
