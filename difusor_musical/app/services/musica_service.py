from PIL import Image
from ..models import Musica

def cadastrar_musica(musica):
    Musica.objects.create(titulo=musica.titulo, usuario=musica.usuario)

def listar_musicas(usuario):
    return Musica.objects.filter(usuario=usuario).all()

def listar_musicas_id(id):
    return Musica.objects.get(id=id)

def editar_musica(musica_bd, musica_nova):
    musica_bd.titulo = musica_nova.titulo
    musica_bd.save(force_update=True)

def remover_musica(musica_bd):
    musica_bd.delete()