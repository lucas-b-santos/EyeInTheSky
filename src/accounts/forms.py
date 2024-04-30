from typing import Any
from django import forms
from .models import User

from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm, UsernameField
from django.utils.translation import gettext_lazy as _
from validate_docbr import CPF

CPF_VALIDATOR = CPF()

class UserRegisterForm(UserCreationForm, forms.ModelForm):

    email = forms.EmailField(label="Email:", widget=forms.EmailInput(attrs={"type":"text"}))
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
            field.widget.attrs["class"] = "form-control"

            if field_name == "cpf":
                field.widget.attrs["placeholder"] = "___.____.___-__"

    def clean_cpf(self):
        data = self.cleaned_data.get("cpf")

        if CPF_VALIDATOR.validate(data):
            return data
        else:
            raise ValidationError(_("Informe um CPF válido."))

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
            field.widget.attrs["class"] = "form-control"
            
