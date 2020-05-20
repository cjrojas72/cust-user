from django.shortcuts import render, reverse, HttpResponseRedirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from myapp.forms import LoginForm, SignUpForm
from myapp.models import CustUser
from practice.settings import AUTH_USER_MODEL

def loginview(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(
                request, username=data['username'], password=data['password'])
            if user:
                login(request, user)
                return HttpResponseRedirect(request.GET.get('next', reverse('home')))
    form = LoginForm()
    return render(request, 'login.html', {'form': form})


def logoutview(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))

def signUpview(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            CustUser.objects.create_user(
                    username=data["username"],
                    password=data['password']
            )
            return HttpResponseRedirect(reverse('home'))
    form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

@login_required
def index(request):
    data = CustUser.objects.all()
    data2 = AUTH_USER_MODEL
    return render(request, 'index.html', {'data':data, 'data2': data2})
