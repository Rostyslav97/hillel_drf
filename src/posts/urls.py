from django.urls import path

from .api import PostListAPI, PostRetrieveAPI, PostCreateAPI, PostUpdateAPI, PostDestroyAPI, PostIDListAPI, PostIDRetrieveAPI

app_name = "posts"

urlpatterns = [
    # path("",posts, name="list"),
    path("list/", PostListAPI.as_view(), name="posts_list"),
    path("list_id/", PostIDListAPI.as_view(), name="posts_list"),
    path("list/<int:id>/", PostRetrieveAPI.as_view(), name="post_detail"),
    path("list_id/<int:id>/", PostIDRetrieveAPI.as_view(), name="post_detailid"),
    path("create/", PostCreateAPI.as_view(), name="create"),
    path("update/<int:id>/", PostUpdateAPI.as_view(), name="update"),
    path("delete/<int:id>", PostDestroyAPI.as_view(), name="delete")
]  