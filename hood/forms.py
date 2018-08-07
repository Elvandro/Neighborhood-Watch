from django import forms
from .models import Neighbourhood, Profile, Business, Post, Comment

class CreateHoodForm(forms.ModelForm):
    class Meta:
        model = Neighbourhood
        fields = ['name','location','description','population']

class CreateBusinessForm(forms.ModelForm):
    class Meta:
        model = Business
        fields = ['name','description','email_address']

class CreatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title','body']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment',]               
