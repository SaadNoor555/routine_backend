# Generated by Django 4.0.4 on 2022-04-21 06:16

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_period_courseteachers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='period',
            name='courseTeachers',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(blank=True, default='', max_length=5), null=True, size=None),
        ),
    ]
