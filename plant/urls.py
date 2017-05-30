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

]