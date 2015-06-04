#tala_app/models.py

from django.db import models
from django import forms

import datetime
from django.utils import timezone
from collections import OrderedDict

from django.contrib.auth.models import AbstractBaseUser

# Manager for Custom User
from django.contrib.auth.models import UserManager

class PodcastModel(models.Model):
	name = models.TextField(max_length=50, unique=True, default="default_podcast_name")
	slug = models.SlugField(max_length = 60, unique=True, default="default_slug")
	description = models.TextField(max_length=1000)
	image = models.FileField(upload_to='podcast_images', default='default_podcast_img.jpg')
	genre = models.CharField(max_length=30, default="None")
	#published = models.DateTimeField(default=datetime.datetime.now())
	followers = models.TextField(max_length=2000, default="")
	supporters = models.TextField(max_length=2000, default="")

	episodeOrdered = models.CharField(max_length=15, default='LastToFirst') # 'LastToFirst' or 'FirstToLast'

	RSS_link = models.CharField(default=None, null=True, blank=True, max_length=150)
	AssignEpisodeNumbers = models.BooleanField(default=True)

	def latest_episode(self):
		return self.podcastepisode_set.all()[::-1][0]

	def followers_as_objects(self):
		# Return podcast userprofile follower objects

		# seperate text into array of names (not objects)
		podcast_follower_names = list(OrderedDict.fromkeys(self.followers.split(',')[1:]))

		podcast_follower_objects = []
		for follower in podcast_follower_names:
			try:
				f = Userprofile.objects.get(identifier=follower)
				podcast_follower_objects.insert(0, f)
			except:
				print "ERROR, cannot find", follower, "in podcast", self.name

		return podcast_follower_objects

	def supporters_as_objects(self):

		# seperate text into array of names (not objects)
		podcast_supporter_names = list(OrderedDict.fromkeys(self.supporters.split(',')[1:]))
		
		podcast_supporter_objects = []
		for supporter in podcast_supporter_names:
			try:
				s = Userprofile.objects.get(identifier=supporter)
				podcast_supporter_objects.insert(0, s)
			except:
				print "ERROR (from Model PodcastModel): Cannot find user object supporter", supporter, "in podcast", self.name

		return podcast_supporter_objects

	def fromRSS(self):
		# Used in templating for boolean values
		return True if self.RSS == None else False

	class Meta:
		get_latest_by = 'published'

	def __str__(self):
		return self.name


# Using a custom user model to prevent the user_auth error caused by heroku and django
# that was due to the create_user field in the django User model. It's easier just to
# create a custom class than fix it as the error runs deep. Plus it simplifies things having
# only one class

# more info: https://docs.djangoproject.com/en/1.7/topics/auth/customizing/#specifying-a-custom-user-model



class Userprofile(AbstractBaseUser):

	# default password is "default_password"

	identifier = models.CharField(max_length=30, unique=True, default="default_username")
	slug = models.SlugField(max_length=30, unique=True, default="default_slug")
	email = models.EmailField(max_length=120, unique=True, default="default@email.com")
	image = models.FileField(upload_to='user_images', default='user_images/default-profile.png', blank=True)
	following = models.TextField(max_length=1300, default="", blank=True) # ~ 50 podcasts
	supporting = models.TextField(max_length=1300, default="", blank=True) # ~ 50 podcasts
	podcast = models.ForeignKey(PodcastModel, null=True, blank=True, on_delete=models.SET_NULL)
	#created = models.DateTimeField(default=datetime.datetime.now())

	# settings
	visibility = models.BooleanField(default=True)
	notification_setting = models.CharField(max_length=15, default='both') # Values: 'none', 'both', 'following' or 'supporting'
	hasStripeCustomer = models.BooleanField(default=False)

	USERNAME_FIELD = 'identifier'

	def following_as_objects(self):
		# Returns array of podcast objects user is following
		
		user_following_names = list(OrderedDict.fromkeys(self.following.split(',')[1:]))
		
		user_following_objects = [] 
		for podcast in user_following_names:
			try:
				p = PodcastModel.objects.get(name=podcast)
				user_following_objects.insert(0, p)
			except:
				print "ERROR: from model function, Userprofile -- Podcast", podcast, "user is following, not found"

		return user_following_objects

	def supporting_as_objects(self):
		# Returns array of podcast objects user is supporting

		user_supporting_names = list(OrderedDict.fromkeys(self.supporting.split(',')[1:]))
		
		user_supporting_objects = [] 
		for podcast in user_supporting_names:
			try:
				s = PodcastModel.objects.get(name=podcast)
				user_supporting_objects.insert(0, s)
			except:
				print "ERROR: from model function, Userprofile -- Podcast", podcast, "user is supporting, not found"

		return user_supporting_objects

	def edit(self, followOrSupport, podcast):

		# Adds/removes user from PodcastModel and adds/removes podcast from Userprofile
		# podcast parameter requires a Podcast Object, not name, else a unicode error will display.

		# Reasoning behind this is to prevent me from actually messing with the text file, instead 
		# typing userprofile.edit('follow', podcastObject) will update everything for me.
		# This leads to consistency, and prevents accidental fuck-ups.

		if followOrSupport == 'follow':
			if podcast not in self.following_as_objects():
				# Add podcast to following
				podcast.followers = podcast.followers + ',' + self.get_username()
				self.following = self.following + ',' + podcast.name

			else:
				# Remove podcast, user wants to unfollow.
				podcast.followers = podcast.followers.replace("," + self.get_username(), "")
				self.following = self.following.replace("," + podcast.name, "")

		elif followOrSupport == 'support':
			if podcast not in self.supporting_as_objects():
				# Add podcast to supporting
				podcast.supporters = podcast.supporters + ',' + self.get_username()
				self.supporting = self.supporting + ',' + podcast.name

			else:
				# Remove podcast, user wants to unsupport.
				podcast.supporters = podcast.supporters.replace("," + self.get_username(), "")
				self.supporting = self.supporting.replace("," + podcast.name, "")


		else:
			raise Http404("Userprofile.edit() followOrSupport parameter is not 'follow' or 'support' ")	

		self.save()
		podcast.save()

	def __str__(self):
		return self.get_username()

	# Default UserManager for Django (Allows for the login(), logout(), authentication() and other functions)
	objects = UserManager()

class PodcastEpisode(models.Model):
	number = models.IntegerField(max_length=4)
	title = models.CharField(max_length=50)
	shownotes = models.TextField(max_length=1000)
	explicit = models.NullBooleanField(blank=True, null=True)
	podcast = models.ForeignKey(PodcastModel, null=True, blank=True)
	episode = models.FileField(upload_to='podcast_episodes', default='default.mp3')
	#published = models.DateTimeField()

	class Meta:
		ordering = ('number',)

	def __str__(self):
		return self.title



