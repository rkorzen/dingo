from django.contrib import messages
from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView

from posts.forms import PostForm, AuthorForm
from posts.models import Post, Author


def posts_list(request):
    posts = Post.objects.all()
    form = PostForm()
    if request.method == "POST":
        form = PostForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            messages.add_message(
                request,
                messages.SUCCESS,
                "Dodano nowy Post!!"
            )
            form = PostForm()
        else:
            messages.add_message(
                request,
                messages.ERROR,
                form.errors["__all__"]
            )
    return render(
        request=request,
        template_name="posts/list.html",
        context={"posts": posts, "form": form, 'active': 'posts'}
    )


def post_details(request, id):
    post = Post.objects.get(pk=id)
    return render(
        request=request,
        template_name="posts/details.html",
        context={"post": post, 'active': "posts"}
    )


def authors_list(request):
    authors = Author.objects.all()
    form = AuthorForm()
    if request.method == "POST":
        form = AuthorForm(data=request.POST)
        if form.is_valid():
            Author.objects.create(**form.cleaned_data)
            messages.add_message(
                request,
                messages.SUCCESS,
                "Dodano Autora!!"
            )
        else:
            messages.add_message(
                request,
                messages.ERROR,
                form.errors["__all__"]
            )
    return render(
        request=request,
        template_name="posts/authors.html",
        context={'authors': authors, 'form': form}
    )


def author_details(request, id):
    author = Author.objects.get(pk=id)
    return render(
        request=request,
        template_name="posts/author.html",
        context={'author': author}
    )


class PostsList(ListView):
    model = Post
    template_name = "posts/list.html"
    form_class = PostForm
    context_object_name = "posts"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = PostForm()
        return context


