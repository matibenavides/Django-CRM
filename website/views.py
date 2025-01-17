from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.


def home(request):

    #Verificar si el usuario esta autenticado
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        #autentica el usuario
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Has iniciado sesión")
            return redirect('home')
        else:
            messages.success(request, "Hubo un error al iniciar sesión")
            return redirect('home')

    else:
        return render(request, 'home.html', {}) 


def login_user(request):
    pass

def logout_user(request):
    logout(request)
    messages.success(request, "Has cerrado sesión")
    return redirect('home')


