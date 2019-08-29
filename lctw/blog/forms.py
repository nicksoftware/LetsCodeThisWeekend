from django import forms
from .models import Post, Comment
class CommentForm(forms.ModelForm):
    author = forms.CharField(label='Your name',widget=forms.TextInput(attrs={'class':"form-control" }))    
    text = forms.CharField(label='Comment',widget=forms.Textarea(attrs={'placholder':"Enter your Comment","class":"form-control"}))
    class Meta:
        model = Comment
        fields =('author','text')