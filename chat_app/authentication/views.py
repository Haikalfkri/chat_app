from django.shortcuts import render, redirect
from authentication.forms import UserRegisterForm
from django.contrib import messages
from django.contrib.auth.models import Group
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


# Create your views here.
def UserRegister(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        
        if form.is_valid():
            user = form.save()
    
            group = Group.objects.get(name='user')
            user.groups.add(group)
            
            messages.success(request, "Register Successfully!")
            return redirect('login')   
    else:
        form = UserRegisterForm()

    
    return render(request, "authentication/register.html", {'form': form})


def UserLogin(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect_check(request)
        else:
            messages.error(request, "Username OR password is incorrect")    
                
    return render(request, "authentication/login.html")


def UserLogout(request):
    logout(request)
    messages.success(request, "Logout Successfully")
    return redirect('login')


@login_required(login_url='login')
def redirect_check(request):
    user = request.user
    
    if user.role == "user" and user.groups.filter(name='user').exists():
        return redirect("post")
    else:
        messages.error(request, "You dont have any permission")
        return redirect('post')