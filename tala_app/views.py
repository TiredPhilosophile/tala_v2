from django.shortcuts import redirect, get_object_or_404, render

from django.http import HttpResponse, Http404, HttpResponseRedirect

from tala_app.models import *

from django.core import serializers

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

def user_data(request):
	if len(Userprofile.objects.all()) == 1:
		new_user = Userprofile(name="magicjohnson", email="poot@poot.com")
		new_user.save()
	data = serializers.serialize("json", Userprofile.objects.all())
	return HttpResponse(data)

def podcast_data(request):
	if len(PodcastModel.objects.all()) == 0:
		new_podcast = PodcastModel(name="newpodcast", description="this is a new podcast")
		new_podcast.save()
	data = serializers.serialize("json", PodcastModel.objects.all())
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
