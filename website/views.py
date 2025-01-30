from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm, AddRecordForm
from .models import Record

# Create your views here.


def home(request):
    records = Record.objects.all()

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
        return render(request, 'home.html', {'records': records}) 



def logout_user(request):
    logout(request)
    messages.success(request, "Has cerrado sesión")
    return redirect('home')



def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            #autentica y logea el usuario
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "Te has registrado correctamente")
            return redirect('home')
    else:
        form = SignUpForm()
        return render(request, 'register.html', {'form': form}) 
        
    return render(request, 'register.html', {'form': form}) 


# Pasamos llave primaria del registro a mostrar. Esté siendo señalado de urls.py
# por path('record/<int:pk',...)
def customer_record(request, pk):
    if request.user.is_authenticated:
        # Buscamos el registro que coincide con la llave primaria
        customer_record = Record.objects.get(id=pk)
        return render(request, 'record.html', {'customer_record': customer_record})
    else:
        messages.success(request, "Debes iniciar sesión para ver esta página") 
        return redirect('home')


def delete_record(request, pk):
    if request.user.is_authenticated:
        delete_it = Record.objects.get(id=pk)
        delete_it.delete()
        messages.success(request, "El registro se ha eliminado correctamente")
        return redirect('home')
    else:
        messages.success(request, "Debes iniciar sesión para eliminar un registro")
        return redirect('home')


def add_record(request):
    form = AddRecordForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == "POST":
            if form.is_valid():
                add_record = form.save()
                messages.success(request, "El registro se ha agregado correctamente")
                return redirect('home')
        return render(request, 'add_record.html', {'form': form})
    else:
        messages.success(request, "Debes iniciar sesión para agregar un registro")
        return redirect('home')