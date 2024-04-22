from  django import forms
from .models import User

from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(label="Email:")
    cpf = forms.CharField(label="CPF:", max_length=14)

    class Meta:
        model = User
        fields = ["email", "cpf", "password1", "password2"]
        
    def __init__(self, *args, **kwargs): # Adiciona 
        super().__init__(*args, **kwargs)  
        for field_name, field in self.fields.items():   
              field.widget.attrs['class'] = 'form-control' 
   
          
       
