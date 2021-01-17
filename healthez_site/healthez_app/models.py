from django.db import models
from django.db.models import JSONField

# Create your models here.

class Food(models.Model):
	foodType = models.CharField(max_length=100)
	cacheDate = models.DateTimeField('Date cached')
	data = JSONField()

class listItem(models.Model):
	content = models.TextField()
	product_id = models.TextField()

class searchItem(models.Model):
	title = models.TextField()
	img_url = models.TextField()
	product_id = models.TextField()
