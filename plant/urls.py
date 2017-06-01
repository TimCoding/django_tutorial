from django.conf.urls import url
from . import views

app_name = 'plant'

urlpatterns = [
    # /plant/
    url(r'^$', views.TypeListView.as_view(), name='index'),
    
    # /plant/perennials/
    # Note for class based views make sure you use pk
    url(r'^(?P<slug>[a-z]+)/$', views.TypeDetailView.as_view(), name='detail'),

    # /plant/type/1-tacos
    url(r'^(?P<type>[a-z]+)/(?P<pk>[0-9]+)-(?P<name>[a-z]+)/$', views.PlantDetailView.as_view(), name='plant'),

    #URL that allows us to delete types
    # /plant/<type>/delete
    url(r'^(?P<slug>[a-z]+)/delete/$', views.TypeDelete.as_view(), name='type-delete'),

    #URL that allows us to delete individual plants
     # /plant/type/1-tacos/delete
    url(r'^(?P<type>[a-z]+)/(?P<pk>[0-9]+)-(?P<name>[a-z]+)/delete/$', views.PlantDelete.as_view(), name='plant-delete'),

    #URL for type form
    url(r'^type/add/$', views.TypeCreate.as_view(), name='type-add'),

    #URL for plant form
    url(r'^plants/add/$', views.PlantCreate.as_view(), name='plant-add'),
]