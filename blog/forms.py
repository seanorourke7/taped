from .models import Comment, Post
from django import forms


class CommentForm(forms.ModelForm):
    # comment form
    class Meta:
        model = Comment
        fields = ('body',)


class PostForm(forms.ModelForm):
    # Blog post form for editing on the front end
    class Meta:
        model = Post
        fields = ('title', 'content', 'location', 'equiptment_featured', 'slug', 'featured_image', 'status')
