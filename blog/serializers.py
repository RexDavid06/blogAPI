from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['title', 'slug', 'content', 'image', 'author', 'created_at', 'updated_at']
        extra_kwargs = {"author": {"read_only": True}}