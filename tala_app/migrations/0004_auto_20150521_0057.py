# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tala_app', '0003_podcastmodel'),
    ]

    operations = [
        migrations.RenameField(
            model_name='podcastmodel',
            old_name='descriptions',
            new_name='description',
        ),
    ]
