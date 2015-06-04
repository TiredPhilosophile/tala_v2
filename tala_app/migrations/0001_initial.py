# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PodcastEpisode',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('number', models.IntegerField(max_length=4)),
                ('title', models.CharField(max_length=50)),
                ('shownotes', models.TextField(max_length=1000)),
                ('explicit', models.NullBooleanField()),
                ('episode', models.FileField(default=b'default.mp3', upload_to=b'podcast_episodes')),
                ('published', models.DateTimeField()),
            ],
            options={
                'ordering': ('number',),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PodcastModel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.TextField(default=b'default_podcast_name', unique=True, max_length=50)),
                ('slug', models.SlugField(default=b'default_slug', unique=True, max_length=60)),
                ('description', models.TextField(max_length=1000)),
                ('image', models.FileField(default=b'default_podcast_img.jpg', upload_to=b'podcast_images')),
                ('genre', models.CharField(default=b'None', max_length=30)),
                ('published', models.DateTimeField(default=datetime.datetime(2015, 5, 23, 6, 58, 46, 888235))),
                ('followers', models.TextField(default=b'', max_length=2000)),
                ('supporters', models.TextField(default=b'', max_length=2000)),
                ('episodeOrdered', models.CharField(default=b'LastToFirst', max_length=15)),
                ('RSS_link', models.CharField(default=None, max_length=150, null=True, blank=True)),
                ('AssignEpisodeNumbers', models.BooleanField(default=True)),
            ],
            options={
                'get_latest_by': 'published',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Userprofile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(default=django.utils.timezone.now, verbose_name='last login')),
                ('identifier', models.CharField(default=b'default_username', unique=True, max_length=30)),
                ('slug', models.SlugField(default=b'default_slug', unique=True, max_length=30)),
                ('email', models.EmailField(default=b'default@email.com', unique=True, max_length=120)),
                ('image', models.FileField(default=b'user_images/default-profile.png', upload_to=b'user_images', blank=True)),
                ('following', models.TextField(default=b'', max_length=1300, blank=True)),
                ('supporting', models.TextField(default=b'', max_length=1300, blank=True)),
                ('created', models.DateTimeField(default=datetime.datetime(2015, 5, 23, 6, 58, 46, 889587))),
                ('visibility', models.BooleanField(default=True)),
                ('notification_setting', models.CharField(default=b'both', max_length=15)),
                ('hasStripeCustomer', models.BooleanField(default=False)),
                ('podcast', models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, blank=True, to='tala_app.PodcastModel', null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='podcastepisode',
            name='podcast',
            field=models.ForeignKey(blank=True, to='tala_app.PodcastModel', null=True),
            preserve_default=True,
        ),
    ]
