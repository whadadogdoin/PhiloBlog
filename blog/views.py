from django.shortcuts import render, get_object_or_404
from  django.utils import timezone
from  .models import Post
from .forms import Postform
from django.shortcuts import redirect

def post_list(request):
    posts=Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html',{'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def post_new(request):
    if request.method == "POST":
        form = Postform(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = Postform()
    return render(request, 'blog/post_edit.html', {'form': form})

def post_edit(request,pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = Postform(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = Postform(request.POST, instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})

def drafts_list(request):
    posts=Post.objects.filter(published_date__isnull=True).order_by('created_date')
    return render(request,'blog/drafts_list.html',{'posts':posts})

def post_publish(request,pk):
    post = get_object_or_404(Post, pk=pk)
    post.publish()
    return redirect('post_detail', pk=pk)

def post_delete(request,pk):
    post=get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('post_list')