from django.urls import path
from . import views as v

urlpatterns = [
    path("register/", v.register, name="accounts_register"),
    path("home/", v.home, name="accounts_home"),
]
