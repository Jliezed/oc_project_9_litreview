from django.contrib.auth import login

from django.shortcuts import render, redirect
from django.conf import settings

# Create your views here.
from . import forms


def signup_page(request):
    form = forms.SignupForm()
    if request.method == 'POST':
        form = forms.SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            # auto-login user
            login(request, user)
            return redirect(settings.LOGIN_REDIRECT_URL)
    return render(request, 'user/signup.html', context={'form': form})


