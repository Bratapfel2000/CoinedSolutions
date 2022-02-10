from rest_framework import generics
from blog.models import Post
from .serializers import PostSerializer
from coincollection.models import Product
from .serializers import CoinProductSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .permissions import IsAuthorOrReadOnly # new

class PostAPIView(generics.ListAPIView):
	queryset = Post.objects.all()
	serializer_class = PostSerializer
	permission_classes = (IsAuthorOrReadOnly,)

class CoinProductAPIView(generics.ListAPIView):
	queryset = Product.objects.all()
	serializer_class = CoinProductSerializer
	permission_classes = (IsAuthorOrReadOnly,)