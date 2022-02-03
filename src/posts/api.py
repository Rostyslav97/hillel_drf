from django.http import JsonResponse
from rest_framework.generics import ListAPIView
from posts.serializers import PostSerializer 

from posts.services import handle_error, post_to_dict, NotAPostInstanceError
from .models import Post

# def posts(request):
#     posts = Post.objects.all()
#     try:
#         results = [post_to_dict(12) for post in posts]
#         return JsonResponse({"results": results})
#     except NotAPostInstanceError as error: 
#         return JsonResponse(status=400, data={"messages": error.args})


@handle_error
def posts(request):
    posts = Post.objects.all()
    results = [post_to_dict(12) for post in posts]
    return JsonResponse({"results": results})

class PostListAPI(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
