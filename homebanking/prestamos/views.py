from django.shortcuts import render
from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import PrestamoForm
from .models import Prestamo
from django.contrib.auth.decorators import login_required

# @login_required


def prestamos(request):
    prestamo_form = PrestamoForm
    # validamos que ocurrio una peticion POST
    if request.method == "POST":
        # Traemos los datos enviados
        prestamo_form = prestamo_form(data=request.POST)
        # Chequeamos que los datos son validos, de ser asi, los asignamos a una variable
        if prestamo_form.is_valid():
            loan_paymentReceived = request.POST.get('loan_payment', '')
            loan_dateReceived = request.POST.get('loan_date', '')
            loan_totalReceived = request.POST.get('loan_total', '')

            prestamo = Prestamo(loan_payment=loan_paymentReceived, loan_date=loan_dateReceived,
                                loan_total=loan_totalReceived, customer_id=1)
            prestamo.save()

            return render(request, 'prestamos/prestamos.html', {'enviado': "carlos"})
    return render(request, 'prestamos/prestamos.html', {'form': prestamo_form})
