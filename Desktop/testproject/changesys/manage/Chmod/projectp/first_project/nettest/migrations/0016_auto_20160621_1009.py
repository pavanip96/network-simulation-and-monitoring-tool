# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-21 10:09
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nettest', '0015_auto_20160621_1007'),
    ]

    operations = [
        migrations.DeleteModel(
            name='capture',
        ),
        migrations.DeleteModel(
            name='monitable',
        ),
        migrations.DeleteModel(
            name='percentageofpacketdown',
        ),
        migrations.DeleteModel(
            name='percentageofpacketup',
        ),
    ]
