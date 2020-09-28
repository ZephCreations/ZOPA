import datetime

from django.db import models
from django.utils import timezone


# Create your models here.
class Event(models.Model):
    REPEAT_BY_CHOICES = [
        ('D', 'Daily'),
        ('W', 'Weekly'),
        ('F', 'Fortnightly'),
        ('M', 'Monthly'),
        ('Y', 'Yearly'),
    ]

    event_name = models.CharField(max_length=200)
    start_date = models.DateTimeField('start date/time')
    end_date = models.DateTimeField('end date/time')
    repeat_by = models.CharField('Repeat event', blank=True, max_length=1, choices=REPEAT_BY_CHOICES)

    def has_started(self):
        now = timezone.now()
        return now >= self.start_date
        # return self.start_date < now < self.end_date

    def has_finished(self):
        now = timezone.now()
        return now >= self.end_date

    def __str__(self):
        return self.event_name


class Task(models.Model):
    PRIORITY_CHOICES = [
        (1, 'High'),
        (2, 'Medium'),
        (3, 'Low'),
    ]

    task_name = models.CharField(max_length=200)
    task_description = models.TextField(blank=True)
    due_date = models.DateTimeField('Date to be completed by')
    time_for_completion = models.DurationField('Time needed to complete task', default='00:00:00', help_text='Format: '
                                                                                                             'HH:MM:SS')
    priority = models.IntegerField(choices=PRIORITY_CHOICES, default=2)

    recommended_priority = models.IntegerField(default=99999, editable=False)
    recommended_start_time = models.DateTimeField(editable=False, default=timezone.now())

    def __str__(self):
        return self.task_name
