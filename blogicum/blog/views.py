from django.http import Http404

from django.shortcuts import render, get_object_or_404

from django.utils import timezone

from .models import Post, Category


def index(request):
    current_time = timezone.now()
    posts = Post.objects.filter(
        pub_date__lte=current_time,
        is_published=True,
        category__is_published=True
    ).order_by('-pub_date')[:5]
    return render(request, 'blog/index.html', {'posts': posts})


def post_detail(request, post_id):
    current_time = timezone.now()
    try:
        post = Post.objects.get(id=post_id)
        if (post.pub_date > current_time or
            not post.is_published or
            not post.category.is_published):
            raise Http404(f'Post with id {post_id} is not available')
    except Post.DoesNotExist:
        raise Http404(f'Post with id {post_id} not found')
    return render(request, 'blog/detail.html', {'post': post})


def category_posts(request, category_slug):
    current_time = timezone.now()
    category = get_object_or_404(Category, slug=category_slug)
    if not category.is_published:
        raise Http404(f'Category with slug {category_slug} is not published')
    posts_in_category = Post.objects.filter(
        category=category,
        pub_date__lte=current_time,
        is_published=True
    )
    return render(request, 'blog/category.html', {'category': category,
                                                  'posts': posts_in_category})
