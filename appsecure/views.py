from django.shortcuts import render, redirect
from .forms import CreateUserForm


from django.contrib.auth.models import auth
from django.contrib.auth.decorators import login_required

from django.contrib import messages


def home(request):
    return render(request, 'appsecure/index.html')

def register(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect("two_factor:login")
    context = {"registerForm": form}
    return render(request, 'appsecure/register.html', context)


@login_required(login_url='two_factor:login')
def dashboard(request):
    return render(request, 'appsecure/dashboard.html')


def user_logout(request):

    auth.logout(request)
    messages.success(request, "Logout success!")
    
    return redirect("home")

def account_locked(request):
    return render(request, 'appsecure/account-locked.html')