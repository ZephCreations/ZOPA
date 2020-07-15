from django.http import Http404
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from .models import Event
# Create your views here.

def index(request):
    upcoming_events_list = Event.objects.order_by('-start_date')[:5]
    context = {'upcoming_events_list': upcoming_events_list}
    return render(request, 'events/index.html', context)

def detail(request, event_id):
    event = get_object_or_404(Event, pk=event_id)


    return render(request, 'events/detail.html', {'event': event})

def edit(request, event_id):
    response = "You're editing the event '%s'"
    return HttpResponse(response % event_id)