from django.shortcuts import render, redirect
from django.contrib import messages
from .controllers import EnvioCrimeController
from django.contrib.auth.decorators import login_required
from .models import Ocorrencia
from pytz import timezone
from core.settings import TIME_ZONE
import json


@login_required
def enviar_ocorrencia(request):
    template = "system_occurrences/tela-informar-crime.html"

    if request.method == 'POST':

        # passa para controlador as informações que o usuário enviou
        controller = EnvioCrimeController(request.POST, request.FILES)

        # caso informações válidas
        if controller.is_valid():

            # salva ocorrência, informando o usuário associado como parâmetro
            controller.saveOccurrence(request.user.id)

            # informa sucesso e retorna para tela inicial
            messages.success(request, "A ocorrência foi enviada com sucesso!")
            return redirect("home")

        # caso dados inválidos, envia formulário já populado
        context = {'form': controller, 'invalidForm': 'true'}
        return render(request, template, context)

    controller = EnvioCrimeController()

    # controlador é usado para gerar formulário no HTML, pois tem acesso aos atributos do Model
    context = {'form': controller}
    return render(request, template, context)


# VIEW USADA APENAS PARA APRESENTAR PARA O PROFESSOR... POR FAVOR IGNORAR
def ver_ocorrencias(request):
    ocorrencias = []

    for ocorrencia in Ocorrencia.objects.all():

        ocorrencias.append({"data_hora": ocorrencia.data_hora.astimezone(timezone(TIME_ZONE)),
                          "tipo": ocorrencia.tipo_crime,
                          "localizacao": ocorrencia.localizacao})
        
    context = {'ocorrencias': ocorrencias}

    return render(request, "system_occurrences/visualizar_crimes.html", context)
