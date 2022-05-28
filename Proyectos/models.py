from django.db import models
from django.contrib.auth.models import User
from pkg_resources import require

# Create your models here.

class categorias(models.Model):
    nombre = models.CharField(max_length=60)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'categoria'
        verbose_name_plural = 'categorias'
    
    def __str__(self):
        return self.nombre

class tecnologias(models.Model):
    nombre = models.CharField(max_length=60)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'tecnologia'
        verbose_name_plural = 'tecnologias'
    
    def __str__(self):
        return self.nombre

class proyectos(models.Model):
    nombre = models.CharField(max_length=60)
    descripcion = models.CharField(max_length=250)
    imagen = models.ImageField(upload_to = 'proyecto', null = True, blank = True)
    git = models.URLField(max_length=130)
    host = models.URLField(max_length=130)
    categoria = models.ForeignKey(categorias, on_delete= models.CASCADE, default="")
    tecnologia = models.ManyToManyField(tecnologias)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'proyecto'
        verbose_name_plural = 'proyectos'
    
    def __str__(self):
        return self.nombre