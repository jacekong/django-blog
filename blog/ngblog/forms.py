from django import forms
from django.forms import ModelForm,widgets
from .models import Post

class PostForm(ModelForm):
    class Meta:
        model = Post
        exclude = ['slug','user']
        widgets = {
            'image': forms.FileInput(attrs={'class':'image-input'}),
            'category': forms.Select(attrs={'class':'category'})
        }