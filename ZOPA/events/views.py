from django.http import HttpResponseRedirect, Http404
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.utils.dateparse import parse_duration
import datetime

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
        context['tasks_list'] = Task.objects.order_by('priority')
        context['optimized_task_list'] = optimize_tasks(Task.objects)
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

def tasks_dict(tasks):
    D = dict()
    i = 0
    for task in tasks:
        D.update({task.id: i})
        i += 1
    print(D)
    print('-----------------')
    return D


def optimize_tasks(tasks):
    PR_tasks = tasks.order_by('priority', '-time_for_completion')
    TN_tasks = tasks.order_by('-time_for_completion')
    print(PR_tasks)
    print(TN_tasks)

    PRs = tasks_dict(PR_tasks)
    TNs = tasks_dict(TN_tasks)

    prev_PST = timezone.now()
    prev_TN = parse_duration('0 0')
    for task in PR_tasks:
        key = task.id
        PR = PRs[key]
        TN = TNs[key]
        RP = 2*PR + TN
        setattr(task, 'recommended_priority', RP)
        task.save()

        PST = prev_PST + prev_TN

        setattr(task, 'recommended_start_time', PST)
        task.save()

        # Last code in loop
        prev_PST = PST
        prev_TN = task.time_for_completion

    for task in PR_tasks:
        # Step 3
        print(task)
        MST = task.due_date - task.time_for_completion
        if task.recommended_start_time > MST:
            PST = MST
            print(PST)
            setattr(task, 'recommended_start_time', PST)
            task.save()

    # Step 2 - PST = Previous PST + Previous TN
    # Step 3 - if PST > MET - TN
    #       PST = MET

    return tasks.order_by('recommended_start_time')
