from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Type, Plant
# Create your views here.

class TypeList(generic.ListView):
    model = Type
    #Name which will be used in your templates to retrieve objects
    context_object_name = 'all_types'
    #Name of your actual template
    template_name = 'plant/index.html'

def detail(request, type_name):
    type = get_object_or_404(Type, t_name = type_name)
    #Assumption: If type exists then it must have a set of plants even if the set is empty
    type_plants = type.plant_set.all()
    context = {
        'type': type,
        'plants': type_plants,
    }
    return render(request, 'plant/detail.html', context)

def plant(request, type, plant_id, slug):
    #Checks to see if the type of plant is still correct
    selected_type = get_object_or_404(Type, t_name=type)
    #Actually selects plant to be used
    selected_plant = get_object_or_404(Plant, pk=plant_id)
    return render(request, 'plant/plant.html', {'plant': selected_plant})
