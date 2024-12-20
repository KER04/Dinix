from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def login (request):
    #return HttpResponse('Prueba Django, mairethtiamomiamor')
    #saludo = {'nombre': 'Kevin'}
    return render (request, 'login.html')

def registro(request):
    return render(request, 'registro.html')

def inicio(request):
    return render(request, 'inicio.html')