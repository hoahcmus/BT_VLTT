from django.shortcuts import render
# Create your views here.

from blog.models import Post


def post_list_view(request):
    """ A view that display a list of published posts."""
    posts = Post.objects.all()

    context = {
        "posts": posts
    }
    return render(request, "blog/post_list.html", context)
