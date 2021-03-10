from django.contrib import admin
from .models import Page

# Register your models here.
class PageAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug']
    list_display_links = ('title',)

    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Page, PageAdmin)