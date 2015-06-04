from django.shortcuts import redirect, get_object_or_404, render

from django.http import HttpResponse, Http404, HttpResponseRedirect

from tala_app.models import *

import json
from django.core import serializers
from itertools import chain

# you might ensure ensure_csrf_token decorator
def index(request):
	return render(request, 'main/index.html')

# ---------- Pages ---------- #

def home(request):
	return render(request, 'main/home.html')

def testing(request):
	return render(request, 'main/testing.html')

def nest1(request):
	return render(request, 'main/nest_testing1.html')

def search(request):
	return render(request, 'main/search.html')

# ---------- API ---------- #

def podcast_data(request, podcast):
	
	# just use pickle or something., there needs to be a better way
	
	print PodcastModel.objects.all()

	podcast_object = PodcastModel.objects.get(name=podcast)
	userprofile_object = Userprofile.objects.all()[0]
	
	page_data = {
		'viewcount': 10,
		'understanding': "potato",
		'life': [1, 6, 10, 19],
	}
	
	serialized_p = serializers.serialize("json", [podcast_object])
	serialized_u = serializers.serialize("json", [userprofile_object])
	
	# combined json using chain
	combined = list(chain([podcast_object], [userprofile_object]))
	combined_data = serializers.serialize("json", combined)
	
	# print combined json
	parsed = json.loads(combined_data)
	print json.dumps(parsed, indent=4, sort_keys=True)
	
	# there needs to be a better way to combine json

		
	return HttpResponse(combined_data)

def userprofile_data(request, username):
	try:
		userprofile_object = Userprofile.objects.get(identifier=username)
		json = userprofile_object.serialized(fields="all")
	except:
		json = "Cannot find userprofile"
	return HttpResponse(json)

def user_data(request):
	if len(Userprofile.objects.all()) == 1:
		new_user = Userprofile(name="magicjohnson", email="poot@poot.com")
		new_user.save()
	data = serializers.serialize("json", Userprofile.objects.all())
	return HttpResponse(data)

# ---------- Functions ---------- #

def process_form(request):
	print request.is_ajax()
	if request.method == 'POST':
		print "POST"
		print request
	else:
		print "non post"

	return HttpResponse("done")
