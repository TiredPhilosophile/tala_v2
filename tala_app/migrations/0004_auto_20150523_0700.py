# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tala_app', '0003_auto_20150523_0659'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='podcastepisode',
            name='published',
        ),
        migrations.RemoveField(
            model_name='podcastmodel',
            name='published',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='created',
        ),
    ]
