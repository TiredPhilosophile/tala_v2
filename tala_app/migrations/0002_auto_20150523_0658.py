# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('tala_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='podcastmodel',
            name='published',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 23, 6, 58, 57, 494158)),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 23, 6, 58, 57, 495363)),
            preserve_default=True,
        ),
    ]
