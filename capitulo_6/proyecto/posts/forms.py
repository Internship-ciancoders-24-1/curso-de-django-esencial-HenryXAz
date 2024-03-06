from django import forms

from posts.models import  Post

class PostForm(forms.ModelForm):
    """Post model form"""
    class Meta:
        model=Post
        fields=('user', 'profile', 'title', 'photo')