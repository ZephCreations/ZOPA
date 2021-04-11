from django.test import TestCase


# Create your tests here.
class UserEmailTests(TestCase):

    def test_email_required_when_creating_user(self):
        """
        Email field is required when creating a new user
        """
