from django.conf.urls import url
from . import views

app_name = 'plant'

urlpatterns = [
    # /plant/
    url(r'^$', views.index, name='index'),
    
    # /plant/perennials/
    url(r'^(?P<type_name>[a-z]+)/$', views.detail, name='detail'),

    # /plant/type/1-tacos
    url(r'^(?P<type>[a-z]+)/(?P<plant_id>[0-9]+)-(?P<slug>[a-z])+/$', views.plant, name='plant'),

     # /plant/type/1-tacos/favorite
    url(r'^(?P<type>[a-z]+)/(?P<plant_id>[0-9]+)-(?P<slug>[a-z])+/favorite$', views.favorite, name='favorite'),
]