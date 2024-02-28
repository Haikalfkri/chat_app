from django import forms
from .models import Post, Comments, UserProfile

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
    user = forms.CharField(widget=forms.TextInput(attrs={
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
        fields = ('user', 'bio', 'image')
    
    def clean_user(self):
        return self.cleaned_data['user']
    
    def clean_image(self):
        image = self.cleaned_data.get('image', False)
        if image:
            if image._size > 10 * 1024 * 1024: #10 mb
                raise forms.ValidationError("Image file size should not exceed 10 MB.")
            return image