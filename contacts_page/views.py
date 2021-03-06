# import json
# import urllib
import requests

from django.shortcuts import render, redirect, HttpResponse
from systems_products.models import SystemsProduct
from django.contrib import messages

from .models import Contact
from pages.models import Page
from django.conf import settings
import base64
from django.core.mail import send_mail, BadHeaderError
import os
from django.core.mail import EmailMessage
from django.template.loader import render_to_string


# Create your views here.
def contact_us(request):
    products = SystemsProduct.objects.order_by('order_by').filter(is_published=True)
    contact_sidebar = Page.objects.filter(slug__exact='contact-us')
    
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        enquiry = request.POST['enquiry']
        message = request.POST.get('message')

        ''' Begin reCAPTCHA validation '''
        recaptcha_response = request.POST.get('g-recaptcha-response')
        data = {
            'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY,
            'response': recaptcha_response
        }
        r = requests.post('https://www.google.com/recaptcha/api/siteverify', data=data)
        result = r.json()

        ''' End reCAPTCHA validation '''

        if result['success']:

            # save to object
            contextEmail = {
                    'name' :name,
                    'email' :email,
                    'phone' :phone,
                    'enquiry' :enquiry,
                    'message' :message,
            }
            # Save to DB
            contact = Contact(name=name, email=email, phone=phone, enquiry=enquiry,  message=message)
            contact.save()

            try:
                #settings.EMAIL_HOST_USER,
                mail = EmailMessage(
                    'Email inquiry from ' + name, 
                    # 'Contact Number: ' +  phone + '.'+ '%0A' + message + '\n', 
                    render_to_string('contacts/email.html', contextEmail),
                    email,
                    [settings.EMAIL_HOST_USER], 
                    reply_to=[email]              
                )

                mail.content_subtype = 'html'
                mail.send(fail_silently=False)

            except BadHeaderError:
                return HttpResponse('Invalid header found')

            return redirect('/contact-us/thank-you')

        else:
            messages.error(request, 'Invalid reCAPTCHA. Please check the checkbox and try again.')
            return redirect('contact-us')
    
    context = {
        'products':products,
        'contact_sidebar':contact_sidebar
    }

    return render(request, 'contacts/contacts.html', context)

def thank_you(request):
    products = SystemsProduct.objects.order_by('order_by').filter(is_published=True)
    context = {
        'products':products,
    }
    return render(request, 'contacts/thank_you.html', context)