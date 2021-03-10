from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Post
from taggit.models import Tag
from django.db.models import Count
from systems_products.models import SystemsProduct


def post_list(request, tag_slug=None):
    products = SystemsProduct.objects.order_by('order_by').filter(is_published=True)
    object_list = Post.published.all()

    tag = None

    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        object_list = object_list.filter(tags__in=[tag])

    paginator = Paginator(object_list, 3)
    page = request.GET.get('page')

    try:
        posts = paginator.page(page)

    except PageNotAnInteger:
        # If page is not an integer deliver the first page
        posts = paginator.page(1)

    except EmptyPage:
        # If page is out of range deliver last page of results
        posts = paginator.page(paginator.num_pages)

    context = {
        'page': page,
        'posts': posts,
        'tag': tag,
        'products':products,
    }
    return render(request,'news_update/news_update_list.html', context)


def post_detail(request, slug_p):
    products = SystemsProduct.objects.order_by('order_by').filter(is_published=True)
    post = get_object_or_404(Post, slug=slug_p, status='published')

    # List of similar posts
    post_tags_ids = post.tags.values_list('id', flat=True)
    similar_posts = Post.published.filter(tags__in=post_tags_ids).exclude(id=post.id)
    similar_posts = similar_posts.annotate(same_tags=Count('tags')).order_by('-same_tags', 'publish')[:3]
    
    context = {
        'post': post,
        'similar_posts': similar_posts,
        'products':products,
    }

    return render(request, 'news_update/news_update_details.html', context)