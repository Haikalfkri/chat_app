from django.shortcuts import render

# Create your views here.
def UserPost(request):
    return render(request, "app/user/post.html")