from django.http import HttpResponse
from django.shortcuts import render
from django.template import Template, Context

from .forms import MathForm
from .models import Calculation
# Create your views here.

def calculations_list(request):
    calculations = Calculation.objects.all()
    c = {"texty": calculations}
    return render(
        request,
        "maths/lista.html",
        c
    )

def add(request, a, b):
    operation = 'add'
    result = a + b

    form = MathForm()

    x = request.POST.get('x')
    y = request.POST.get('y')
    print(x, y)
    return render(
        request,
        "maths/calculation.html",
        {"result": result, 'operation': operation, 'form': form}
    )
