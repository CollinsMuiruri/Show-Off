# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-23 15:12
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('off', '0004_auto_20180522_1640'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='category',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='location',
            old_name='location',
            new_name='name',
        ),
    ]
