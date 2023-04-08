from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader
from .forms import Sign_In,Sing_Up

def index(request):
    return render(request, 'index.html')

def biling(request):
    return render(request, 'pages/billing.html')

def dashboard(request):
    return render(request, 'pages/dashboard.html')

def profile(request):
    return render(request, 'pages/profile.html')

def rtl(request):
    return render(request, 'pages/rtl.html')


def sign_in(request):
    if request.method == 'POST':
        form = Sign_In(request.POST)
        if form.is_valid():
            print(f'\n{form}\n')
    else:
        form = Sign_In()
    return render(request, 'pages/sign-in.html', {'form': form})

def sign_up(request):
    form = Sing_Up(request.POST)
    if form.is_valid():
        print(f'\n{form}\n')
    else:
        form = Sing_Up()
    return render(request, 'pages/sign-up.html',{'form': form})

def tables(request):
    return render(request, 'pages/tables.html')

def virtual_rea(request):
    return render(request, 'pages/virtual-reality.html')