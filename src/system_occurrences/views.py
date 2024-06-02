from django.shortcuts import render, redirect
from django.contrib import messages
from .controllers import EnvioCrimeController
from django.contrib.auth.decorators import login_required

@login_required
def enviar_ocorrencia(request):
    template = "system_occurrences/tela-informar-crime.html"
    
    if request.method == 'POST':
        
        controller = EnvioCrimeController(data=request.POST)
        
        if controller.is_valid():
            controller.save()
            messages.success(request, "A ocorrência foi enviada com sucesso!")
            return redirect("home")
        
        context = {'form': controller, 'invalidform': 'true'}
        
        return render(request, template, context)
        
    controller = EnvioCrimeController()
    
    context = {'form': controller}
    
    return render(request, template, context)