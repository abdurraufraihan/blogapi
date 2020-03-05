from django.contrib import admin
from .models import Category, Tag

class CategoryAdmin(admin.ModelAdmin):
	list_display = ['name']

class TagAdmin(admin.ModelAdmin):
	list_display = ['name']

admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
