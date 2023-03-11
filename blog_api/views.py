from rest_framework import generics
from blog.models import Post
from .serializers import PostSerializer

# Listing and creating 
class PostList(generics.ListCreateAPIView):
    queryset = Post.postobjects.all()
    serializer_class = PostSerializer

# Retrieving and destroying
class PostDetail(generics.RetrieveDestroyAPIView):
    queryset = Post.postobjects.all()
    serializer_class = PostSerializer