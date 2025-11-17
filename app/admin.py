from django.contrib import admin
from .models import Flower, FlowerCategory

@admin.register(Flower)
class FlowerAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'image')
    search_fields = (['name', 'category'])
    
@admin.register(FlowerCategory)
class FlowerCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'image')
    search_fields = (['name'])
    