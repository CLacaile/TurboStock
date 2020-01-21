from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login as log_in, logout as log_out
from app.authentication import authentication as au
from .models import Store
from .models import AisleManager, StoreManager
from .models import User


def get_stores_context():
    """ Prepare stores context

    This function fetches all stores and store managers in DB and wraps the objects
    in a dictionary before being rendered in home.html using render().
    """
    stores = Store.objects.all()
    store_managers = StoreManager.objects.all()
    context = {
        'stores': stores,
        'store_managers': store_managers,
    }
    return context


def home(request):
    """ Home function

    This function renders the list of stores in DB in home.html. It calls get_stores_context().
    """

    if request.user.is_authenticated:

        store = Store.objects.get(id=1)
        print(au.has_permission_on_item(request.user, store))

        context = get_stores_context()
        return render(request, 'home.html', context=context)
    else:
        print("not authenticated")
        return render(request, 'login.html')


def login(request):
    """ Login function

    This function renders login.html
    """
    return render(request, 'login.html')


def logout(request):
    """ Logout function

    This function renders login.html with a farewell message
    """
    log_out(request)
    context = {
        'message': "Vous avez été déconnecté."
    }
    return render(request, 'login.html', context=context)


def auth(request):
    """ User authentication function 

    It uses 'email' and 'password' as inputs names. If the user is correct, 
    it renders 'home.html'. Otherwise it routes the user back to login with a 
    'message' text in context.
    """
    email = request.POST['email']
    password = request.POST['password']
    user = authenticate(request, username=email, password=password)

    if user is not None:
        log_in(request, user)
        # display stores as home page
        context = get_stores_context()
        return render(request, 'home.html', context=context)
    else:
        print("Authentification failed : bad credentials")
        context = {
            'message': "Erreur: l'utilisateur/mot de passe n'existe pas !"
        }
        return render(request, 'login.html', context=context)


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
    store = Store.objects.get(id=store_id)
    store_manager = StoreManager.objects.get(store_id=store_id)
    store_managers = StoreManager.objects.all()
    context = {
        'au': au,
        'user':request.user,
        'store': store,
        'store_manager': store_manager,
        'store_managers': store_managers,
    }
    return render(request, 'store.html', context=context)
