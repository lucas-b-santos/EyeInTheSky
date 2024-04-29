from django.urls import path
from . import views as v

urlpatterns = [
    path("register/", v.register, name="register"),
    path("login/", v.signIn, name="login"),
    path("logout/", v.signOut, name="logout"),
    path("", v.home, name="home"),
]
