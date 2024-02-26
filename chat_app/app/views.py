from django.shortcuts import render, redirect
from .models import Post, Comments
from .forms import PostForm, CommentForm
from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.http import JsonResponse

from django.contrib.auth.decorators import login_required

# Create your views here.

# posts
@login_required(login_url='login')
def UserPost(request):
    post = Post.objects.all().order_by('-created')
    logged_user = request.user
    if request.method == "POST":
        form = PostForm(request.POST)
        
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.user = request.user
            new_post.save()
            return redirect('post')
    else:
        form = PostForm()
    
    context = {
        'posts': post,
        'form': form,
        'logged_user': logged_user,
    }
    return render(request, "app/user/post.html", context)


@login_required(login_url='login')
def deletePost(request, id):
    post = Post.objects.get(id=id)  
    post.delete()
    
    return redirect('post')  


@login_required(login_url='login')
def LikePost(request):
    if request.method == "POST":
        post_id = request.POST.get('post_id')
        post = get_object_or_404(Post, id=post_id)
        
        if post.liked_by.filter(id=request.user.id).exists():
            post.liked_by.remove(request.user)
            post.save()
        else:
            post.liked_by.add(request.user)
            post.save()
            
        
        return redirect('post')
    else:
        return JsonResponse({'error': 'Invalid request method'})
    
    
@login_required(login_url='login')
def PostComments(request, id):
    posts = Post.objects.get(id=id)
    logged_user = request.user

    if request.method == "POST":
        form = CommentForm(request.POST)
        
        if form.is_valid():
            new_comment = form.save(commit=False)
            post_id = request.POST.get('post_id')
            post = get_object_or_404(Post, id=post_id)
            new_comment.post = post
            new_comment.posted_by = logged_user
            new_comment.save()
    else:
        form = CommentForm()
    
    context = {
        'post': posts,
        'form': form,
        'logged_user': logged_user,
    }
    
    return render(request, "app/user/comments.html", context)