from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate


# Create your views here.
def home(request):
    return render(request, 'todos/home.html')


def signupuser(request):
    if request.method == 'GET':
        return render(request, 'todos/signupuser.html', {'form': UserCreationForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('currenttodos')
            except IntegrityError:
                return render(request, 'todos/signupuser.html', {'form': UserCreationForm(), 'error': 'Username already exist. Please choose different.'})
        else:
            return render(request, 'todos/signupuser.html', {'form': UserCreationForm(), 'error': 'Your password didn\'t match'})


def loginuser(request):
    if request.method == 'GET':
        return render(request, 'todos/loginuser.html', {'form': AuthenticationForm()})
    else:
        user = authenticate(render, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'todos/loginuser.html', {'form': AuthenticationForm(), 'error': 'Username or Password is incorrect!'})
        else:
            login(request, user)
            return redirect('currenttodos')


def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        return render(request, 'todos/home.html')


def currenttodos(request):
    return render(request, 'todos/currenttodos.html')
