# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-22 10:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nettest', '0018_auto_20160622_1043'),
    ]

    operations = [
        migrations.CreateModel(
            name='percentageofpacketdown',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('monid1', models.CharField(blank=True, max_length=200, null=True)),
                ('pcid', models.CharField(blank=True, max_length=200, null=True)),
                ('ips1', models.CharField(blank=True, max_length=50, null=True)),
                ('p1_p250', models.IntegerField(blank=True, null=True)),
                ('p251_p500', models.IntegerField(blank=True, null=True)),
                ('p501_p750', models.IntegerField(blank=True, null=True)),
                ('p751_p1000', models.IntegerField(blank=True, null=True)),
                ('p1001_p1250', models.IntegerField(blank=True, null=True)),
                ('p1251_p1500', models.IntegerField(blank=True, null=True)),
                ('p1501_p1750', models.IntegerField(blank=True, null=True)),
                ('p1751', models.IntegerField(blank=True, null=True)),
                ('totdown', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='percentageofpacketup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('monid1', models.CharField(blank=True, max_length=200, null=True)),
                ('pcid', models.CharField(blank=True, max_length=200, null=True)),
                ('ips1', models.CharField(blank=True, max_length=50, null=True)),
                ('p1_p250', models.IntegerField(blank=True, null=True)),
                ('p251_p500', models.IntegerField(blank=True, null=True)),
                ('p501_p750', models.IntegerField(blank=True, null=True)),
                ('p751_p1000', models.IntegerField(blank=True, null=True)),
                ('p1001_p1250', models.IntegerField(blank=True, null=True)),
                ('p1251_p1500', models.IntegerField(blank=True, null=True)),
                ('p1501_p1750', models.IntegerField(blank=True, null=True)),
                ('p1751', models.IntegerField(blank=True, null=True)),
                ('totup', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]
