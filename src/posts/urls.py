from django.urls import path

from .api import posts, PostListAPI

app_name = "posts"

urlpatterns = [
    path("",posts, name="list"),
    path("list/", PostListAPI.as_view(), name="posts_list"),
]  