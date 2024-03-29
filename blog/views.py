from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import Post
from .forms import CommentForm, PostForm
from . import forms
from django.contrib import messages
from django.views.generic import UpdateView
from django.urls import reverse_lazy


class PostList(generic.ListView):
    # views for the blog overview page
    model = Post
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 3


class PostDetail(View):
    # view to show the blogpost details
    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by("-created_on")
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": False,
                "liked": liked,
                "comment_form": CommentForm()
            },
        )

    def post(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by("-created_on")
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        comment_form = CommentForm(data=request.POST)

        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
            messages.info(request, f'New comment has been submitted for approval')
        else:
            comment_form = CommentForm()

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": True,
                "liked": liked,
                "comment_form": CommentForm()
            },
        )


class PostLike(View):
    # views for liking posts
    def post(self, request, slug, *args, **kwargs):
        post = get_object_or_404(Post, slug=slug)
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        return HttpResponseRedirect(reverse('post_detail', args=[slug]))


class PostCreate(View):
    # view for creating a new post by the admin/superuser
    def get(self, request):
        form = forms.PostForm()
        return render(request, "postcreate.html", {'form': form})

    def post(self, request):
        form = forms.PostForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            if instance.status == 1:
                messages.info(request, f'Created and published new post')
            else:
                messages.info(request, f'New post created as draft only. ')
            return HttpResponseRedirect(reverse('home'))
        return render(request, 'postcreate.html', {'form': form})


class Delete(View):
    # view for deleting posts by the admin/superuser
    def delete(self, request, slug):
        template_name = "delete_post.html"

class DeletePost(View):
    def get(self, request, slug):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        post.delete()
        messages.info(request, f'Post has been Deleted')
        return HttpResponseRedirect(reverse('home'))


class EditPost(UpdateView):
    # view for editing posts by the admin/superuser
    model = Post
    template_name = 'edit_post.html'
    fields = ['title', 'content', 'location', 'equiptment_featured', 'featured_image', 'status']
    success_url = reverse_lazy('home')
