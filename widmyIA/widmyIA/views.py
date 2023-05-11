from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

def healthCheck(request):
    return HttpResponse('ok')

def inicio(request):
    return render(request, 'inicio.html')