from django.db import models

class Userprofile(models.Model):
	name = models.CharField(max_length=20, default="default_name")
	email = models.EmailField(max_length=20, default="default@email.com")
	member = models.BooleanField(default=True)

class PodcastModel(models.Model):
	name = models.CharField(max_length=20, default="default_name")
	description = models.TextField(max_length=30, default="description")
	fancy = models.BooleanField(default=True)

