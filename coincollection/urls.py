from django.urls import path
from . import views

urlpatterns = [
    #path('coinhome/', views.coinhome, name='blog-home'),
    path('', views.coinhome, name='coin-home'),
    path('country/<int:id>/<slug:slug>', views.country, name='country'),
    path('category/<slug:slug>/<int:id>', views.coin_detail, name='coin-detail'),

]