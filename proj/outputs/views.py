from django.shortcuts import render
#from .models import Input

# Create your views here.

def outputs(request):
    #outputs = Input.objects.all()

    #return render(request, 'outputs.html', {'outputs':outputs})
    return render(request, 'outputs.html')