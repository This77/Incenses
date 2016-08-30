from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
	url(r'^rauch/', include('rauch.urls')),
	url(r'^admin/', admin.site.urls),
	url(r'^$', admin.site.urls),
	]