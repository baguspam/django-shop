from django.contrib import admin
from .models import *
# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name','slug', 'created_at', 'updated_at']
    list_filter = ()
    search_fields = ['name','slug', 'created_at', 'updated_at']
admin.site.register(Category,CategoryAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = ['category', 'name', 'slug', 'description', 'price', 'available', 'stock', 'image', 'created_at', 'updated_at']
    list_filter = ('category',)
    search_fields = ['category__name', 'name', 'slug', 'description', 'price', 'available', 'stock', 'image', 'created_at', 'updated_at']
admin.site.register(Product,ProductAdmin)
    