from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from systems_products.models import SystemsProduct
from .models import Page

def index(request, c_slug=None):

    products = SystemsProduct.objects.order_by('order_by').filter(is_published=True)
    about = Page.objects.filter(slug__exact='about-us')
   
    context = {
        'products':products,
        'about':about
    }

    return render(request, 'pages/index.html', context)


def about(request):
    products = SystemsProduct.objects.order_by('order_by').filter(is_published=True)
    about = Page.objects.filter(slug__exact='about-us')
    
    context = {
        'products':products,
        'about': about
    }
    return render(request, 'pages/about.html', context)




