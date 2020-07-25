from django.shortcuts import render,redirect, HttpResponse, get_object_or_404
from .models import *
from django.contrib.auth.models import User
from .forms import *
from django.contrib.auth.decorators import login_required, user_passes_test
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger



def add_blog(request):
    
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post=form.save(commit=False)
            post.author= request.user
            post.save()
            return redirect("/blog")
    else:
        form=PostForm()
    return render(request, 'blog/blog_post.html', {'form':form})
           

def view_post(request, slug):
    post=get_object_or_404(Post, slug=slug)
    return render(request, "blog/post_detail.html", {'post':post})

def show(request):
    post1= Post.objects.all().order_by('-created_on')
    page = request.GET.get('page', 1)

    paginator = Paginator(post1, 5)
    try:
        post2 = paginator.page(page)
    except PageNotAnInteger:
        post2 = paginator.page(1)
    except EmptyPage:
        post2 = paginator.page(paginator.num_pages)
    return render(request, "blog/index.html", {'post1':post1, 'post2':post2})


