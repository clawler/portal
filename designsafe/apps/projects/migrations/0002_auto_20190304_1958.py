# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2019-03-04 19:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categoryorder',
            name='parent',
            field=models.UUIDField(blank=True, editable=False, null=True),
        ),
    ]
