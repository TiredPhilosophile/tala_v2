from django.shortcuts import redirect, get_object_or_404, render

from django.http import HttpResponse, Http404, HttpResponseRedirect

from tala_app.models import *

import json
from django.core import serializers
from itertools import chain

import unicodedata

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

	podcast_object = PodcastModel.objects.get(name=podcast)
	userprofile_object = Userprofile.objects.all()[0]
	
	page_data = {
		'viewcount': 10,
		'understanding': "potato",
		'life': [1, 6, 10, 19],
	}
	
	# Serialize django object
	serialized_p = serializers.serialize("json", [podcast_object])
	serialized_u = serializers.serialize("json", [userprofile_object])

	response = {
		'page_data': page_data,
		'userprofile': json.loads(serialized_p), # unserialize, and then add to response to be serialized later
	}

	json_response = json.dumps(response, indent=4) # Serialize
		
	return HttpResponse(json_response, content_type='application/json')

def userprofile_data(request, username):
	try:
		userprofile_object = Userprofile.objects.get(identifier=username)
		json = serializers.serialize("json", [userprofile_object])
	except:
		json = "Cannot find userprofile"
	return HttpResponse(json)

# ---------- Functions ---------- #

def process_form(request):
	print request.is_ajax()
	if request.method == 'POST':
		print "POST"
		print request
	else:
		print "non post"

	return HttpResponse("done")
