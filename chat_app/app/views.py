from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .models import Post, UserProfile
from authentication.models import CustomUser
from .forms import PostForm, CommentForm, ProfileForm, PasswordChangingForm
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.utils import timezone
from django.db.models import Q
from django.contrib.auth.decorators import login_required

from django.contrib.auth.views import PasswordChangeView

# Create your views here.

# change password
class PasswordsChangeView(PasswordChangeView):
    form_class = PasswordChangingForm
    success_url = reverse_lazy('change-password')
    success_message = "Password Succesfully Change"


# posts
@login_required(login_url='login')
def UserPost(request):
    post = Post.objects.all().order_by('-created')
    users = CustomUser.objects.all()
    logged_user = request.user
    if request.method == "POST":
        form = PostForm(request.POST)
        
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.user = request.user
            new_post.created = timezone.now()
            new_post.save()
            return redirect('post')
    else:
        form = PostForm()
    
    context = {
        'posts': post,
        'form': form,
        'logged_user': logged_user,
        'users': users,
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

        # check if the post has never been like before
        
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
        
        form = CommentForm()
    else:
        form = CommentForm()
    
    context = {
        'post': posts,
        'form': form,
        'logged_user': logged_user,
    }
    
    return render(request, "app/user/comments.html", context)



# profile
def Profile(request):
    profile = UserProfile.objects.get(user=request.user)
    
    if request.method == "POST":
        form = ProfileForm(request.POST, instance=profile, files=request.FILES)
        
        if form.is_valid():
            # update the fields in user profile and custom user 
            profile.bio = form.cleaned_data['bio']
            profile.image = form.cleaned_data['image']
            profile.save()
            
            user = request.user
            user.username = form.cleaned_data['username']
            user.save()
            
            form.save()
            
            return redirect("user-profile")
    else:
        form = ProfileForm(initial={
            'username': request.user.username,
            'bio': profile.bio,
            'image': profile.image
        })
        
    context = {
        'form': form,
    }

    return render(request, "app/user/profile.html", context)


def changePassword(request):
    return render(request, "app/user/change_password.html")


def Members(request):
    user = CustomUser.objects.all().order_by("-date_joined")
    
    search_user = request.GET.get('search')
    
    if search_user:
        user = user.filter(Q(username__icontains=search_user))
            
    
    context = {
        'users': user
    }
    
    return render(request, "app/user/members.html", context)