from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('locations/new/', views.LocationCreate.as_view(), name='location_create'),
    path('locations/<int:pk>', views.LocationDetail.as_view(), name="location_detail"),
    path('locations/<int:pk>/update', views.LocationUpdate.as_view(), name='location_update'),
    path('locations/<int:pk>/delete', views.LocationDelete.as_view(), name='location_delete'),

    path('locations/<int:pk>/comment/', views.CommentCreate.as_view(), name='comment_create'),
    path('locations/<int:pk>/comment/update', views.CommentUpdate.as_view(), name='comment_update'),
    path('locationss/<int:pk>/comment/delete', views.CommentDelete.as_view(), name='comment_delete'),

    path('accounts/signup/', views.Signup.as_view(), name="signup"),
]