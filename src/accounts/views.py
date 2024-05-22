from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User

from .controllers import RegisterController, AuthController

from django.http import HttpResponseBadRequest

def register(request):
    if request.method == "POST":
        controller = RegisterController(request.POST)

        if controller.is_valid():
            controller.save()

            messages.success(request, "Conta criada com sucesso!")

            return redirect("home")


        if controller.user_exists:

            messages.error(request, "Informações já cadastradas. Por favor, faça login.")

            return redirect("login")

        
        context = {"form": controller}

        return render(request, "accounts/tela-cadastro.html", context)

    if request.user.is_authenticated:
        return redirect("home")
    
    controller = RegisterController()

    context = {"form": controller}

    return render(request, "accounts/tela-cadastro.html", context)

def signIn(request):
    if request.method == "POST":  
        controller = AuthController(request.POST)
        
        if controller.login_option == 'email':
            if not controller.valid_email:
                messages.error(request, "Email inválido.")
                return redirect("login")

        elif controller.login_option == 'cpf':
            if not controller.valid_cpf:
                messages.error(request, "CPF Inválido.")
                return redirect("login")
            
        else:
            return HttpResponseBadRequest("Houve um erro inesperado...")

        
        if not controller.user_exists:
            messages.error(request, "Usuário não existe. Por favor crie uma conta.")
            return redirect("register")
        
        if controller.authenticate(request):
            return redirect("home")
        
        else:
            messages.error(request, "Senha incorreta.")
            return redirect("login")

        
    controller = AuthController()    
    
    if controller.is_authenticated(request):
        return redirect("home")
    
    context = {"form": controller}

    return render(request, "accounts/tela-login.html", context)

def signOut(request):
    AuthController.logout(request)
    return redirect("home")

def home(request):
    context = {}

    if AuthController.is_authenticated(request):
        context['user'] = request.user.email.split("@")[0]

    return render(request, "accounts/home.html", context)
