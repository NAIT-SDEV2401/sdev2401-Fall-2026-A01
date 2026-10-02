
from django.shortcuts import render, get_object_or_404

# give us access to the Post class from models.py
from .models import Post

# this is what will handle the request
def post_list(request):
    p = Post.objects.all()
    # note the following will render the template created.
    return render(request, 'blog/posts_list.html', {'the_posts': p})

def post_detail(request, primaryKey):
    # get the post with the given primary key (pk) from the database
    post = get_object_or_404(Post, pk=primaryKey)
    return render(request, 'blog/post_detail.html', {'post': post})