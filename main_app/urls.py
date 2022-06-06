from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('locations/', views.LocationList.as_view(), name="location_list"),
    path('locations/<int:pk>', views.LocationDetail.as_view(), name="location_detail"),
    path('locations/new/', views.LocationCreate.as_view(), name='location_create'),
    path('locations/<int:pk>/update', views.LocationUpdate.as_view(), name='location_update'),
    path('locations/<int:pk>/delete', views.LocationDelete.as_view(), name='location_delete'),
]