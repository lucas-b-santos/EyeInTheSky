from .forms import UserRegisterForm, LoginForm, CPF_VALIDATOR
from .models import User
from django.contrib import auth

from django.core.validators import EmailValidator

class CustomEmailValidator(EmailValidator):
    def __call__(self, value: str) -> bool:

        if not value or "@" not in value or len(value) > 320:
            return False

        user_part, domain_part = value.rsplit("@", 1) 

        if not self.user_regex.match(user_part): # valida o user do email
            return False
        
        if not self.validate_domain_part(domain_part): #valida o dominio email
            return False
        
        return True
    
email_validator = CustomEmailValidator()

class RegisterController(UserRegisterForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self._email = self.data.get('email')
        self._cpf = self.data.get('cpf')
        

    @property
    def user_exists(self) -> bool:
        if User.objects.filter(cpf=self._cpf).exists() or User.objects.filter(email=self._email).exists():
            return True
        
        return False

class AuthController(LoginForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self._email = self.data.get('username')
        self._cpf = self.data.get('cpf')
        self._password = self.data.get('password')
        self._username = None
        self._login_option= self.data.get('login_option')
        
    @property
    def login_option(self) -> str:
        return self._login_option
    
    @property
    def valid_email(self) -> bool:
        return email_validator(self._email)
            
    @property
    def valid_cpf(self) -> bool:
        return CPF_VALIDATOR.validate(self._cpf)
    
    @property
    def user_exists(self) -> bool:
        '''Retorna True caso usuário exista e False caso contrário'''
        
        try:
            if self._login_option == "cpf":
                self._username = User.objects.get(cpf=self._cpf).email
                
            else:
                self._username = User.objects.get(email=self._email).email
                        
            return True

        except:
            return False
        
    def authenticate(self, request) -> bool:
        user = auth.authenticate(request, username=self._username, password=self._password)

        if user is not None:
            auth.login(request, user)
            return True
        
        return False
    
    @staticmethod
    def logout(request) -> None:
        auth.logout(request)
        
    @staticmethod
    def is_authenticated(request) -> bool:
        
        if request.user.is_authenticated:
            return True 
        
        return False
        
        
            
        
