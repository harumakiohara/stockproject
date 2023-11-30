from django.contrib import admin

# Register your models here.
from .models import Category, StockPost

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id','title')
    list_diplay_links = ('id','title')
class StockPostAdmin(admin.ModelAdmin):
    list_display = ('id','title')
    list_display_links = ('id','title')

admin.site.register(Category, CategoryAdmin)

admin.site.register(StockPost,StockPostAdmin)
