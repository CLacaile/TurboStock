from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login as log, logout as out

from .models import AisleManager, StoreManager
from .models import User

def home(request):
    #print(type(request.user.child_object()).__name__)
    if request.user.is_authenticated:
        return render(request, 'home.html')
    else:
        print("not authenticated")
        return render(request, 'login.html')


def login(request):
    try:
        user = User(first_name="test", last_name="test", email="test", password="test")
        user.save()
    except:
        print("User test already exist")

    return render(request, 'login.html')


def logout(request):
    out(request)
    return render(request, 'login.html')


def auth(request):
    username = request.POST['username']
    password = request.POST['password']
    print("username = " + username)
    print("password = " + password)
    user = authenticate(request, username=username, password=password)

    if user is not None:
        log(request, user)
        return render(request, 'home.html')
    else:
        print("Authentification failed : bad credentials")
        return render(request, 'login.html')


def store(request):
    """ View fonction detail page of a store """
    stores = Store.objects.all()
    store_managers = StoreManager.objects.all()
    context = {
        'stores': stores,
        'store_managers': store_managers,
    }
    return render(request, 'index.html', context=context)


def store_detail(request, store_id):
    """ View fonction detail page of a store """
    store = Store.objects.filter(id=store_id)
    store_manager = StoreManager.objects.filter(store_id=store_id)
    context = {
        'store': store,
        'store_manager': store_manager,
    }
    return render(request, 'index.html', context=context)