from django.shortcuts import render
from django.http import HttpResponse
from .utils import foodDB
# Create your views here.

def index(request):
	return HttpResponse("test")

def bootstrap_test(request):
	return render(request, 'Index.html', {})

def food_test(request):
	foodDB.getAllFood()
	return HttpResponse("Food")

def food_add(request, name):
	foodDB.addFood(name)
	return HttpResponse("added",name)