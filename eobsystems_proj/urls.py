from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('pages.urls')), 
    path('systems/', include('systems_products.urls')), 
    path('services/', include('services.urls')), 
    path('news-update/', include('news_update.urls', namespace='news_update')), 
    path('contact-us/', include('contacts_page.urls')), 
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
