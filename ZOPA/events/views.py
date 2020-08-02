from django.http import HttpResponseRedirect, Http404
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from .forms import EventForm

from .models import Event
# Create your views here.


class IndexView(generic.ListView):
    template_name = 'events/index.html'
    context_object_name = 'events_list'

    def get_queryset(self):
        return Event.objects.order_by('-start_date')


class DetailView(generic.DetailView):
    model = Event
    template_name = 'events/detail.html'


class EditView(generic.DetailView):
    model = Event


def create_event(request, event_id=None):
    if event_id:
        event = get_object_or_404(Event, pk=event_id)
        template_name = 'events/edit_event.html'

    else:
        event = Event()
        template_name = 'events/new_event.html'

    form = EventForm(request.POST or None, instance=event)

    if request.POST and form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('events:index'))

    return render(request, template_name, {
        # 'error_message': "Please ensure all values are entered and correct.",
        'event': event,
        'form': form,
    })



'''
def create_event(request):
    name = request.POST['name']
    starts = request.POST['starts']
    ends = request.POST['ends']

    if name == "" or starts == "" or ends == "":
        return render(request, 'events/new_event.html', {
            'error_message': "Please ensure all values are entered and correct."
        })

    else:
        Event.objects.create(event_text=name, start_date=starts, end_date=ends)
        return HttpResponseRedirect(reverse('events:index'))
'''