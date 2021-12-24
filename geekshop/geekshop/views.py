from django.shortcuts import render

from mainapp.models import Product


def index(request):
    title = 'Geekshop'
    products = Product.objects.all()[:5]

    context = {
        'title': title,
        'products': products,
    }
    return render(request, 'geekshop/index.html', context)


def contacts(request):
    title = 'контакты'
    context = {
        'title': title,
    }
    return render(request, 'geekshop/contacts.html', context)