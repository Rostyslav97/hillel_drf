from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from posts.serializers import PostSerializer

from .models import Post

class PostListCreateAPI(ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostRetrieveUpdateDestroyAPI(RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_field = "id"

# class PostIDListAPI(ListCreateAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostIDSerializer

# class PostIDRetrieveAPI(RetrieveAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostIDSerializer
#     lookup_field = "id"



# class PostCreateAPI(CreateAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer

# class PostUpdateAPI(RetrieveUpdateAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
#     lookup_field = "id"

# class PostDestroyAPI(RetrieveDestroyAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
#     lookup_field = "id"
