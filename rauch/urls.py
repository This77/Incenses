from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^index/$', views.verzeichnis, name='verzeichnis'),
	url(r'^liste/$', views.substanz_liste, name='substanz_liste'),
	url(r'^(?P<substanz_id>[0-9]+)/$', views.substanz_singleform, name='substanz_singleform'),
	url(r'^(?P<substanz_id>[0-9]+)/images$', views.substanz_images, name='substanz_images'),
	url(r'^$', views.index, name='index'),
	]