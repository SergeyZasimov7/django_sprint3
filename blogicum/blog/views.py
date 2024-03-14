from django.http import Http404
from django.utils import timezone

from django.shortcuts import render, get_object_or_404

from .models import Post, Category


def get_published_posts():
    return Post.objects.filter(
        pub_date__lte=timezone.now(),
        is_published=True,
        category__is_published=True
    )


def index(request):
    posts = posts = get_published_posts()[:5]
    return render(request, 'blog/index.html', {'posts': posts})


def post_detail(request, post_id):
    post = get_object_or_404(get_published_posts(), id=post_id)
    return render(request, 'blog/detail.html', {'post': post})


def category_posts(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    if not category.is_published:
        raise Http404(f'Category with slug {category_slug} is not published')
    posts_in_category = get_published_posts().filter(category=category)
    return render(request, 'blog/category.html', {'category': category,
                                                  'posts': posts_in_category})
