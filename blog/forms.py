from .models import Comment, Post
from django import forms

# comment form


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)

# Blog post form for editing on the front end


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'content', 'location', 'equiptment_featured', 'slug', 'featured_image', 'status')
