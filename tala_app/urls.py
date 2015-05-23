from django.conf.urls import patterns, url
from django.conf import settings
from django.conf.urls.static import static

from tala_app import views

urlpatterns = patterns('',
	url(r'^$', views.index),
	
	url(r'^page/home', views.home),
	url(r'^page/testing', views.testing),
	url(r'^page/nest1', views.nest1),
	url(r'^page/search', views.search),
			
	url(r'^api/user_data', views.user_data),
	url(r'^api/podcast_data', views.podcast_data),
	url(r'^api/process_form', views.process_form),
)