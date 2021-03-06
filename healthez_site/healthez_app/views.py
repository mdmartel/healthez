import pandas as pd
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template import RequestContext
from .utils import foodDB
from .utils.getFoodData import getFoodData
from .utils.callUPCAPI import readBarcode
from .utils.callUPCAPI import callUPCAPI
from .utils.callUPCAPI import barcodeSearch
from .utils.callUPCAPI import retrieveCodeObj
# Create your views here.

from .models import listItem
from .models import searchItem
from .models import barcodeResult
from .forms import barcodeForm


def barcodeImageView(request):
	data = None
	img_url = None
	if request.method == 'POST':
		form = barcodeForm(request.POST, request.FILES) 
		if form.is_valid(): 
			form.save()
			print(form.__dict__)
			UPC_code = readBarcode(form.instance.barcode_Image)
			if UPC_code:
				cached = barcodeSearch(UPC_code)
				if cached:
					api_result = cached 
				else:
					api_result = callUPCAPI(UPC_code)
					barcodeResult.objects.create(barcode=UPC_code, data=api_result)
			data = api_result['products'][0]
			img_url = data['images'][0]
			print(api_result['products'])
			print(api_result['products'][0]['product_name'])
			print(api_result['products'][0]['images'])
		else: 
			form = barcodeForm() 
			pass
		if data == None:
			return render(request, 'images.html', {'form' : form}) 
		else:
			obj = retrieveCodeObj(UPC_code)
			return render(request, 'images_result.html', {'form' : form, 'data':data, 'img_url':img_url, 'item':obj}) 
	return render(request, 'images.html', data) 
  
def addItemBarcode(request, itemID):
	item_to_add = barcodeResult.objects.get(id=itemID).data['products'][0]
	name = item_to_add['product_name']
	product_id = -1
	img_url = item_to_add['images'][0]

	listItem.objects.create(content=name, product_id=product_id, img_url=img_url, data=item_to_add)
	return HttpResponseRedirect("/form/")


def getItemData(request, itemID):
	item_to_get = listItem.objects.get(id=itemID)

	#foodData = getFoodData(item_to_search.product_id)
	return render(request, "details.html", {"obj": item_to_get.data, 'img_url':item_to_get.img_url})


def FormInput(request):
	all_list_items = listItem.objects.all()
	print(all_list_items)
	return render(request, "Input.html", {"all_items": all_list_items})

def addItem(request, itemID):
	item_to_add = searchItem.objects.get(id=itemID)
	name = item_to_add.title
	product_id = item_to_add.product_id
	img_url = item_to_add.img_url
	data = getFoodData(product_id)

	# Remove underscores from important badges
	badges = data['importantBadges']
	for i in range(len(badges)):
		badges[i] = badges[i].replace('_', ' ')
	data['importantBadges'] = badges

	# Remove underscores from badges
	badges = data['badges']
	for i in range(len(badges)):
		badges[i] = badges[i].replace('_', ' ')
	data['badges'] = badges
	print(data)
	listItem.objects.create(content=name, product_id=product_id, img_url=img_url, data=data)
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
	num_items = len(all_search_items)
	divider = int(num_items/3)
	col1 = all_search_items[0:divider] 
	col2 = all_search_items[divider:divider*2]
	col3 = all_search_items[divider*2:]
	return render(request, 'item_select.html', {"col1":col1,"col2":col2,"col3":col3})


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