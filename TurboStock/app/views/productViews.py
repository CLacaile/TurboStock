from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from app.authentication import authentication

from app.models import *

def product(request, product_id):
    """ View function : detail page of a product """
    if not request.user.is_authenticated:
        print("not authenticated")
        return render(request, 'login.html', status=401)
    else:
        product = get_object_or_404(Product, pk=product_id)
    context = {
        "product": product,
    }
    return render(request, 'product.html', context=context)

def create_product(request):
    if not request.user.is_authenticated:
        print("not authenticated")
        return render(request, 'login.html', status=401)
    try:
        name = request.POST['name']
        unit_price = request.POST['unit_price']
        product = Product.objects.create(name=name, unit_price=unit_price)
        product.save()
    except:
        return render(request, 'newProduct.html')
    return redirect('home')

def new_product(request):
    if not request.user.is_authenticated:
        print("not authenticated")
        return render(request, 'login.html', status=401)
    path = request.path
    context = {
        'next': path
    }
    return render(request, 'newProduct.html')

def update_product(request, product_id):
    if not request.user.is_authenticated:
        print("not authenticated")
        return render(request, 'login.html', status=401)
    else:
        product = get_object_or_404(Product, pk=product_id)
        name = request.POST['name']
        unit_price = request.POST['unit_price']
        product.name = name
        product.unit_price = unit_price
        product.save()
        context = {
            "product": product,
        }
        return render(request, 'product.html', context=context)
