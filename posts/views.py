from django.shortcuts import render

# Create your views here.
from posts.models import Post, Author


def post_list(request):
    posts = Post.objects.all()
    return render(
        request=request,
        template_name="posts/list.html",
        context = {"posts": posts}
    )

def post_details(request, id):
    post = Post.objects.get(pk=id)
    return render(
        request=request,
        template_name="posts/details.html",
        context = {"post": post}
    )


def authors_list(request):
    authors = Author.objects.all()
    return render(
        request=request,
        template_name="posts/authors.html",
        context = {'authors': authors}
    )

def author_details(request, id):
    author = Author.objects.get(pk=id)
    return render(
        request=request,
        template_name="posts/author.html",
        context = {'author': author}
    )