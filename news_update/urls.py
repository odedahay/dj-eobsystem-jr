from django.urls import path

from . import views

app_name = 'news_update'

urlpatterns = [
    path('', views.post_list, name='news-update'), 
    path('tag/<slug:tag_slug>', views.post_list, name='post_list_by_tag'), 
    path('<slug:slug_p>/', views.post_detail, name='news-update-detail'), 
]