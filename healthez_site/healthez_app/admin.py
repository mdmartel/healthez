from django.contrib import admin

# Register your models here.

from .models import Food
from .models import listItem
admin.site.register(Food)
admin.site.register(listItem)