from django.contrib import admin
from lib import constants as const
from apps.taxonomy.models import Category, Tag

class CategoryAdmin(admin.ModelAdmin):
	list_display = [
		const.ID_PROPERTY,
		const.CATEGORY_ID_PROPERTY,
		const.NAME_PROPERTY
	]

class TagAdmin(admin.ModelAdmin):
	list_display = [
		const.ID_PROPERTY,
		const.TAG_ID_PROPERTY,
		const.NAME_PROPERTY
	]

admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
