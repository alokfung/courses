# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-03-24 19:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20180324_1215'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='email',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='course',
            name='full_name',
            field=models.CharField(max_length=255),
        ),
    ]
