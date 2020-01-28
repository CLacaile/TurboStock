from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login as log_in, logout as log_out


from app.models import *


def aisle(request, store_id, aisle_id):
    """ View function detail page of an aisle """
    if not request.user.is_authenticated:
        print("not authenticated")
        return render(request, 'login.html', status=401)
    else:
        store = get_object_or_404(Store, pk=store_id)
    aisle = get_object_or_404(Aisle, pk=aisle_id)
    aisle_manager = AisleManager.objects.filter(aisle_id=aisle_id)
    aisle_managers = AisleManager.objects.all()
    stocks = Stock.objects.filter(aisle_id=aisle_id)
    products = Product.objects.all()
    context = {
        'aisle': aisle,
        'aisle_manager': aisle_manager,
        'aisle_managers': aisle_managers,
        'stocks': stocks,
        'products': products,
    }
    return render(request, 'aisle.html')

def create_aisle(request,store_id):
    #TODO
    return render(request, 'aisle.html')

def delete_aisle(request,store_id,aisle_id):
    #TODO
    return render(request, 'aisle.html')

def new_aisle(request,store_id):
    #TODO
    return render(request, 'aisle.html')
