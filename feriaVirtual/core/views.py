from django.shortcuts import render

# Create your views here. la funcion def home busca el template (controlador)

def home(request):

    return render(request, 'core/home.html')

def login(request):

    return render(request, 'core/login.html')

def registrar(request):

    return render(request, 'core/registrar.html')