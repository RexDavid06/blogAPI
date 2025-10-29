from django.shortcuts import render
from .serializers import PostSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .models import Post
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.shortcuts import get_object_or_404

# Create your views here.
class PostCreateView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(author=request.user) # attaching the author as the logged-in user
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class PostListView(APIView):
    permission_classes = [AllowAny]
    def get(self, request):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class PostDetailView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, slug):
        post = get_object_or_404(Post, slug=slug)
        serializer =PostSerializer(post)
        return Response(serializer.data, status=status.HTTP_200_OK)


class PostUpdateView(APIView):
    def put(self, request, slug):
        post = get_object_or_404(Post, slug=slug, author=request.user)
        serializer = PostSerializer(post, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PostDeleteView(APIView):
    def delete(self, request, slug):
        post = get_object_or_404(Post, slug=slug, author=request.user)
        post.delete()
        return Response({
            "message": "post deleted successfully"
        }, status=status.HTTP_204_NO_CONTENT)