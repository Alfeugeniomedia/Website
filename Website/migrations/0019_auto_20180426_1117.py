# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-26 11:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Website', '0018_remove_front_users_redirect_to'),
    ]

    operations = [
        migrations.AlterField(
            model_name='front_users',
            name='key',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
