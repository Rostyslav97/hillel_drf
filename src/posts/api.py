from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, RetrieveUpdateAPIView, RetrieveDestroyAPIView
from posts.serializers import PostSerializer, PostIDSerializer

from .models import Post

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