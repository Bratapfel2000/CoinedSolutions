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

def country(request,id,slug):
    products = Product.objects.filter(category_id=id) 
    catdata = Category.objects.get(pk=id)
    category = Category.objects.all()
    context={'products': products,
             'category':category,
             'catdata':catdata,
             'slug': slug}
    return render(request,'coincollection/country.html',context)