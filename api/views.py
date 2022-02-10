from rest_framework import generics
from blog.models import Post
from .serializers import PostSerializer
from coincollection.models import Product
from .serializers import CoinProductSerializer
from .permissions import IsAuthorOrReadOnly

class PostAPIView(generics.ListAPIView):
	permission_classes = (IsAuthorOrReadOnly,)
	queryset = Post.objects.all()
	serializer_class = PostSerializer

class CoinProductAPIView(generics.ListAPIView):
	permission_classes = (IsAuthorOrReadOnly,)
	queryset = Product.objects.all()
	serializer_class = CoinProductSerializer