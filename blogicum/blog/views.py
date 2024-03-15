from django.shortcuts import get_object_or_404, render
from django.utils import timezone

from .models import Category, Post


def get_published_posts(queryset):
    return queryset.filter(
        pub_date__lte=timezone.now(),
        is_published=True,
        category__is_published=True
    )


def index(request):
    posts = get_published_posts(Post.objects)[:5]
    return render(request, 'blog/index.html', {'posts': posts})


def post_detail(request, post_id):
    return render(request, 'blog/detail.html', {'post': get_object_or_404(
        get_published_posts(Post.objects), id=post_id)}
    )


def category_posts(request, category_slug):
    category = get_object_or_404(
        Category.objects.filter(is_published=True),
        slug=category_slug
    )
    posts_in_category = get_published_posts(category.posts)
    return render(request, 'blog/category.html', {
        'category': category,
        'posts': posts_in_category
    })
