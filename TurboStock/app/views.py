from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse("Index page")

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
