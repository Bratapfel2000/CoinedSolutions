from rest_framework import generics
from blog.models import Post
from .serializers import PostSerializer
from coincollection.models import Product
from .serializers import CoinProductSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class PostAPIView(generics.ListAPIView):
	permission_classes = (IsAuthenticatedOrReadOnly,)
	queryset = Post.objects.all()
	serializer_class = PostSerializer
	print("")
	print("")	
	print("")

	print(">>>>>", serializer.errors)
	print("")
	print("")
	print("")

class CoinProductAPIView(generics.ListAPIView):
	permission_classes = (IsAuthenticatedOrReadOnly,)
	queryset = Product.objects.all()
	serializer_class = CoinProductSerializer
	print("")
	print("")	
	print("")

	print(">>>>>", serializer.errors)
	print("")
	print("")
	print("")