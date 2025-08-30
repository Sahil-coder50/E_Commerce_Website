from django.contrib import admin
from . models import Products

# Register your models here.

class ProductsAdmin(admin.ModelAdmin):
    list_display=['id','title','price','discount_price','category','description','image']
    list_display_links=['title']
    search_fields=['title']

admin.site.register(Products,ProductsAdmin)

