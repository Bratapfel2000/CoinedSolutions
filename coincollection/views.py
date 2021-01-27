from django.shortcuts import render
from django.http import HttpResponse
from .models import Category, Product
from .filters import ProductFilter

