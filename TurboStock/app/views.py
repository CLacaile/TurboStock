from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login as log, logout as out

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
        return render(request,'home.html')
    else:
        print("Authentification failed : bad credentials")
        return render(request, 'login.html')


def store(request):
    """ View fonction detail page of a store """
    stores_list = Store.objects.all()
    context = {
        'stores_list': stores_list,
    }
    return render(request, 'index.html', context=context)


def store_detail(request, store_id):
    """ View fonction detail page of a store """
    store = Store.objects.filter(id=store_id)
    context = {
        'store': store,
    }
    return render(request, 'index.html', context=context)