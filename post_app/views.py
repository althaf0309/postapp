from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.generics import CreateAPIView, ListAPIView
from .models import Post, Like
from .serializers import UserSignupSerializer, PostSerializer
from rest_framework.parsers import MultiPartParser, FormParser

# Render Pages
def signup_page(request):
    return render(request, 'signup.html')

def login_page(request):
    return render(request, 'login.html')

def posts_page(request):
    return render(request, 'posts.html')

# API for User Signup
class UserSignupView(CreateAPIView):
    serializer_class = UserSignupSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

# API for Creating Posts
class PostCreateView(CreateAPIView):
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]
    parser_classes = (MultiPartParser, FormParser)  # Ensure support for file uploads

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

# API for Listing Posts
class PostListView(ListAPIView):
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Post.objects.filter(published=True)  # Display all published posts


# Like/Unlike Post API
class LikePostView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, post_id):
        try:
            post = Post.objects.get(id=post_id)
            like, created = Like.objects.get_or_create(user=request.user, post=post)
            if not created:
                like.delete()
                return Response({"message": "Post unliked"}, status=status.HTTP_200_OK)
            return Response({"message": "Post liked"}, status=status.HTTP_201_CREATED)
        except Post.DoesNotExist:
            return Response({"error": "Post not found"}, status=status.HTTP_404_NOT_FOUND)
