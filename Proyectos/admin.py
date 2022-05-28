from django.contrib import admin
from .models import categorias, tecnologias, proyectos
# Register your models here.

class categoria_admin(admin.ModelAdmin):
    readonly_fields=('created','updated')

class tecnologia_admin(admin.ModelAdmin):
    readonly_fields=('created','updated')

class proyecto_admin(admin.ModelAdmin):
    readonly_fields=('created','updated')

admin.site.register(categorias, categoria_admin)
admin.site.register(tecnologias, tecnologia_admin)
admin.site.register(proyectos, proyecto_admin)