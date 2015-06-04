# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('tala_app', '0002_auto_20150523_0658'),
    ]

    operations = [
        migrations.AlterField(
            model_name='podcastmodel',
            name='published',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 23, 6, 59, 11, 498426)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 23, 6, 59, 11, 499616)),
            preserve_default=True,
        ),
    ]
