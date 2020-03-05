from django.contrib import admin
from .models import Category, Tag

class CategoryAdmin(admin.ModelAdmin):
	list_display = ['id', 'name']

class TagAdmin(admin.ModelAdmin):
	list_display = ['id', 'name']

admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
