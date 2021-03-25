from django.urls import path
from . import views

urlpatterns = [
    path('', views.contact_us, name='contact-us'),
    path('thank-you', views.thank_you, name='thank_you'),
]