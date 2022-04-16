from django.contrib import admin
from django.urls import path
from .views.musica_views import *
from .views.usuario_views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('listar_musicas/', listar_musicas, name='listar_musicas'),
    path('cadastrar_musica/', cadastrar_musica, name='cadastrar_musica'),
    path('editar_musica/<int:id>', editar_musica, name='editar_musica'),
    path('remover_musica/<int:id>', remover_musica, name='remover_musica'),
    path('cadastrar_usuario/', cadastrar_usuario, name='cadastrar_usuario'),
    path('logar_usuario/', logar_usuario, name='logar_usuario'),
    path('deslogar_usuario/', deslogar_usuario, name='deslogar_usuario'),
    path("", HomePageView.as_view(), name="home"),
    path("post/", CreatePostView.as_view(), name="add_post"),
]