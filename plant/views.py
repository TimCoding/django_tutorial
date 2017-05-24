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

def detail(request, plant_name):
    try:
        type = Type.objects.get(t_name=plant_name)
    except Type.DoesNotExist:
        raise Http404("Plant type does not exist")
    return render(request, 'plant/detail.html', {'type': type})
