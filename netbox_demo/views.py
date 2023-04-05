from django.conf import settings
from django.contrib import messages
from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.views.generic import View

from .forms import CreateUserForm
from .utils import create_user

__all__ = (
    'AutoLoginView',
)


class AutoLoginView(View):

    def get(self, request):
        if request.user.is_authenticated:
            return redirect('home')

        return render(request, 'netbox_demo/login.html', {
            'form': CreateUserForm(),
        })

    def post(self, request):
        form = CreateUserForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username'] or None
            password = form.cleaned_data['password'] or None

            new_user, password = create_user(username=username, password=password)
            login(request, new_user, backend=settings.AUTHENTICATION_BACKENDS[0])
            messages.success(request, f"Logged in as {new_user} with password {password}")
            return redirect('home')

        return render(request, 'netbox_demo/login.html', {
            'form': form,
        })
