from django.contrib.auth.forms import UserCreationForm, PasswordResetForm
from django import forms


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(max_length=200)

    class Meta(UserCreationForm.Meta):
        fields = UserCreationForm.Meta.fields + ("email",)


class CustomPasswordResetForm(PasswordResetForm):
    username = forms.CharField(max_length=150)
    field_order = ['username', 'email']