from django.http import Http404

from django.shortcuts import render

from blog.models import Post

posts = Post.objects.all()

posts_dict = {post['id']: post for post in posts}


def index(request):
    return render(request, 'blog/index.html', {
        'posts': reversed(posts)})


def post_detail(request, post_id):
    post = posts_dict.get(post_id)
    if post is not None:
        return render(request, 'blog/detail.html', {'post': post})
    raise Http404(f'Post with id {post_id} not found')


def category_posts(request, category_slug):
    return render(request, 'blog/category.html', {
        'category_slug': category_slug})
