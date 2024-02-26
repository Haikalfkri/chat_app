from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm
from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.db.models import F
from django.http import JsonResponse

# Create your views here.

# posts
def UserPost(request):
    post = Post.objects.all()
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


def deletePost(request, id):
    post = Post.objects.get(id=id)  
    post.delete()
    
    return redirect('post')  


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
    
    
def PostComments(request):
    pass