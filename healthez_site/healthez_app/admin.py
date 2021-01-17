from django.contrib import admin

# Register your models here.

from .models import Food
from .models import listItem
from .models import searchItem

admin.site.register(Food)
admin.site.register(listItem)
admin.site.register(searchItem)