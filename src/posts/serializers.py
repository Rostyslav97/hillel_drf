from rest_framework import serializers

from posts.models import Post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        exclude = ("id", "created_at", "updated_at")
        # fields = "__all__"
        # fields = ("id", "title")

# class PostIDSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Post
#         exclude = ("created_at", "updated_at")