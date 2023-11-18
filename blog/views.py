from django.shortcuts import render
from .models import Post, Category, Hashtag


def blog(request):
    posts = Post.objects.all()
    latest_post = posts.latest('fecha')
    categories = Category.objects.all()
    hashtags = Hashtag.objects.all()
    return render(request, 'blog.html', {'user': request.user, 'posts': posts, 'latest_post': latest_post, 'categories': categories, 'hashtags': hashtags})
