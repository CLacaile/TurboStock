from django.contrib.auth import authenticate, login as log, logout as out
from django.shortcuts import render

# Create your views here.
from app.models import AisleManager
from app.models import User


def home(request):
    print(type(request.user.child_object()).__name__)
    if request.user.is_authenticated:
        return render(request, 'home.html')
    else:
        print("not authenticated")
        return render(request, 'login.html')


def login(request):
    #user = User(first_name="test", last_name="test", email="test", password="test")
    #user.save()
    return render(request, 'login.html')

def logout(request):
    out(request)
    return render(request, 'login.html')


def auth(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)

    if user is not None:
        log(request, user)
        return render(request, 'home.html')
    else:
        print("Authentification failed : bad credentials")
        return render(request, 'login.html')
