from django import forms
from .models import Post, Comments

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