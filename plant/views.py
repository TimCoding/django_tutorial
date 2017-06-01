from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from .models import Type, Plant
# Create your views here.

class TypeListView(generic.ListView):
    model = Type
    #Name which will be used in your templates to retrieve objects
    context_object_name = 'all_types'
    #Name of your actual template
    template_name = 'plant/index.html'

class TypeDetailView(generic.DetailView):
    #Expects pk from url
    model = Type
    #Name of object template will use
    context_object_name = 'type'
    #Name of actual template
    template_name = 'plant/detail.html'

    def get_context_data(self, **kwargs):
        #Call the base implementation first to get a context
        context = super(TypeDetailView, self).get_context_data(**kwargs)
        #Add in list of plants using query
        context['plants'] = Type.objects.get(t_name=self.kwargs['slug']).plant_set.all()
        return context;

class PlantDetailView(generic.DetailView):
    #Expects pk from url
    model = Plant
    #Name of object template will use
    context_object_name = 'plant'
    #Name of actual template
    template_name = 'plant/plant.html'

class TypeCreate(CreateView):
    model = Type
    fields = ['t_name', 't_img', 't_description']

class TypeDelete(DeleteView):
    model = Type
    #redirects to details page when finished deleting
    success_url = reverse_lazy('plant:index')



#Automatically detects plant-form.html just make sure to set up url
#html file should follow <Model Name>_form.html format
class PlantCreate(CreateView):
    model = Plant
    fields = ['type', 'p_name', 'p_img', 'p_description', 'p_quantity']

class PlantDelete(DeleteView):
    model = Plant
    #This piece of code is necessary because it allows us to go back to details page of type
    #After deleting a plant
    #We grab the type to go back to from the url using self.kwargs
    #https://stackoverflow.com/questions/10631381/redirect-to-parent-after-deleting-an-object-with-deleteobject-generic-view
    def get_success_url(self, **kwargs):
        return reverse('plant:detail', kwargs={'slug':self.kwargs['type']})


    