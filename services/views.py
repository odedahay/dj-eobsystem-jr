from django.shortcuts import render

from .models import Service
from systems_products.models import SystemsProduct

def services(request):
    services = Service.objects.order_by('order_by').filter(is_published=True)
    products = SystemsProduct.objects.order_by('order_by').filter(is_published=True)
    
    context = {
        'services':services,
         'products':products,
    }

    return render(request, 'services/services_list.html', context)