from django.urls import path

from . import views

app_name = 'systems_product'

urlpatterns = [
    path('', views.systems_products, name='systems_products'), 
    path('<slug:c_slug>/', views.systems_product_details, name='systems_product_details'), 
]