from django.shortcuts import render, redirect
from django.contrib import messages
from .controllers import RegisterController, AuthController
from django.http import HttpResponseBadRequest

def register(request):
    '''View responsável pela interface de Registro'''
    
    template = "accounts/tela-cadastro.html"
    
    # usuário enviando dados para o server
    if request.method == "POST":
        
        # instancia um novo controlador informando os dados enviados pelo usúario
        controller = RegisterController(request.POST)

        # caso informações sejam todas válidas
        if controller.is_valid():
            
            # cria novo usuário
            controller.createUser()

            # adiciona mensagem para avisar que conta foi criada e redireciona para tela inicial
            messages.success(request, "Conta criada com sucesso!")
            return redirect("home")

        # caso usuário já exista
        if controller.user_exists:

            # informa que usuário já existe e redireciona para tela de login
            messages.error(request, "Informações já cadastradas. Por favor, faça login.")
            return redirect("login")
        
        # context vai retornar formulário com dados já preenchidos caso informações sejam inválidas
        context = {"form": controller}
        return render(request, template, context)

    # caso usuário já está autenticado redireciona para tela inicial
    if AuthController.is_authenticated(request):
        return redirect("home")
    
    # controlador é usado para gerar formulário no HTML, pois tem acesso aos atributos do Model
    controller = RegisterController()
    context = {"form": controller}

    # retorna interface para usuário
    return render(request, template, context)

def signIn(request):
    '''View responsável pela interface de login'''
    
    # caso usuário enviou dados para o servidor
    if request.method == "POST":  
        
        # controlador instanciado com os dados enviados pelo usuário
        controller = AuthController(data=request.POST)
                
        # caso opção de login for email
        if controller.login_option == 'email':
            
            # se o email for inválido
            if not controller.valid_email:
                
                # recarrega página informando erro para usuário
                messages.error(request, "Email inválido.")
                return redirect("login")

        # caso opção de login for cpf
        elif controller.login_option == 'cpf':
            
            # caso cpf inválido
            if not controller.valid_cpf:
                
                # recarrega página informando erro para usuário
                messages.error(request, "CPF Inválido.")
                return redirect("login")
        
        # caso usuário alterou de forma maliciosa o componente de opção de login
        else:
            return HttpResponseBadRequest("Houve um erro inesperado...")

        # caso usuário não existe
        if not controller.user_exists:
            
            # informa problema, redirecionando para tela de cadastro
            messages.error(request, "Usuário não existe. Por favor crie uma conta.")
            return redirect("register")
        
        # se autenticação foi feita com sucesso, redireciona para tela inicial
        if controller.authenticate(request):
            return redirect("home")
        
        # caso contrário, informa que senha está incorreta
        else:
            messages.error(request, "Senha incorreta.")
            return redirect("login")

    
    controller = AuthController()    
    
    # controlador verifica se usuário já está logado, caso sim redireciona para tela inicial
    if controller.is_authenticated(request):
        return redirect("home")
    
    # controlador é usado para gerar formulário no HTML, pois tem acesso aos atributos do Model
    context = {"form": controller}
    return render(request, "accounts/tela-login.html", context)

def signOut(request):
    '''View que realiza logout do usuário'''
    
    # faz logout do usuário e redireciona para tela inicial
    AuthController.logout(request)
    return redirect("home")

def home(request):
    '''View da tela inicial'''
    
    context = {}

    # caso usuaŕio autenticado, configura para mostrar seu nome na tela inicial
    if AuthController.is_authenticated(request):
        context['user'] = request.user.email.split("@")[0]

    return render(request, "accounts/home.html", context)
