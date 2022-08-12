from django.shortcuts import render

# Create your views here.


def clientes(request):
    return render(request, "clientes/clientes.html")
def home(request):
    return render(request, "clientes/home.html")