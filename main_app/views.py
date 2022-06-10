from django.shortcuts import render
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView
from django.urls import reverse
from django.shortcuts import redirect, render
from .models import Location, Comment
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.conf import settings



@method_decorator(login_required, name='dispatch')
class Home(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['locations'] = Location.objects.all()
        context['API_KEY'] = settings.API_KEY
        return context


# Location Views 
  
@method_decorator(login_required, name='dispatch')
class LocationDetail(DetailView):
    model = Location
    template_name = 'location_detail.html'

    def get_context_data(self, **kwargs):
        context = super(LocationDetail, self).get_context_data(**kwargs)
        context['comments'] = Comment.objects.filter(location_id=self.kwargs['pk'])
        return context

@method_decorator(login_required, name='dispatch')
class LocationCreate(CreateView):
    model = Location
    fields = ['name', 'city', 'state', 'img', 'lat', 'lng', 'description']
    template_name = 'location_create.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(LocationCreate, self).form_valid(form)
    
    def get_success_url(self):
        return reverse('location_detail', kwargs={'pk': self.object.pk})

@method_decorator(login_required, name='dispatch')
class LocationUpdate(UpdateView):
    model = Location
    fields = ['name', 'city', 'state', 'img', 'lat', 'lng', 'description']
    template_name = 'location_update.html'
    def get_success_url(self):
        return reverse('location_detail', kwargs={'pk': self.object.pk})

@method_decorator(login_required, name='dispatch')
class LocationDelete(DeleteView):
    model = Location
    template_name = 'location_delete_confirmation.html'
    success_url = '/'


# Comment Views  

@method_decorator(login_required, name='dispatch')
class CommentCreate(CreateView):
    model = Comment
    fields = ['location', 'user', 'comment']
    template_name = 'comment_create.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(CommentCreate, self).form_valid(form)
    
    def get_success_url(self):
        return reverse('location_detail', kwargs={'pk': self.object.location_id})
    
@method_decorator(login_required, name='dispatch')
class CommentUpdate(UpdateView):
    model = Comment
    fields = ['location', 'user', 'comment']
    template_name = 'comment_update.html'

    def get_success_url(self):
        return reverse('location_detail', kwargs={'pk': self.object.location_id})

@method_decorator(login_required, name='dispatch')
class CommentDelete(DeleteView):
    model = Comment
    template_name = 'comment_delete_confirmation.html'

    def get_success_url(self):
        return reverse('location_detail', kwargs={'pk': self.object.location_id})


# Signup View

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

