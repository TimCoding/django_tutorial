from django.conf.urls import url
from . import views

urlpatterns = [
    # /plant/
    url(r'^$', views.index, name='index'),

    # /plant/71/
    url(r'^(?P<plant_name>[A-Z][a-z]+)/$', views.detail, name='detail'),

    # /plant/71/1-tacos
    url(r'^(?P<plant_id>[0-9]+)-[a-z]|[A-Z]+/$', views.detail, name='detail'),
]