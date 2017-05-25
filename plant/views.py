from django.http  import Http404
from django.shortcuts import render
from .models import Type
# Create your views here.

def index(request):
    all_types = Type.objects.all()
    context = {
        'all_types': all_types,
    }
    return render(request, 'plant/index.html', context)

def detail(request, type_name):
    try:
        type = Type.objects.get(t_name=type_name)
    except Type.DoesNotExist:
        raise Http404("Plant type does not exist")
    #Assumption: If type exists then it must have a set of plants even if the set is empty
    type_plants = type.plant_set.all()
    context = {
        'type': type,
        'plants': type_plants,
    }
    return render(request, 'plant/detail.html', context)

