# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-23 15:17
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('off', '0005_auto_20180523_1812'),
    ]

    operations = [
        migrations.RenameField(
            model_name='location',
            old_name='name',
            new_name='location',
        ),
    ]
