from django.urls import path

from . import views

app_name = 'events'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    #path('<int:pk>/edit/', views.EditView.as_view(), name='edit'),
    path ('new/', views.create_event, name='create_event'),
    path('<event_id>/edit/', views.create_event, name='edit_event'),
]