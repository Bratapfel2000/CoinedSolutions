# api/views.py
from rest_framework import generics
from coincollection.models import Product
from .serializers import CoinProductSerializer


class CoinProductAPIView(generics.ListAPIView):
	queryset = Product.objects.all()
	serializer_class = CoinProductSerializer