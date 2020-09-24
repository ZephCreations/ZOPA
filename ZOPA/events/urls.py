from django.urls import path

from . import views

app_name = 'events'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('events/<int:pk>/', views.EventDetailView.as_view(), name='event_detail'),
    #path('<int:pk>/edit/', views.EditView.as_view(), name='edit'),
    path ('events/new/', views.create_event, name='create_event'),
    path('events/<event_id>/edit/', views.create_event, name='edit_event'),
    path('events/<event_id>/delete/', views.delete_event, name='delete_event'),
    path('tasks/<int:pk>/', views.TaskDetailView.as_view(), name='task_detail'),
    path('tasks/new/', views.create_task, name='create_task'),
    path('tasks/<task_id>/edit/', views.create_task, name='edit_task'),
    path('tasks/<task_id>/delete/', views.delete_task, name='delete_task')
]