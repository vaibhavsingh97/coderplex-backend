# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-24 01:14
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0003_auto_20171124_0105'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Profile',
            new_name='UserProfile',
        ),
    ]