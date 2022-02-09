from rest_framework import generics
from blog.models import Post
from .serializers import PostSerializer
from coincollection.models import Product
from .serializers import CoinProductSerializer

class PostAPIView(generics.ListAPIView):
	queryset = Post.objects.all()
	serializer_class = PostSerializer

class CoinProductAPIView(generics.ListAPIView):
	queryset = Product.objects.all()
	serializer_class = CoinProductSerializer