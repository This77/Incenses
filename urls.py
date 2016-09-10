from django.conf.urls import url
from . import views

app_name = 'rauch'
urlpatterns = [
	url(r'^index/$', views.verzeichnis, name='verzeichnis'),
	url(r'^substanzen/$', views.substanz_liste, name='substanz_liste'),
	url(r'^substanzen/input/$', views.substanz_input, name='substanz_input'),
	url(r'^substanzen/(?P<substanz_id>[0-9]+)/$', views.substanz_singleform, name='substanz_singleform'),
	url(r'^substanzen/(?P<substanz_id>[0-9]+)/images$', views.substanz_images, name='substanz_images'),
	url(r'^eigenschaften/$', views.eigenschaft_liste, name='eigenschaft_liste'),
	url(r'^eigenschaften/(?P<eigenschaft_id>[0-9]+)/$', views.eigenschaft_singleform, name='eigenschaft_singleform'),
	url(r'^$', views.index, name='index'),
	]