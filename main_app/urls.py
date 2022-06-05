from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('location/<int:pk>', views.Location.as_view(), name="location_detail"),
]