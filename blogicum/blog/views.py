from django.shortcuts import get_object_or_404, render
from django.utils import timezone

from .models import Category, Post


def get_published_posts(posts):
    return posts.filter(
        pub_date__lte=timezone.now(),
        is_published=True,
        category__is_published=True
    )


def index(request):
    return render(request, 'blog/index.html', {'posts': get_published_posts(
        Post.objects)[:5]}
    )


def post_detail(request, post_id):
    return render(request, 'blog/detail.html', {'post': get_object_or_404(
        get_published_posts(Post.objects), id=post_id)}
    )


def category_posts(request, category_slug):
    category = get_object_or_404(
        Category,
        slug=category_slug,
        is_published=True
    )
    return render(request, 'blog/category.html', {
        'category': category,
        'posts': get_published_posts(category.posts)
    })
