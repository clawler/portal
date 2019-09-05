# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2019-09-04 20:36
import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    replaces = [(b'notifications', '0001_initial'), (b'notifications', '0002_auto_20160301_2331')]

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_type', models.CharField(max_length=50)),
                ('user', models.CharField(max_length=20)),
                ('read', models.BooleanField(default=False)),
                ('deleted', models.BooleanField(default=False)),
                ('notification_time', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('body', models.TextField()),
            ],
        ),
    ]
