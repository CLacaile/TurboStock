from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login as log_in, logout as log_out
from app.authentication import authentication as au

from app.models import *



def store(request, store_id):
    """ View fonction detail page of a store """
    if not request.user.is_authenticated:
        print("not authenticated")
        return render(request, 'login.html', status=401)
    else:
        store = get_object_or_404(Store, pk=store_id)
    store_managers = StoreManager.objects.all()
    store_manager = StoreManager.objects.filter(store_id=store_id)
    aisles = Aisle.objects.filter(store_id=store_id)
    aisle_managers = AisleManager.objects.filter(aisle_id__in=aisles)
    context = {
        'au': au,
        'user': request.user,
        'store': store,
        'store_managers': store_managers,
        'store_manager': store_manager,
        'aisles': aisles,
        'aisle_managers': aisle_managers,
    }
    return render(request, 'store.html', context=context)


def create_store(request):
    if not request.user.is_authenticated:
        print("not authenticated")
        return render(request, 'login.html', status=401)
    if type(request.user.child_object()).__name__ != CEO.__name__:
        return render(request, 'login.html', status=401)
    try:
        address = request.POST['address']
        city = request.POST['city']
    except:
        return render(request, 'login.html', status=400)
    try:
        store = Store.objects.create(address=address, city=city)
        print(store)
        store.save()
    except:
        return render(request, 'newStore.html', status=400)
    return redirect('home')


def delete_store(request, store_id):
    if not request.user.is_authenticated:
        print("not authenticated")
        return render(request, 'login.html', status=401)
    if type(request.user.child_object()).__name__ != CEO.__name__:
        return render(request, 'login.html', status=401)

    try:
        print(Store.objects.get(id=store_id))
        Store.objects.get(id=store_id).delete()

    except:
        redirect('/home/', status=400)
    return redirect('/home/')


def new_store(request):
    if not request.user.is_authenticated:
        print("not authenticated")
        return render(request, 'login.html', status=401)
    if type(request.user.child_object()).__name__ != CEO.__name__:
        return render(request, 'login.html', status=401)
    return render(request, 'newStore.html', status=200)


