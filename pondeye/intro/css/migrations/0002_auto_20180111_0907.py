# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-01-11 09:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('intro', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='email',
            name='email',
            field=models.CharField(max_length=255),
        ),
    ]