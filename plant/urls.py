from django.conf.urls import url
from . import views

urlpatterns = [
    # /plant/
    url(r'^$', views.index, name='index'),

    # /plant/perennials/
    url(r'^(?P<type_name>[a-z]+)/$', views.detail, name='detail'),

    # /plant/71/1-tacos
    url(r'^[a-z]/(?P<plant_id>[0-9]+)-[a-z]|[A-Z]+/$', views.detail, name='plants'),
]