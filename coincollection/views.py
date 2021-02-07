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


def coinbase(request):
    category = Category.objects.all()
    all_products = Product.objects.all()
    page = "somu-overview"
    order = Product.objects.all()
    myFilter = ProductFilter(request.GET, queryset=order)
    order = myFilter.qs
    context={'category':category, 'all_products':all_products, 'order':order, 'myFilter':myFilter}
    return render(request, 'coincollection/base.html',context)

def country(request,id,slug):
    products = Product.objects.filter(category_id=id) 
    all_products = Product.objects.all()
    catdata = Category.objects.get(pk=id)
    category = Category.objects.all()
    context={'products': products,
             'all_products':all_products, 
             'category':category,
             'catdata':catdata,
             'slug': slug}
    return render(request,'coincollection/country.html',context)

def coin_detail(request,id,slug):
    category = Category.objects.all()
    product = Product.objects.get(pk=id)
    context = {'product': product,'category': category,
               }
    return render(request,'coincollection/coin_detail.html',context)

def coin_filter(request):
    category = Category.objects.all()
    all_products = Product.objects.all()
    page = "somu-overview"
    order = Product.objects.all()
    myFilter = ProductFilter(request.GET, queryset=order)
    order = myFilter.qs
    context={'category':category, 'all_products':all_products, 'order':order, 'myFilter':myFilter}
    return render(request,'coincollection/coinfilter.html',context)
