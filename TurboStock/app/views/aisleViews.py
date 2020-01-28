from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login as log_in, logout as log_out
from app.authentication import authentication

from app.models import *


def aisle(request, store_id, aisle_id):
    """ View function detail page of an aisle """
    if not request.user.is_authenticated:
        print("not authenticated")
        return render(request, 'login.html', status=401)
    try:
        store = Store.objects.get(id=store_id)
        aisle = Aisle.objects.get(id=aisle_id)

    except Exception as e :
        print(e)
        return redirect('home')

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


def create_aisle(request, store_id):
    """ Create a new aisle from newAisle.html """
    if not request.user.is_authenticated:
        print("not authenticated")
        return render(request, 'login.html', status=401)
    try:
        store = Store.objects.get(id=store_id)
    except:
        return redirect('home')
    if not authentication.has_permission_on_item(request.user, store):
        return render(request, 'login.html', status=401)
    try:
        name = request.POST['name']
        aisle = Aisle.objects.create(name=name, store=store)
        aisle.save()
    except:
        context = {
        'user': request.user,
        'store': store,
        }
        return render(request, 'newAisle.html', context=context)
    return redirect('/store/'+ str(store_id))


def delete_aisle(request, store_id, aisle_id):
    """ Delete an aisle """
    if not request.user.is_authenticated:
        print("not authenticated")
        return render(request, 'login.html', status=401)
    try:
        store = Store.objects.get(id=store_id)
        aisle = Aisle.objects.get(id=aisle_id)
    except:
        return redirect('home')
    if not authentication.has_permission_on_item(request.user, aisle):
        return render(request, 'login.html', status=401)
    aisle.delete()
    return redirect('/store/'+str(store_id))


def new_aisle(request, store_id):
    """ Render newAisle.html the form to create a new aisle """
    if not request.user.is_authenticated:
        print("not authenticated")
        return render(request, 'login.html', status=401)
    try:
        store = Store.objects.get(id=store_id)
    except:
        return redirect('home')
    if not authentication.has_permission_on_item(request.user, store):
        return render(request, 'login.html', status=401)
    context = {
        'user': request.user,
        'store': store,
    }
    return render(request, 'newAisle.html', context=context)

def update_aisle(request, store_id, aisle_id):
    """ Update an aisle with values input in aisle.html """
    if not request.user.is_authenticated:
        print("not authenticated")
        return render(request, 'login.html', status=401)
    try:
        store = Store.objects.get(id=store_id)
        aisle = Aisle.objects.get(id=aisle_id)
    except:
        return redirect('home')
    if not authentication.has_permission_on_item(request.user, store):
        return render(request, 'login.html', status=401)
    try:
        name = request.POST['name']
        manager_id = request.POST['manager']
        # update Aisle
        aisle = Aisle.objects.get(id=aisle_id)
        aisle.name = name
        aisle.save()
        # update AisleManager
        aisle_manager = AisleManager.objects.get(id=manager_id)
        aisle_manager.aisle = aisle
        aisle_manager.save()
    except:
        context = {
        'user': request.user,
        'store': store,
        'aisle': aisle,
        #'aisle_manager': aisle_manager,
        }
        print("ko")
        return redirect('aisle', store_id=store_id, aisle_id=aisle_id)
    return redirect('/store/'+ str(store_id))