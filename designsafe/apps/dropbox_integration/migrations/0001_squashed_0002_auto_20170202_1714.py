# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2019-09-04 20:29
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    replaces = [(b'dropbox_integration', '0001_initial'), (b'dropbox_integration', '0002_auto_20170202_1714')]

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='DropboxUserToken',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dropbox_user_id', models.CharField(max_length=48)),
                ('access_token', models.CharField(max_length=255)),
                ('account_id', models.CharField(max_length=255)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='dropbox_user_token', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]