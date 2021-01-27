import django_filters

from .models import *

class ProductFilter(django_filters.FilterSet):
	class Meta:
		model = Product
		exclude = ['image']
		fields = '__all__'
		#fields =  ['coin_choice_field']