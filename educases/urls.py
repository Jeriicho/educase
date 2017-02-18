from django.conf.urls import url
from . import views

app_name = 'educases'

urlpatterns = [
    #/index/
    url(r'^', views.IndexView.as_view(), name='index'),

    #/educases/56/
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),

]