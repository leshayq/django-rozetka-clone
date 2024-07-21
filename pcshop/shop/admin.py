from django.contrib import admin

from .models import Category, Product

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    ordering = ('name',)

    def get_prepopulated_fields(self, request, obj=None):
        return {'slug': ('name',)}
    
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'brand', 'slug', 'price', 'available', 'created_at', 'updated_at')
    ordering = ('title',)
    list_filter = ('available', 'created_at', 'updated_at')

    #при заполнении title автоматически заполняется slug исходя из title с помощью этого метода
    def get_prepopulated_fields(self, request, obj=None):
        return {'slug': ('title',)}
