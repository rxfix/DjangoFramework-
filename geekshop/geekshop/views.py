from django.shortcuts import render

from basketapp.models import Basket
from mainapp.models import Product



def index(request):
    title = 'Geekshop'
    products = Product.objects.all()[:5]
    basket = []
    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user)
    context = {
        'title': title,
        'products': products,
        'basket': basket,
    }
    return render(request, 'geekshop/index.html', context)


def contacts(request):
    title = 'контакты'
    context = {
        'title': title,
    }
    return render(request, 'geekshop/contacts.html', context)
