from django.shortcuts import render
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView
from django.urls import reverse
from django.shortcuts import redirect, render
from .models import Location
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator



@method_decorator(login_required, name='dispatch')
class Home(TemplateView):
    template_name = 'home.html'

@method_decorator(login_required, name='dispatch')
class LocationList(TemplateView):
    template_name = 'location_list.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['locations'] = Location.objects.all()
        return context
    
@method_decorator(login_required, name='dispatch')
class LocationDetail(DetailView):
    model = Location
    template_name = 'location_detail.html'

@method_decorator(login_required, name='dispatch')
class LocationCreate(CreateView):
    model = Location
    fields = ['name', 'city', 'state', 'img', 'description', 'lat', 'lng', 'img2', 'img3', 'img4']
    template_name = 'location_create.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(LocationCreate, self).form_valid(form)
    
    def get_success_url(self):
        return reverse('location_detail', kwargs={'pk': self.object.pk})

@method_decorator(login_required, name='dispatch')
class LocationUpdate(UpdateView):
    model = Location
    fields = ['name', 'city', 'state', 'img', 'description', 'lat', 'lng', 'img2', 'img3', 'img4']
    template_name = 'location_update.html'
    def get_success_url(self):
        return reverse('location_detail', kwargs={'pk': self.object.pk})

@method_decorator(login_required, name='dispatch')
class LocationDelete(DeleteView):
    model = Location
    template_name = 'location_delete_confirmation.html'
    success_url = '/locations/'


class Signup(View):
    def get(self, request):
        form = UserCreationForm()
        context = {"form": form}
        return render(request, "registration/signup.html", context)
    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("home")
        else:
            context = {"form": form}
            return render(request, "registration/signup.html", context)
