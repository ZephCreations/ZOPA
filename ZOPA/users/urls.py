from django.urls import path, include, reverse_lazy
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    path('password_reset/', views.CustomPasswordResetView.as_view(), name='password_reset'),
    path('', include('django.contrib.auth.urls')),
    path('register/', views.register, name='register'),
]
