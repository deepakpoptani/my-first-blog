# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-03-24 06:33
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Oost',
            new_name='Post',
        ),
    ]
