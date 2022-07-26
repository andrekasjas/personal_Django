from django.shortcuts import render
from django.contrib.auth.models import User

# Create your views here.

def home(request):
    user = User.objects.last()
    url = "https://res.cloudinary.com/dc1hb2uev/image/upload/fl_attachment/{}/personal/yo/CV_Andres_Mogollon.pdf".format(user.first_name)
    return render(request, 'Home/home.html',{"url":url})
