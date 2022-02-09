from django.urls import path
from .views import CoinProductAPIView

urlpatterns = [
	path('', CoinProductAPIView.as_view()),
]