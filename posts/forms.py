from django import forms
from .models import Post, Comment

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'select1_content','img1', 'select2_content', 'img2',)


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)