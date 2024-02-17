from django.contrib import admin
from .models import *

class AdminProduct(admin.ModelAdmin):
    list_display = ['name' , 'price', 'category']

# Register your models here.
admin.site.register(Product,AdminProduct)
admin.site.register(Category)
admin.site.register(Customer)