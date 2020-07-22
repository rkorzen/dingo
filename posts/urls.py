from django.urls import path

from posts.views import post_list, post_details, authors_list, author_details

app_name = "posts"

urlpatterns = [
    path('', post_list, name="list"),
    path('<int:id>', post_details, name="details"),
    path('authors', authors_list, name="authors"),
    path('authors/<int:id>', author_details, name="author")
]
