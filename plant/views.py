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

def detail(request, plant_id):
    try:
        type = Type.objects.get(pk=plant_id)
    except Type.DoesNotExist:
        raise Http404("Album does not exist")
    return render(request, 'plant/detail.html', {'type': type})
