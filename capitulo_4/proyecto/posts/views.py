from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from posts.models import Post

# Create your views here.

@login_required
def list_posts(request):
    posts = list(Post.objects.all())
    return render(request, 'posts/feed.html', {'posts': posts})