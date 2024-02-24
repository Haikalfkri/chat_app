from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    body = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control',
        'placeholder': 'Write Something',
        'rows': 4,
    }))
    
    class Meta:
        model = Post
        fields =  ("body", )