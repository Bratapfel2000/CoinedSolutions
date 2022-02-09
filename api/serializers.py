# api/serializers.py
from rest_framework import serializers
from coincollection.models import Product

class CoinProductSerializer(serializers.ModelSerializer):
	class Meta:
		model = Product
		##fields = ('LETTERS', 'coin_choice_field', 'coin_sort_field', 'title', 'description', 'year', 'date_found', 'category')
		fields = ('LETTERS')

