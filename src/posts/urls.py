from django.urls import path

from .api import PostListAPI, PostRetrieveUpdateDestroyAPI, PostCreateAPI

app_name = "posts"

urlpatterns = [
    path("", PostListAPI.as_view(), name="list"),
    path("<int:id>/", PostRetrieveUpdateDestroyAPI.as_view(), name="retrieve"),
    path("create/", PostCreateAPI.as_view(), name="create"),
    # path("id/", PostIDListAPI.as_view(), name="posts_list"),
    # path("id/<int:id>/", PostIDRetrieveAPI.as_view(), name="post_detailid"),
]