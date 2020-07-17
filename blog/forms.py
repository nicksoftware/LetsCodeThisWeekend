from django import forms

from .models import Post, Comment
class CommentForm(forms.ModelForm):
   
    text = forms.CharField(label='Comment',widget=forms.Textarea(attrs={'placholder':"Enter your Comment","class":"form-control"}))
    class Meta:
        model = Comment
        fields =('author','text')