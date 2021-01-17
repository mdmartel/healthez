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
	return food_types

def addFood(name, data):
	Food.objects.create(foodType=name, cacheDate=datetime.datetime.now(), data=data.json())

def retrieveFood(name):
	food = Food.objects.filter(foodType=name)[0]
	return food.data

def extractDetails(listItem_obj):
	title = listItem_obj['title']
	badges = listItem_obj['importantBadges']
	ingredients = listItem_obj['ingredients']
	nutrition = listItem_obj['nutrition']
	description = listItem_obj['description']

	nutrients = nutrition['nutrients']
	calories = nutrition['calories']
	caloric_breakdown = nutrition['caloric_breakdown']
	fat = nutrition['fat']
	protein = nutrition['protein']
	carbs = nutrition['carbs']

'''
def getAllData():
	food = listItem.objects.all()
	food_types = set((obj.foodType for obj in food))
	return food_types

def retrieveData(name):
	food = listItem.objects.filter(content=name)[0]
	return food.data

def foodDataSearch(food_name):
    cachedData = getAllData() # Type = python set
    if food_name not in cachedData:
    	return None
    else:
        foodData = retrieveFood(user_food)
    return foodData
'''