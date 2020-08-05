from django import forms

from posts.models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = "__all__"
        fields = ["title", "content", "author", "image", "tags"]


class AuthorForm(forms.Form):
    nick = forms.CharField()
    email = forms.EmailField()
