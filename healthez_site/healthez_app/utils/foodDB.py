import datetime
from ..models import Food

def getAllFood():
	food = Food.objects.all()
	food_types = set((obj.foodType for obj in food))
	print(food_types)
	return food_types

def addFood(name, data):
	Food.objects.create(foodType=name, cacheDate=datetime.datetime.now(), data=data)

def retrieveFood(name):
	food = Food.objects.get(pk=name)
	return food