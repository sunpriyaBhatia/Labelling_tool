# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2019-01-15 16:01
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0004_auto_20190115_1152'),
    ]

    operations = [
        migrations.RenameField(
            model_name='labelled_img',
            old_name='image_path',
            new_name='image_name',
        ),
    ]