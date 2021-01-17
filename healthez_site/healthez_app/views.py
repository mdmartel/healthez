from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template import RequestContext
from .utils import foodDB
# Create your views here.

from .models import listItem

def FormInput(request):
	all_list_items = listItem.objects.all()
	return render(request, "Form_input.html", {"all_items": all_list_items})

def addItem(request):
	#new_item = listItem(content = request.POST.get('name', "none"))
	#new_item.save()
	name = request.POST['name']
	listItem.objects.create(content=name)
	return HttpResponseRedirect("/form/")

def deleteItem(request, itemID):
	item_to_delete = listItem.objects.get(id=itemID)
	item_to_delete.delete()
	return HttpResponseRedirect("/form/")

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

def search_test(request):
	return render(request, 'Form_input.html', {})

def run_search(request):
	if request.method == 'POST':
		print(request.POST['name'])
		return render(request, 'Form_input.html')