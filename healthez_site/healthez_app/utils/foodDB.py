import datetime
from ..models import Food
from .callFoodAPI import callFoodAPI

def foodSearch(user_food):
    cachedFood = getAllFood() # Type = python set
    if user_food not in cachedFood:
        foodData = callFoodAPI(user_food)
        addFood(user_food, foodData)
    else:
        foodData = retrieveFood(user_food)
    return foodData

def getAllFood():
	food = Food.objects.all()
	food_types = set((obj.foodType for obj in food))
	print(food_types)
	return food_types

def addFood(name, data):
	Food.objects.create(foodType=name, cacheDate=datetime.datetime.now(), data=data.json())

def retrieveFood(name):
	food = Food.objects.filter(foodType=name)[0]
	return food.data