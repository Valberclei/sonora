from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from ..forms import PostForm
from ..models import PostImage
from django.contrib.auth.mixins import LoginRequiredMixin


class HomePageView(ListView):
    model = PostImage
    template_name = "home.html"

class CreatePostView(LoginRequiredMixin, CreateView):
    form_class = PostForm
    model = PostImage
    template_name = "post.html"
    success_url = reverse_lazy("home")

def cadastrar_usuario(request):
    if request.method == 'POST':
        form_usuario = UserCreationForm(request.POST)
        if form_usuario.is_valid():
            form_usuario.save()
            return redirect('listar_musicas')
    else:
        form_usuario = UserCreationForm()
    return render(request, 'usuarios/form_usuario.html', {"form_usuario": form_usuario})

def logar_usuario(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        usuario = authenticate(request, username=username, password=password)
        if usuario is not None:
            login(request, usuario)
            return redirect('listar_musicas')
        else:
            messages.error(request, 'Credenciais incorretas')
            return redirect('logar_usuario')
    else:
        form_login = AuthenticationForm()
    return render(request, 'usuarios/login.html', {"form_login": form_login})

def deslogar_usuario(request):
    logout(request)
    return redirect('logar_usuario')