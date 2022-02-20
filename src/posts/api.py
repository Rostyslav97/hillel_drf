from rest_framework.generics import ListAPIView,RetrieveUpdateDestroyAPIView, CreateAPIView
from posts.serializers import PostSerializer
from .models import Post
from posts.tasks import create_post

class PostListAPI(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostRetrieveUpdateDestroyAPI(RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_field = "id"

class PostCreateAPI(CreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def post(self, request, *args, **kwargs):
        create_post.delay() 
        return self.create(request, *args, **kwargs)
    

# class PostIDListAPI(ListCreateAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostIDSerializer

# class PostIDRetrieveAPI(RetrieveAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostIDSerializer
#     lookup_field = "id"





# class PostUpdateAPI(RetrieveUpdateAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
#     lookup_field = "id"

# class PostDestroyAPI(RetrieveDestroyAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
#     lookup_field = "id"
