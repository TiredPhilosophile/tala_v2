# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tala_app', '0002_userprofile_member'),
    ]

    operations = [
        migrations.CreateModel(
            name='PodcastModel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default=b'default_name', max_length=20)),
                ('descriptions', models.TextField(default=b'description', max_length=30)),
                ('fancy', models.BooleanField(default=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
