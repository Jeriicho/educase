
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^$', include('educases.urls')),
    url(r'^educases/', include('educases.urls')),
    url(r'^admin/', admin.site.urls),
]
