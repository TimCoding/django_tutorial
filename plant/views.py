from django.shortcuts import render, get_object_or_404
from .models import Type, Plant
# Create your views here.

def index(request):
    #Get all the types to display them in the field
    all_types = Type.objects.all()
    context = {
        'all_types': all_types,
    }
    return render(request, 'plant/index.html', context)

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

def favorite(request, type, plant_id, slug):
    #Checks to see if the type of plant is still correct
    selected_type = get_object_or_404(Type, t_name=type)
    #Actually selects plant to be used
    try:
        selected_plant = get_object_or_404(Plant, pk=request.POST['plant'])
    except (KeyError, Plant.DoesNotExist):
        return render(request, 'plant/detail.html', {
            'type' : selected_type,
            'plants' : selected_type.plant_set.all(),
            'error_message' : "You did not select a valid plant",
        })
    else: 
        is_favorited = selected_plant.p_favorite
        selected_plant.p_favorite = not(is_favorited)
        selected_plant.save()
        return render(request, 'plant/plant.html', {'plant': selected_plant})