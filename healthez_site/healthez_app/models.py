from django.db import models

# Create your models here.

class Food(models.Model):
	foodType = models.CharField(max_length=100)
	cacheDate = models.DateTimeField('Date cached')
	data = {}