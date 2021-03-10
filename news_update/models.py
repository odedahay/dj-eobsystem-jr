from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from django.urls import reverse
from taggit.managers import TaggableManager

class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset().filter(status='published')

class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )

    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    author = models.ForeignKey(User, on_delete=models.PROTECT, related_name='blog_post')
    body = RichTextField(blank=True, null=True)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10,
                              choices=STATUS_CHOICES,
                              default='draft')
    objects = models.Manager()
    published = PublishedManager() #custom manager
    tags = TaggableManager()

    def get_absolute_url(self):
        return reverse('news_update:news-update-detail', args=[self.slug])

    class Meta:
        ordering = ('-publish',)
        verbose_name = 'News and Update'
        verbose_name_plural = 'News and Update'
    
    def __str__(self):
        return self.title

