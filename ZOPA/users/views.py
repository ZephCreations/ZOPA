from django.contrib.auth import login, get_user_model
from django.contrib.auth.views import PasswordResetView
from django.shortcuts import redirect, render
from django.urls import reverse
from . import forms


def register(request):
    if request.method == "GET":
        return render(
            request, "users/register.html",
            {"form": forms.CustomUserCreationForm}
        )
    elif request.method == "POST":
        form = forms.CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(reverse("pages:index"))

        return render(request, "users/register.html", {
            # 'error_message': "Please ensure all values are entered and correct.",
            'form': form,
        })


class CustomPasswordResetView(PasswordResetView):
    form_class = forms.CustomPasswordResetForm

    def form_valid(self, form):
        username = form.cleaned_data.get('username')
        email = form.cleaned_data.get('email', '').lower()
        try:
            user = get_user_model().objects.get(username=username, email=email)
        except get_user_model().DoesNotExist:
            user = None
        if user is None:
            return redirect('password_reset_done')
        return super().form_valid(form)