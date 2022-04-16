from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Musica(models.Model):
    titulo = models.CharField(max_length=30, null=False, blank=False)
    usuario = models.ForeignKey(User, null=True, on_delete=models.CASCADE)

class PostImage(models.Model):
    title = models.TextField(max_length=200, null=True, blank=True)
    cover = models.ImageField(upload_to='images/')
    def __str__(self):
      return self.title