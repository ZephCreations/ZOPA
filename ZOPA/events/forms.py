from django.utils.translation import gettext_lazy as _
from django.forms import ModelForm, DateTimeInput
from .models import Event


class EventForm(ModelForm):
    class Meta:
        model = Event
        fields = '__all__'
        # widgets = {
        #    'end_date': DateTimeInput(attrs={'type': 'datetime-local'}),
        #    'start_date': DateTimeInput(attrs={'type': 'datetime-local'}),
        # }
        help_texts = {
            'start_date': '<br> Accepted formats include: <br>"YYYY-mm-dd HH:MM:SS" eg. "2006-10-25 14:30:59" and <br>"YYYY-mm-dd HH:MM" eg. "2006-10-25 14:30"'

        }
