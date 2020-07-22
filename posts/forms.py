from django import forms

from posts.models import Author


class PostForm(forms.Form):
    title = forms.CharField()
    content = forms.CharField(widget=forms.Textarea)
    author = forms.ChoiceField(
        choices=((a.id, a.nick) for a in Author.objects.all())
    )


class AuthorForm(forms.Form):
    nick = forms.CharField()
    email = forms.EmailField()
