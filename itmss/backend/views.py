from django.shortcuts import render,redirect

# Create your views here.
from django.db import IntegrityError
from django.http import JsonResponse
from django.template import loader
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required

import json
from .forms import Sign_In,Sing_Up
from .models import UserSignUp

def index(request):
    return render(request, 'index.html')

def biling(request):
    return render(request, 'pages/billing.html')

@login_required
def dashboard(request):
    return render(request, 'pages/dashboard.html')

def profile(request):
    return render(request, 'pages/profile.html')

def rtl(request):
    return render(request, 'pages/rtl.html')

def sign_in(request):
    form = Sign_In(request.POST or None)
    if form.is_valid():
        email = form.cleaned_data['email']
        password = form.cleaned_data['password']
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        form.add_error(None, 'Email ou senha inválidos')
    return render(request, 'pages/sign-in.html', {'form': form})


def sign_up(request):
    form = Sing_Up(request.POST or None)
    if form.is_valid():
        nome = form.cleaned_data['nome']
        email = form.cleaned_data['email']
        password = form.cleaned_data['password']
        user = UserSignUp(nome=nome, email=email)
        user.set_password(password)
        try:
            user.save()
        except IntegrityError:
            form.add_error('email', 'Este email já está em uso')
        else:
            return redirect('dashboard')
    return render(request, 'pages/sign-up.html', {'form': form})

@login_required
def tables(request):
     
    if request.method == 'POST':
        data = json.loads(request.body)
        text = data['text']
        # Salvar o texto no banco de dados ou em outro lugar
        return JsonResponse({'success': True})
    else:
        return render(request, 'pages/tables.html')

def virtual_rea(request):
    return render(request, 'pages/virtual-reality.html')