from django.urls import path
from . import views

urlpatterns = [
    #path('coinhome/', views.coinhome, name='blog-home'),
    path('', views.coinhome, name='coin-home'),

]