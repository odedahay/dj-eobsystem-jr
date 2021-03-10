from django.db import models
from datetime import datetime
from ckeditor.fields import RichTextField

# Create your models here.
class Page(models.Model):
    title = models.CharField(max_length=200, unique=True, null=True)
    slug = models.SlugField(max_length=200, unique=True, null=True)
    page_intro = RichTextField(blank=True, null=True)
    body = RichTextField(blank=True, null=True)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    created_date = models.DateTimeField(auto_now_add=True, null=True)
    is_published = models.BooleanField(default=True)

    class Meta:
        ordering =('title',)
        verbose_name = 'page'
        verbose_name_plural = 'pages'

    def __str__(self):
        return self.title
