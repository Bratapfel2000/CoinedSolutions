from django.urls import path
from .views import PostAPIView
from .views import CoinProductAPIView

urlpatterns = [
	path('blogs/', PostAPIView.as_view()),
	path('coins/', CoinProductAPIView.as_view()),
]