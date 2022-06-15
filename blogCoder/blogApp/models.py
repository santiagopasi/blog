from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class TagManager(models.Manager):
    def crear_tag(self, tag):
        tag = self.create(tag=tag)
        # do something with the book
        return tag

class Tag(models.Model):
    tag = models.CharField(max_length=100)
    
    objects = TagManager()

    def __str__(self):
        return self.tag

    



class Post(models.Model):
    titulo = models.CharField(max_length=200)
    cuerpo = models.TextField()
    creado = models.DateTimeField(auto_now_add=True)
    actualizado = models.DateTimeField(auto_now=True)
    creado_por = models.ForeignKey(User, on_delete=models.CASCADE)
    tags=models.ManyToManyField('Tag',blank=True)
    class TipoPost(models.TextChoices):
        pelicula = 'Pelicula'
        libro='Libro'
        
    
    tipo_post = models.CharField(choices= TipoPost.choices, max_length=40)
