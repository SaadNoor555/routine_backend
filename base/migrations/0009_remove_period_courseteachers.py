# Generated by Django 4.0.4 on 2022-04-21 06:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0008_alter_period_courseteachers'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='period',
            name='courseTeachers',
        ),
    ]
