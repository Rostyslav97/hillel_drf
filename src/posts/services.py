from django.http import JsonResponse
from .models import Post

class NotAPostInstanceError(Exception):
    def __init__(self, *args, **kwargs):
        return super().__init__("You can not create a dictionary from the instance of a class that is not a Post")


def handle_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except NotAPostInstanceError as error:
            return JsonResponse(status=400, data={"messages": error.args})
    return inner


def post_to_dict(post: Post) -> dict:
    if not isinstance(post, Post):
        raise NotAPostInstanceError
    return {"id": post.id, "title": post.title, "content": post.content, "status": post.status} 