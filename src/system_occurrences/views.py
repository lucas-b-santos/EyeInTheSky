from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Ocorrencia

# Create your views here.

def enviar_ocorrencia(request):
    return render(request, "system_occurences/tela-informar-crime.html")