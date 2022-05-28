from django.urls import path
from .views import *


urlpatterns = [
    path('', proyectoss, name="proyectos"),
    path('categoria/<int:categoria_id>/', categoria, name="categoria"),
    path('tecnologia/<int:tecnologia_id>/', tecnologia, name="tecnologia"),
]