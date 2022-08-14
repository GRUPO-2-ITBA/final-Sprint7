from django.shortcuts import render

# Create your views here.
from django.contrib.auth.decorators import login_required


@login_required
def prestamos (request):
    return render(request, "prestamos/prestamos.html")