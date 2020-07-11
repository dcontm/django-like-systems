from django.urls import path, include
from . import views


urlpatterns = [
    path('', include('like_system.urls')),
    path('', views.HomeView.as_view(), name='home')
]
