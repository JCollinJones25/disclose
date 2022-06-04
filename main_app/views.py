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

    
# def front(request):
#     context = { }
#     return render(request, 'index.html', context)


 
# @api_view(['GET', 'POST'])
# def location(request):

#     if request.method == 'GET':
#         location = Location.objects.all()
#         serializer = LocationSerializer(location, many=True)
#         return Response(serializer.data)

#     elif request.method == 'POST':
#         serializer = LocationSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['DELETE'])
# def location_detail(request, pk):
#     try:
#         location = Location.objects.get(pk=pk)
#     except Location.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)

#     if request.method == 'DELETE':
#         location.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)