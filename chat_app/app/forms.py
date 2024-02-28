from django import forms
from .models import Post, Comments, UserProfile
from django.contrib.auth.forms import PasswordChangeForm
from django.conf import settings

class PostForm(forms.ModelForm):
    body = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control',
        'placeholder': 'Write Something',
        'rows': 4,
    }))
    
    class Meta:
        model = Post
        fields =  ("body", )
        
    
class CommentForm(forms.ModelForm):
    body = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Add a comment',
    }))
    
    class Meta:
        model = Comments
        fields = ("body", )
        
        

class ProfileForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'id': 'username',
        'placeholder': 'Username'
    }))
    bio = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control',
        'id': 'bio',
        'rows': '3',
        'placeholder': 'type something...'
    }))
    class Meta:
        model = UserProfile
        fields = ('username', 'bio', 'image')


class PasswordChangingForm(PasswordChangeForm):
    old_password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'type': 'password',
    }))
    new_password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'type': 'password',
    }))
    new_password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'type': 'password',
    }))
    class Meta:
        model = settings.AUTH_USER_MODEL
        fields = ('old_password', 'new_password1', 'new_password2')