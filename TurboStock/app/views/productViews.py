
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login as log_in, logout as log_out


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
