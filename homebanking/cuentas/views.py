from django.shortcuts import render

# Create your views here.
def cuentas(request):
    return render(request, "cuentas/cuentas.html")