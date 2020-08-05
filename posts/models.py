from django.db import models


# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    author = models.ForeignKey('posts.Author', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='photos/%Y/%m/%d', null=True, blank=True)
    tags = models.ManyToManyField("posts.Tag", related_name="posts")
    def __str__(self):
        return f"<Post: Author:{self.author}, Title:{self.title}>"


class Author(models.Model):
    nick = models.CharField(max_length=50, unique=True)
    email = models.EmailField()

    def __str__(self):
        return f"<Author: {self.nick}>"


class Tag(models.Model):
    word = models.CharField(max_length=50, unique=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.word