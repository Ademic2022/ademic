from django.contrib import admin
from shop.models import Product
from shop.models import Category

# Register your models here.

admin.site.register(Product)
admin.site.register(Category)