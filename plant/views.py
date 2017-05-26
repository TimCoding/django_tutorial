from django.http  import Http404
from django.shortcuts import render
from .models import Type, Plant
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

def plant(request, type, plant_id, slug):
    try:
        selected_type = Type.objects.get(t_name=type)
    except Type.DoesNotExist:
        raise Http404("Type does not exist")
    try:
        selected_plant = Plant.objects.get(pk=plant_id)
    except Plant.DoesNotExist:
        raise Http404("Plant does not exist")
    return render(request, 'plant/plant.html', {'plant': selected_plant})
