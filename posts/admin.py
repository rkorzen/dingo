from django.contrib import admin
from posts.models import Post, Author

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["title", "created"]
    search_fields = ["title", "content"]

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    pass