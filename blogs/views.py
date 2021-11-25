from django.shortcuts import render, redirect

from . models import BlogPost

from .forms import BlogPostForm


def index(request):
    blogs = BlogPost.objects.all()
    context = {'blogs': blogs}
    return render(request, 'blogs/index.html', context)


def new_post(request):
    if request.method != 'POST':
        form = BlogPostForm()
    else:
        form = BlogPostForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('blogs:index')
    context = {'form': form}
    return render(request, 'blogs/new_post.html', context)


def edit_post(request, post_id):
    post = BlogPost.objects.get(id=post_id)
    if request.method != 'POST':
        form = BlogPostForm(instance=post)
    else:
        form = BlogPostForm(data=request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('blogs:index')
    context = {'form': form, 'post': post}
    return render(request, 'blogs/edit_post.html', context)
