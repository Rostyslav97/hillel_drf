from django.http import JsonResponse
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, RetrieveUpdateAPIView, RetrieveDestroyAPIView
from posts.serializers import PostSerializer, PostIDSerializer

from .models import Post

from posts.services import handle_error, post_to_dict, NotAPostInstanceError

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

class PostIDListAPI(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostIDSerializer

class PostRetrieveAPI(RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_field = "id"

class PostIDRetrieveAPI(RetrieveAPIView):
    queryset = Post.objects.all()
    serializer_class = PostIDSerializer
    lookup_field = "id"

class PostCreateAPI(CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostUpdateAPI(RetrieveUpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_field = "id"

class PostDestroyAPI(RetrieveDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_field = "id"