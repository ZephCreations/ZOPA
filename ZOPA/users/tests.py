from http import HTTPStatus

from django.test import TestCase, override_settings
from django.urls import reverse
from .forms import CustomUserCreationForm
from django.contrib.auth.forms import AuthenticationForm


# Create your tests here.
class CustomUserCreationFormUnitTests(TestCase):
    def test_form_email_field_exists(self):
        """Test email field is in CustomUserCreationForm."""
        form = CustomUserCreationForm()
        self.assertIn('email', form.fields)

    def test_email_field_has_char_limit(self):
        """Test email field has max length of 200."""
        form = CustomUserCreationForm()
        self.assertEqual(form.fields['email'].max_length, 200)

    def test_email_field_required_error(self):
        """Test the email field raises an error when blank."""
        data = {'email': ''}
        form = CustomUserCreationForm(data=data)
        self.assertEqual(form.errors['email'], ['This field is required.'])

    def test_email_field_valid_email_error(self):
        """Test the email field raises an error when the input is not a valid email address."""
        data = {'email': 'aaa.com'}
        form = CustomUserCreationForm(data=data)
        self.assertEqual(form.errors['email'], ['Enter a valid email address.'])


class UserRegistrationIntegrationTests(TestCase):
    def test_get_register_url(self):
        """Test the url '/users/register/' has a status code of 200 when accessed."""
        response = self.client.get(reverse('register'))
        self.assertEqual(response.status_code, 200)

    def test_post_success(self):
        """
        Test the '/users/register/' url successfully creates user and redirects when provided with correct post data.
        :return:
        """
        data = {
            'username': 'TestUser',
            'email': 'a@a.com',
            'password1': 'testPassword',
            'password2': 'testPassword',
        }
        response = self.client.post(reverse('register'), data=data)
        self.assertEqual(response.status_code, 302) # check success
        self.assertIn(response['location'], '/') # check redirects

    def test_post_error(self):
        """
        Test the '/users/register/' url redirects to same page and displays error when provided with incorrect
        post data.
        :return:
        """
        data = {
            'username': 'TestUser',
            'email': '',
            'password1': 'testPassword',
            'password2': 'testPassword',
        }
        response = self.client.post(reverse('register'), data=data)
        self.assertEqual(response.status_code, 200) # check fails
        self.assertContains(response, 'This field is required.') # check Error Message
