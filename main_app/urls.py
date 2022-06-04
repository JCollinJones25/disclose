from django.urls import path
# from .views import LocationView
from .views import Home

urlpatterns = [
    path('', Home.as_view(), name="home"),
    # path('', LocationView.as_view(), name="home"),
]