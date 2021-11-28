from django.shortcuts import render,redirect
# Create your views here.
from  blog.models import  Post
from django.http import HttpResponse
def createpost(request):
        if request.method == 'POST':
            if request.POST.get('title') and request.POST.get('content'):
                post=Post()
                Post.title= request.POST.get('title')
                Post.text= request.POST.get('content')
                Post.published_date=request.POST.get('pub_date')
                post.save()

                return render(request, 'blog/create_post.html')

        else:
                return render(request,'blog/create_post.html')

def show (request):
    querry=Post.objects.all()
    context={
        "post": querry
        }
    return render (request,"blog/post_list.html ",context)

def delete(request):
    pass
    # di voi js se de hon :))
