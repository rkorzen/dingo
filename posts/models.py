from django.db import models


# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    author = models.ForeignKey('posts.Author', on_delete=models.CASCADE)

    def __str__(self):
        return f"<Post: Author:{self.author}, Title:{self.title}>"


class Author(models.Model):
    nick = models.CharField(max_length=50, unique=True)
    email = models.EmailField()

    def __str__(self):
        return f"<Author: {self.nick}>"
