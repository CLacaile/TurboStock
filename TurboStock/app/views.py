from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.contrib.auth import authenticate, login as log_in, logout as log_out

from .models import Store, Aisle, Product, Stock
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



def store(request, store_id):
    """ View fonction detail page of a store """
    store = get_object_or_404(Store, pk=store_id)
    store_managers = StoreManager.objects.all()
    store_manager = StoreManager.objects.filter(store_id=store_id)
    aisles = Aisle.objects.filter(store_id=store_id)
    aisle_managers = AisleManager.objects.filter(aisle_id__in=aisles)
    context = {
        'store': store,
        'store_managers': store_managers,
        'store_manager': store_manager,
        'aisles': aisles,
        'aisle_managers': aisle_managers,
    }
    return render(request, 'store.html', context=context)

def aisle(request, store_id, aisle_id):
    """ View function detail page of an aisle """
    store = get_object_or_404(Store, pk=store_id)
    aisle = get_object_or_404(Aisle, pk=aisle_id)
    aisle_manager = AisleManager.objects.filter(aisle_id=aisle_id)
    aisle_managers = AisleManager.objects.all()
    stocks = Stock.objects.filter(aisle_id=aisle_id)
    products = Product.objects.all() 
    context = {
        'store': store,
        'aisle': aisle,
        'aisle_manager': aisle_manager,
        'aisle_managers': aisle_managers,
        'stocks': stocks,
        'products': products,
    }
    return render(request, 'aisle.html', context=context)

def product(request, product_id):
    """ View function : detail page of a product """
    product = get_object_or_404(Product, pk=product_id)
    context = {
        "product": product,
    }
    return render(request, 'product.html', context=context)