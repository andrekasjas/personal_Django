from django.shortcuts import render, redirect
from .forms import Formulario_contacto
from django.core.mail import EmailMessage
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.

def contactame(request):
    if (request.method == "POST"):
        formulario = Formulario_contacto(data = request.POST)
        if (formulario.is_valid()):
            nombre = request.POST.get('nombre') 
            email = request.POST.get('email') 
            contenido = request.POST.get('contenido') 
            # mensaje = 'Hola soy {}, mi correo es {} me comunico para decirte que: \n\n{}'.format(nombre,email,contenido)
            email = EmailMessage('PERSONAL WEBSITE ANDRES:', 
            'Hola soy {}, mi correo es {} me comunico para decirte que: \n\n{}'.format(nombre,email,contenido), 
            '', [settings.EMAIL_HOST_USER], ['andresmogollob@gmail.com','erikadayanatobi@gmail.com','cabeza_1245@hotmail.com'])

            try:
                email.send()
                return redirect('/contactame/?valido')
            except:
                return redirect('/contactame/?novalido')
            # try:
            #     send_mail(nombre, mensaje, 'andresmogollob@gmail.com', ['andresmogollob@gmail.com','erikadayanatobi@gmail.com'])
            # except:
            #     return redirect('/contactame/?novalido')
            # return redirect('/contactame/?valido')

    else:
        formulario = Formulario_contacto()

    return render(request, "Contactame/contactame.html",{'formulario':formulario})