import datetime

from django.test import TestCase
from django.utils import timezone
from django.urls import reverse

from .models import Event
# Create your tests here.


class EventModelTests(TestCase):

    def test_has_started_with_future_event(self):
        """
        has_started() returns False for events with a start_date in the future
        :return:
        """
        time = timezone.now() + datetime.timedelta(days=30)
        future_event = Event(start_date=time)
        self.assertIs(future_event.has_started(), False)

    def test_has_started_with_past_event(self):
        """
        has_started() returns True for events with a start_date in the past
        :return:
        """
        time = timezone.now() - datetime.timedelta(microseconds=1)
        past_event = Event(start_date=time)
        self.assertIs(past_event.has_started(), True)

    def test_has_started_with_event_now(self):
        """
        has_started() returns True for events with a start_date now
        :return:
        """
        time = timezone.now()
        event_now = Event(start_date=time)
        self.assertIs(event_now.has_started(), True)

    def test_has_finished_with_future_event(self):
        """
        has_finished() returns False for events with a end_date in the future
        :return:
        """
        time = timezone.now() + datetime.timedelta(days=30)
        future_event = Event(end_date=time)
        self.assertIs(future_event.has_finished(), False)

    def test_has_finished_with_past_event(self):
        """
        has_finished() returns True for events with a end_date in the past
        :return:
        """
        time = timezone.now() - datetime.timedelta(microseconds=1)
        past_event = Event(end_date=time)
        self.assertIs(past_event.has_finished(), True)

    def test_has_finished_with_event_now(self):
        """
        has_finished() returns True for events with a end_date now
        :return:
        """
        time = timezone.now()
        event_now = Event(end_date=time)
        self.assertIs(event_now.has_finished(), True)


def create_event(event_text, start_days, end_days):
    """
    Create an event with the given `event_text` and started the
    given number of `days` offset to now (negative for events started
    in the past, positive for events that have yet to be started).
    """
    start_time = timezone.now() + datetime.timedelta(days=start_days)
    end_time = timezone.now() + datetime.timedelta(days=end_days)
    return Event.objects.create(event_text=event_text, start_date=start_time, end_date=end_time)


class EventIndexViewTests(TestCase):

    def test_no_events(self):
        """
        If no events exist, an appropriate message is displayed
        :return:
        """
        response = self.client.get(reverse('events:index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "No events are available.")
        self.assertQuerysetEqual(response.context['events_list_all'], [])