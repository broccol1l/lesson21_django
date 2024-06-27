from django.contrib import admin

from .models import CategoryModel, ProductModel, NewsCategory, News, CartModel

@admin.register(CategoryModel)
class CategoryModelAdmin(admin.ModelAdmin):
    search_fields = ['category_name']
    list_display = ['id', 'category_name', 'created_at']
    list_filter = ['created_at']
    ordering = ['-id']

@admin.register(ProductModel)
class ProductModelAdmin(admin.ModelAdmin):
    search_fields = ['product_name']
    list_display = ['id', 'product_name', 'price', 'count', 'created_at']
    list_filter = ['created_at']
    ordering = ['-id']

@admin.register(NewsCategory)
class NewsCategoryAdmin(admin.ModelAdmin):
    search_fields = ['category_name']
    list_display = ['id', 'category_name', 'created_at']
    list_filter = ['created_at']
    ordering = ['-id']

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    search_fields = ['title']
    list_display = ['id', 'title', 'created_at']
    list_filter = ['created_at']
    ordering = ['-id']

@admin.register(CartModel)
class CartModelAdmin(admin.ModelAdmin):
    search_fields = ['user_id, user_product']
    list_display = ['user_id', 'user_product', 'user_product_quantity', 'user_add_date']
    list_filter = ['user_add_date']
    ordering = ['-user_id']