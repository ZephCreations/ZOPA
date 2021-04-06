from django.urls import path, include, reverse_lazy
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('register/', views.register, name='register'),
]
