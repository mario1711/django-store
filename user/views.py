from django.shortcuts import render , redirect
from django.http import HttpResponse
from django.views.generic import View
from django.contrib.auth.forms import  AuthenticationForm
from .forms import FormularioRegistro
from django.contrib import messages
from django.contrib.auth import login , logout , authenticate
from django.contrib.auth.views import PasswordResetView
from django.contrib.auth.decorators import login_required
from .forms import ReviewForm
from django.contrib.auth.forms import PasswordResetForm, SetPasswordForm


# Create your views here.
def acceder(request):
    if request.method == "POST":
        form = AuthenticationForm(request , data= request.POST)
        if form.is_valid():
            nombre_usuario = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            usuario = authenticate(username = nombre_usuario , password = password)
            if usuario is not None:
                login(request , usuario)
                messages.success(request , f"Bienvenido de nuevo {nombre_usuario}")
                return redirect("inicio")
            else:
                messages.error(request , "Los datos son incorrectos")
        else:

            messages.error(request , "Los datos son incorrectos")
            
    form = AuthenticationForm()
    return render(request , "user/acceder.html" , {"form": form})


class VistaRegistro(View):
    def get(self, request):
        form = FormularioRegistro()
        return render(request, "user/registro.html", {"form": form})

    def post(self, request):
        form = FormularioRegistro(request.POST)
        if form.is_valid():
            usuario = form.save()
            nombre = form.cleaned_data.get("username")
            messages.success(request, f"Bienvenido {nombre}")
            login(request, usuario)
            return redirect("inicio")
        else:
            for msg in form.error_messages:
                messages.error(request, form.error_messages[msg])
            return render(request, "user/registro.html", {"form": form})

def salir(request):
    logout(request)
    messages.success(request , f'Tu sesion se ha cerrado correctamente')
    return redirect("acceder")

class CustomPasswordResetView(PasswordResetView):
    template_name = 'user/password_reset.html'
    email_template_name = 'user/password_reset_email.html'
    success_url = '/user/password_reset/done/'

@login_required
def publicar_resena(request):
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.usuario = request.user
            review.save()
            return redirect('inicio')  # Redirigir a la página principal después de publicar la reseña
    else:
        form = ReviewForm()
    return render(request, 'user/anadir_resena.html', {'form': form})