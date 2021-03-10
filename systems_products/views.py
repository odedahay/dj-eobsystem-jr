from django.shortcuts import render, get_object_or_404
from .models import SystemsProduct
from systems_products.models import SystemsProduct
# Create your views here.


def systems_products(request):

    products = SystemsProduct.objects.order_by('order_by').filter(is_published=True)

    context = {
        'products':products
    }

    return render(request, 'systems_products/systems_products_list.html', context)


def systems_product_details(request, c_slug=None):

    products = SystemsProduct.objects.order_by('order_by').filter(is_published=True)
    products_details = get_object_or_404(SystemsProduct, slug=c_slug)

    context = {
        'products': products,
        'products_details': products_details,
    }

    return render(request, 'systems_products/systems_product.html', context)