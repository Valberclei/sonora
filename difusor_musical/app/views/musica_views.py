from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from ..forms import MusicaForm
from ..entidades.musica import Musica
from ..services import musica_service

# Create your views here.

@login_required()
def listar_musicas(request):

    musicas = musica_service.listar_musicas(request.user)
    return render(request, 'musicas/listar_musicas.html', {"musicas": musicas})

@login_required()
def cadastrar_musica(request):
    if request.method == "POST":
        form_musica = MusicaForm(request.POST)
        if form_musica.is_valid():
            titulo = form_musica.cleaned_data["titulo"]
            musica_nova = Musica(titulo=titulo, usuario=request.user)
            musica_service.cadastrar_musica(musica_nova)
            return redirect('listar_musicas')
    else:
        form_musica = MusicaForm()
    return render(request, 'musicas/form_musica.html', {"form_musica": form_musica})

@login_required()
def editar_musica(request, id):
    musica_bd = musica_service.listar_musicas_id(id)
    if musica_bd.usuario != request.user:
        return HttpResponse("Não permitido")
    form_musica = MusicaForm(request.POST or None, instance=musica_bd)
    if form_musica.is_valid():
        titulo = form_musica.cleaned_data["titulo"]
        musica_nova = Musica(titulo=titulo, usuario=request.user)
        musica_service.editar_musica(musica_bd, musica_nova)
        return redirect('listar_musicas')
    return render(request, 'musicas/form_musica.html', {"form_musica": form_musica})

@login_required()
def remover_musica(request, id):
    musica_bd = musica_service.listar_musicas_id(id)
    if musica_bd.usuario != request.user:
        return HttpResponse("Não permitido")
    if request.method == "POST":
        musica_service.remover_musica(musica_bd)
        return redirect('listar_musicas')
    return render(request, 'musicas/confirma_exclusao.html', {'musica': musica_bd})