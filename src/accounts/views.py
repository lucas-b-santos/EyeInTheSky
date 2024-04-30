from django.shortcuts import render, redirect
from .forms import UserRegisterForm, LoginForm, CPF_VALIDATOR
from django.contrib import messages
from django.contrib import auth
from .models import User

from django.http import HttpResponseBadRequest

from django.core.validators import EmailValidator

class CustomEmailValidator(EmailValidator):
    def validate(self, value):

        if not value or "@" not in value or len(value) > 320:
            return False

        user_part, domain_part = value.rsplit("@", 1)

        if not self.user_regex.match(user_part):
            return False
        
        if not self.validate_domain_part(domain_part):
            return False
        
        return True
    
email_validator = CustomEmailValidator()

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
        password = request.POST.get("password")

        if request.POST.get("login_option") == 'email':
            username = request.POST.get("username")

            if not email_validator.validate(username):
                messages.error(request, "Email inválido.")
                return redirect("login")

        elif request.POST.get("login_option") == 'cpf':
            cpf = request.POST.get("cpf")

            if not CPF_VALIDATOR.validate(cpf):
                messages.error(request, "CPF Inválido.")
                return redirect("login")
            
            try:
                username = User.objects.get(cpf=cpf).email
            except:
                messages.error(request, "Usuário não existe. Por favor crie uma conta.")
                return redirect("register")

        else:
            return HttpResponseBadRequest("Houve um erro inesperado...")

        user = auth.authenticate(request, username=username, password=password)

        if user is not None:
            form = auth.login(request, user)
            return redirect("home")
        
        elif not User.objects.filter(email=username).exists():
            messages.error(request, "Usuário não existe. Por favor crie uma conta.")
            return redirect("register")
        
        else:
            messages.error(request, "Senha incorreta.")
            return redirect("login")

        
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
