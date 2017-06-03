from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from . import views

app_name = 'plant'

urlpatterns = [
    # /plant/
    url(r'^$', login_required(views.TypeListView.as_view()), name='index'),
    
    #Login Action
    url(r'^login/$', views.action_login, name='action_login'),

    #Logout Action
    url(r'^logout/$', views.action_logout, name='action_logout'),

    #Login Page
    url(r'^login_page/$', views.LoginPage.as_view(), name='login-page'),

    #Registering
    url(r'^register/$', views.UserFormView.as_view(), name='register'),

    # /plant/perennials/
    # Note for class based views make sure you use pk
    url(r'^(?P<slug>[a-z]+)/$', login_required(views.TypeDetailView.as_view()), name='detail'),

    # /plant/type/1-tacosß
    url(r'^(?P<type>[a-z]+)/(?P<pk>[0-9]+)-(?P<name>[a-z]+)/$', login_required(views.PlantDetailView.as_view()), name='plant'),

    #URL that allows us to delete types
    # /plant/<type>/delete
    url(r'^(?P<slug>[a-z]+)/delete/$', login_required(views.TypeDelete.as_view()), name='type-delete'),

    #URL that allows us to update types
    # /plant/<type>/update
    url(r'^(?P<slug>[a-z]+)/update/$', login_required(views.TypeUpdate.as_view()), name='type-update'),

    #URL that allows us to delete individual plants
    # /plant/type/1-tacos/delete
    url(r'^(?P<type>[a-z]+)/(?P<pk>[0-9]+)-(?P<name>[a-z]+)/delete/$', login_required(views.PlantDelete.as_view()), name='plant-delete'),

    #URL that allows us to update individual plants
    # /plant/type/1-tacos/update
    url(r'^(?P<type>[a-z]+)/(?P<pk>[0-9]+)-(?P<name>[a-z]+)/update/$', login_required(views.PlantUpdate.as_view()), name='plant-update'),

    #URL for type form
    url(r'^type/add/$', login_required(views.TypeCreate.as_view()), name='type-add'),

    #URL for plant form
    url(r'^plants/add/$', login_required(views.PlantCreate.as_view()), name='plant-add'),
]