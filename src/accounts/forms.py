from  django import forms
from .models import User

from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm, UsernameField
from django.utils.translation import gettext_lazy as _

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(label="Email:")
    cpf = forms.CharField(label="CPF:", max_length=14)

    password2 = forms.CharField(
        label="Confirme a Senha:",
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
        strip=False,
    )

    class Meta:
        model = User
        fields = ["email", "cpf", "password1", "password2"]
        
    def __init__(self, *args, **kwargs): 
        super().__init__(*args, **kwargs)  
        for field_name, field in self.fields.items():   
            field.widget.attrs['class'] = 'form-control' 
            if field_name == "cpf":
                field.widget.attrs['placeholder'] = '___.____.___-__' 
            if 'password' in field_name:
                field.widget.attrs['class'] += ' password-input' 


    

    

class LoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={"autofocus": True}))

    password = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "current-password"}),
    )

    def __init__(self, *args, **kwargs): 
        super().__init__(*args, **kwargs)  
        for field_name, field in self.fields.items():   
            field.widget.attrs['class'] = 'form-control' 
          
       
