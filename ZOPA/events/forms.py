from django.forms import ModelForm
from .models import Event
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
            'start_date': BootstrapDateTimePickerInput()
        }
        # widgets = {
        #    'end_date': DateTimeInput(attrs={'type': 'datetime-local'}),
        #    'start_date': DateTimeInput(attrs={'type': 'datetime-local'}),
        # }
        help_texts = {
            'start_date': '<br> Accepted formats include: <br>"YYYY-mm-dd HH:MM:SS" eg. "2006-10-25 14:30:59" and <br>"YYYY-mm-dd HH:MM" eg. "2006-10-25 14:30"'

        }


