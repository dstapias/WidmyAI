from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
       path('recomendacion/', views.adendas_view, name='adendas_view'),
       path('actualizar/', views.actualizar_view, name='actualizar_view'),
       path('probar/', views.probar_view, name='probar_view'),
]
