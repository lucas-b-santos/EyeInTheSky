from django.shortcuts import render, redirect
from .forms import UserRegisterForm, LoginForm
from django.contrib import messages
from django.contrib import auth
from .models import User

def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)

        cpf = request.POST.get('cpf')
        email = request.POST.get('email')

        if User.objects.filter(cpf=cpf).exists() or User.objects.filter(email=email).exists():
            messages.error(request, "Informações já cadastradas. Por favor, faça login.")

            return redirect("login")

        if form.is_valid():
            form.save()

            messages.success(request, "Conta criada com sucesso!")

            return redirect("home")

        context = {"form": form}

        return render(request, "accounts/tela-cadastro.html", context)

    if request.user.is_authenticated:
        return redirect("home")
    
    form = UserRegisterForm()

    context = {"form": form}

    return render(request, "accounts/tela-cadastro.html", context)

def signIn(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = auth.authenticate(request, username=username, password=password)

        if user is not None:
            form = auth.login(request, user)
            return redirect("home")
        else:
            messages.error(request, "Usuário não existe. Favor crie uma conta.")
            return redirect("register")
        
    if request.user.is_authenticated:
        return redirect("home")
    
    form = LoginForm()

    context = {"form": form}

    return render(request, "accounts/tela-login.html", context)

def signOut(request):
    auth.logout(request)
    return redirect("home")

def home(request):
    context = {}

    if request.user.is_authenticated:
        context['user'] = request.user.email.split("@")[0]

    return render(request, "accounts/home.html", context)
