from django.urls import path
from .views import *

urlpatterns = [
    path('', contactame, name="contactame"),
]
