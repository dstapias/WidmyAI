from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .logic import adendas_logic as al
from django.http import HttpResponse
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
def adendas_todas(request):
    if request.method == 'GET':
        adendas = al.get_todas()
        adendas_dto = serializers.serialize('json', adendas)
        return HttpResponse(adendas_dto, content_type='application/json')

@csrf_exempt
def adenda_create(request):
    return render(request, 'crearAdendas.html')

@csrf_exempt
def adendas_view(request):
    return render(request, 'adendas.html')

@csrf_exempt
def actualizar_view(request):
    al.actualizarGrafo()
    return render(request, 'adendasActualizar.html')

@csrf_exempt
def probar_view(request):
    if request.method == 'GET' and request.GET.get("descripcion"):
        palabra = request.GET.get("descripcion").split()
        ultima = palabra[len(palabra)-1]
        recomendaciones = al.tres_mas_pesadas(ultima)
        context = {'recomendaciones': recomendaciones,
                   'texto': request.GET.get("descripcion")}
        return render(request, 'adendasProbar.html', context)
    return render(request, 'adendasProbar.html')

@csrf_exempt
def adenda_create_doc(request):
    if request.method == 'POST':
        descripcion = request.POST.get("descripcion")
        adenda = al.create_adenda(descripcion)
        context = {'adendas': adenda}
        return render(request, 'adendas.html', context)