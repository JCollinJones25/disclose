from django.shortcuts import render
from django.views.generic.base import TemplateView
from .serializers import LocationSerializer
from .models import Location
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status



# create a class for the Todo model viewsets
class Home(TemplateView):
    template_name = 'base.html'

class Location(TemplateView):
    model = Location
    template_name = 'location_detail.html'