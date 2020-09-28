from django.forms import ModelForm
from django.utils import timezone
from .models import Event, Task
from .widgets import BootstrapDateTimePickerInput


class EventForm(ModelForm):
    def clean(self):
        cleaned_data = super().clean()
        start_date = cleaned_data.get('start_date')
        end_date = cleaned_data.get('end_date')

        if start_date and end_date and start_date > end_date:
            msg = "Starting date/time must be before ending date/time."
            self.add_error('start_date', msg)

    class Meta:
        model = Event
        fields = '__all__'
        widgets = {
            'end_date': BootstrapDateTimePickerInput(),
            'start_date': BootstrapDateTimePickerInput(),
        }
        # widgets = {
        #    'end_date': DateTimeInput(attrs={'type': 'datetime-local'}),
        #    'start_date': DateTimeInput(attrs={'type': 'datetime-local'}),
        # }
        help_texts = {
            'start_date': '<br> Accepted formats include: <br>"YYYY-mm-dd HH:MM:SS" eg. "2006-10-25 14:30:59" and <br>"YYYY-mm-dd HH:MM" eg. "2006-10-25 14:30"'

        }


class TaskForm(ModelForm):
    def clean(self):
        cleaned_data = super().clean()
        due_date = cleaned_data.get('due_date')

        if due_date < timezone.now():
            msg = "Due date cannot be in the past"
            self.add_error('due_date', msg)

    class Meta:
        model = Task
        fields = '__all__'
        exclude = ('recommended_priority',)
        widgets = {
            'due_date': BootstrapDateTimePickerInput(),
        }
        # widgets = {
        #    'end_date': DateTimeInput(attrs={'type': 'datetime-local'}),
        #    'start_date': DateTimeInput(attrs={'type': 'datetime-local'}),
        # }
        help_texts = {
            'due_date': '<br> Accepted formats include: <br>"YYYY-mm-dd HH:MM:SS" eg. "2006-10-25 14:30:59" and <br>"YYYY-mm-dd HH:MM" eg. "2006-10-25 14:30"'
        }
