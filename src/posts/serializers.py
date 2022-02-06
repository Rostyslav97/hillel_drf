from rest_framework import serializers

from posts.models import Post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        # fields = "__all__"
        # fields = ("id", "title")
        exclude = ("id", "created_at", "updated_at")

class PostIDSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        exclude = ("created_at", "updated_at")