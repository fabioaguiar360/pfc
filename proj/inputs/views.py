from django.shortcuts import render
from .models import Input

# Create your views here.

def inputs(request):
    inputs = Input.objects.all()

    return render(request, 'inputs.html', {'inputs':inputs})