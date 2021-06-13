from django import forms
from .models import Post, Comment
# post -  forms.Form


class PostForm(forms.Form):
    title = forms.CharField(max_length=100)
    content = forms.TextField()


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['nick', 'email', 'title', 'content', 'post']