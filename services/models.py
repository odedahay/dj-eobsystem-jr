from django.db import models
from datetime import datetime
from ckeditor.fields import RichTextField


class Service(models.Model):
    order_by = models.IntegerField(unique=True, blank=True, null=True)
    title = models.CharField(max_length=200)
    slug = models.CharField(max_length=200, unique=True)
    body = RichTextField(blank=True, null=True)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    created_date = models.DateTimeField(auto_now_add=True, null=True)
    is_published = models.BooleanField(default=True)

    class Meta:
        ordering = ('order_by',)
        verbose_name = 'Service'
        verbose_name_plural = 'Services'

    def __str__(self):
        return self.title