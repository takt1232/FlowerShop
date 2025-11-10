from django.contrib import admin
from .models import Flower

@admin.register(Flower)
class FlowerAdmin(admin.ModelAdmin):
    list_display = ('name', 'image')
    search_fields = ('name',)
    