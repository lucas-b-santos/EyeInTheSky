from django.shortcuts import render, redirect
from .forms import UserRegisterForm, LoginForm
from django.contrib import messages
from django.contrib import auth

def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST) or None

        if form.is_valid():
            form.save()

            messages.success(request, "Conta criada com sucesso!")

            return redirect("home")

        data = {}

        for field in form.fields:
            if form.has_error(field):
                data[field] = None
            else:
                data[field] = form.cleaned_data[field]

        form.data = data
        context = {"form": form}
        return render(request, "accounts/tela-cadastro.html", context)

    else:
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
