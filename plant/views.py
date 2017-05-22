from django.http  import HttpResponse
from .models import Type
# Create your views here.

def index(request):
    all_types = Type.objects.all()
    html = ' '
    for type in all_types:
        url = "/plant/" + str(type.id) + "/"
        html += '<a href="' + url + '">' + type.t_name + '</a><br>'
    return HttpResponse(html)

def detail(request, plant_id):
    return HttpResponse("<h2>Details for plant id: " + str(plant_id) + " </h2>")
