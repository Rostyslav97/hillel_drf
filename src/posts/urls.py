from django.urls import path
from .api import posts

app_name = "posts"

urlpatterns = [
    path("",posts, name="list"),
]  