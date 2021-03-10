from django.contrib import admin

from .models import Service

class ServicesAdmin(admin.ModelAdmin):
    list_display = ['order_by','title', 'slug', 'is_published']
    list_display_links = ('title', 'slug',)
    list_editable = ('order_by','is_published',)

    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Service, ServicesAdmin)
