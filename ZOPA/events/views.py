from django.http import HttpResponseRedirect, Http404
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .forms import EventForm, TaskForm

from .models import Event, Task
# Create your views here.


class IndexView(generic.ListView):
    template_name = 'events/index.html'

    def get_queryset(self):
        return Event.objects.order_by('-start_date')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['events_list'] = Event.objects.order_by('-start_date')
        context['tasks_list'] = Task.objects.order_by('-priority')
        return context


class EventDetailView(generic.DetailView):
    model = Event
    template_name = 'events/event_detail.html'


def delete_event(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    event.delete()
    return HttpResponseRedirect(reverse('events:index'))


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
        if event_id:
            return redirect('events:event_detail', pk=event_id)
        return HttpResponseRedirect(reverse('events:index'))

    return render(request, template_name, {
        # 'error_message': "Please ensure all values are entered and correct.",
        'event': event,
        'form': form,
    })


def delete_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    task.delete()
    return HttpResponseRedirect(reverse('events:index'))


class TaskDetailView(generic.DetailView):
    model = Task
    template_name = 'events/task_detail.html'


def create_task(request, task_id=None):
    if task_id:
        task = get_object_or_404(Task, pk=task_id)
        template_name = 'events/edit_task.html'

    else:
        task = Task()
        template_name = 'events/new_task.html'

    form = TaskForm(request.POST or None, instance=task)

    if request.POST and form.is_valid():
        form.save()
        if task_id:
            return redirect('events:task_detail', pk=task_id)
        return HttpResponseRedirect(reverse('events:index'))

    return render(request, template_name, {
        # 'error_message': "Please ensure all values are entered and correct.",
        'task': task,
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
        Event.objects.create(event_name=name, start_date=starts, end_date=ends)
        return HttpResponseRedirect(reverse('events:index'))
'''