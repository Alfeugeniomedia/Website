# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-04-16 05:10
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Website', '0004_auto_20180412_1443'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Events',
            new_name='EventsForm',
        ),
    ]