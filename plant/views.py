from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import TemplateView
from django.urls import reverse_lazy, reverse
from django.shortcuts import render, redirect
#login gives them session id so they don't have to authenticate every time
from django.contrib.auth import authenticate, login
from django.views.generic import View
from .models import Type, Plant
from .forms import UserForm
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

class TypeUpdate(UpdateView):
    model = Type
    fields = ['t_name', 't_img', 't_description']

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

class PlantUpdate(UpdateView):
    model = Plant
    fields = ['type', 'p_name', 'p_img', 'p_description', 'p_quantity']

class UserFormView(View):
    form_class = UserForm
    #html file that form is gunna be included in
    template_name = 'plant/registration_form.html'

    #display blank form
    def get(self, request):
        #Use default user form defined above in the UserFormView class
        #No need to pass in context
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    #When user submits form process it
    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            #Creates object from the form but it doesn't save it to db yet
            user = form.save(commit=False)

            # cleaned and normalized data (data that is formatted correctly)
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            #Manner in which we change user passwords
            user.set_password(password)
            #Adds user to db
            user.save()

            #returns User objects if credentials are correct
            user = authenticate(username=username, password=password)

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('plant:index')
            return render(request, self.template_name, {'form': form})

#View for login page
class LoginPage(TemplateView):
    template_name = "plant/login.html"

#Login
def action_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('plant:index')
    return render(request, "plant/login.html")
