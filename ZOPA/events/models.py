import datetime

from django.db import models
from django.utils import timezone


# Create your models here.
class Event(models.Model):
    event_text = models.CharField(max_length=200)
    start_date = models.DateTimeField('start date/time')
    end_date = models.DateTimeField('end date/time')

    def has_started(self):
        now = timezone.now()
        return now >= self.start_date
        # return self.start_date < now < self.end_date

    def has_finished(self):
        now = timezone.now()
        return now >= self.end_date

    def __str__(self):
        return self.event_text


