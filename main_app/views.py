from django.shortcuts import render
from django.views.generic.base import TemplateView
from .serializers import LocationSerializer
from .models import Location
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
# import requests



# create a class for the Todo model viewsets
class Home(TemplateView):
    template_name = 'home.html'

class Location(TemplateView):
    model = Location
    template_name = 'location_list.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['locations'] = Location.objects.all()
        return context
    
class LocationDetail(TemplateView):
    model = Location
    template_name = 'location_detail.html'

