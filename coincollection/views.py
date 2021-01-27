from django.shortcuts import render
from django.http import HttpResponse
from .models import Category, Product
from .filters import ProductFilter

#def coinhome(request):
#    return render(request, 'coincollection/home.html', {'title': 'coinhome'})


def coinhome(request):
	category = Category.objects.all()
	all_products = Product.objects.all()
	page = "somu-overview"
	order = Product.objects.all()
	myFilter = ProductFilter(request.GET, queryset=order)
	order = myFilter.qs
	context={'category':category, 'all_products':all_products, 'order':order, 'myFilter':myFilter}
	return render(request, 'coincollection/home.html',context)