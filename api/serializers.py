# api/serializers.py
from rest_framework import serializers
from blog.models import Post
from coincollection.models import Product

class PostSerializer(serializers.ModelSerializer):
	class Meta:
		model = Post
		fields = ('title', 'content', 'date_posted', 'author')

class CoinProductSerializer(serializers.ModelSerializer):
	class Meta:
		model = Product
		fields = (
			'coin_choice_field', 
			'coin_sort_field', 
			'title', 
			'description',
			'image',
			'year', 
			'date_found', 
			'category')

