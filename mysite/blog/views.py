from django.shortcuts import render, get_object_or_404
from .forms import PostForm, CommentForm
from .models import Post


# Create your views here.



def post_share(request, post_id):
    post = get_object_or_404(Post, pk=post_id, status='published')
    # if request.method == 'POST':
    return render(request)