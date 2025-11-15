
from django.shortcuts import render, get_object_or_404, redirect
from .models import Cliente
from .forms import ClienteForm
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
# Create your views here.

def saludo(request):
    return HttpResponse("<h1>Hola mundo desde la appventas!</h1>")


def pagina_inicio(request):
    return render(request, 'index.html')

# Create your views here.
def lista_clientes(request):
    clientes = Cliente.objects.all()  #select * from clientes
    return render(request, 'listar_clientes.html', {'clientes': clientes})

def crear_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            Cliente.objects.create(
               nombre = form.cleaned_data['nombre'],
               email = form.cleaned_data['correo'] 
            )
            return redirect('lista_clientes')
    else:
        form = ClienteForm()
        return render(request, 'nuevo_cliente.html',{'form': form})

def eliminar_cliente(request, id):
    cliente = get_object_or_404(Cliente, id_cliente = id)
    cliente.delete()
    return redirect('lista_clientes')

def actualizar_cliente(request, id):
    cliente = get_object_or_404(Cliente, id_cliente = id)
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            cliente.nombre = form.cleaned_data['nombre']
            cliente.email = form.cleaned_data['correo']
            cliente.save()
            return redirect('lista_clientes')
    else:
        form = ClienteForm(initial={
            'nombre': cliente.nombre,
            'correo': cliente.email,
        })
        return render(request, 'actualizar_cliente.html', {'form':form})




@login_required # 1. Protege la vista: solo usuarios logueados entran
def vista_ru_obs(request):
    """
    Vista para la página "RU OBS".
    Solo 'tecnico01' debería poder ver esto.
    """
    if request.user.username != 'tecnico01':
        return redirect('inicio') 

    return render(request, 'ru_obs.html')


def login_personalizado(request):
    """
    Vista para manejar el inicio de sesión personalizado
    y redirigir según el tipo de usuario.
    """
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            user = form.get_user()

            login(request, user)
            if user.is_staff:
                return redirect('admin:index')
            elif user.username == 'tecnico01':
                return redirect('ru_obs')
            else:
                return redirect('inicio')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


# --- INICIA SOLUCIÓN  ---

def logout_personalizado(request):
    """
    Cierra la sesión del usuario
    y lo redirige a la página de inicio.
    """
    # 'logout' borra la sesión del usuario del request
    logout(request)

    # Redirigimos al usuario a la página de inicio ('inicio')
    return redirect('inicio')

