from django import forms
from .models import *

class MusicaForm(forms.ModelForm):
    class Meta:
        model = Musica
        exclude = ('usuario', )
        fields = '__all__'

class PostForm(forms.ModelForm):
    class Meta:
        model = PostImage
        fields = ["title", "cover"]