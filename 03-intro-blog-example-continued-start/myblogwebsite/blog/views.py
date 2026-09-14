
from django.shortcuts import render


# this is what will handle the request
def post_list(request):
    # note the following will render the template created.
    return render(request, 'blog/posts_list.html')
