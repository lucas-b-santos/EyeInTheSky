from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from django.contrib import messages

def register(request):
    
    if request.method == "POST":
        form = UserRegisterForm(request.POST) or None

        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(
                request, f"Your account has been created! You are now able to log in"
            )
            return redirect("accounts_home")

        data = {}

        for field in form.fields:
            if form.has_error(field):
                data[field] = None
            else:
                data[field] = form.cleaned_data[field]            

        form.data = data
        context = {"form": form}
        return render(request, 'accounts/tela-cadastro.html', context) 
        
    else:    
        form = UserRegisterForm()
        context = {'form': form}
            
    
        return render(request, "accounts/tela-cadastro.html", context)
    
def home(request):
    return render(request, 'accounts/home.html')