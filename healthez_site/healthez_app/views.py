import pandas as pd
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template import RequestContext
from .utils import foodDB
# Create your views here.

from .models import listItem
from .models import searchItem

def FormInput(request):
	all_list_items = listItem.objects.all()
	return render(request, "Form_input.html", {"all_items": all_list_items})

def addItem(request, itemID):
	#new_item = listItem(content = request.POST.get('name', "none"))
	#new_item.save()
	item_to_add = searchItem.objects.get(id=itemID)

	name = item_to_add.title
	product_id = item_to_add.product_id
	listItem.objects.create(content=name, product_id=product_id)
	return HttpResponseRedirect("/form/")

def deleteItem(request, itemID):
	item_to_delete = listItem.objects.get(id=itemID)
	item_to_delete.delete()
	return HttpResponseRedirect("/form/")

def itemSelectPage(request):
	api_response = foodDB.foodSearch(request.POST['name'])
	if isinstance(api_response, dict):
		response_df = pd.DataFrame.from_dict(api_response)
	else:
		response_df = pd.read_json(api_response.content)
	items = response_df['products']
	# Delete all items before new search
	searchItem.objects.all().delete()
	for index in range(len(response_df)):
		item_info = items[index]
		item_name = item_info["title"]
		item_img_url = item_info["image"]
		item_product_id = item_info["id"]
		searchItem.objects.create(title=item_name, img_url=item_img_url, product_id=item_product_id)
	all_search_items = searchItem.objects.all()
	return render(request, 'item_select.html', {"search_items":all_search_items})


def selectItem(request):
	pass

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