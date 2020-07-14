from django.contrib import admin
from lib import constants as const
from apps.post.models import Post

class PostAdmin(admin.ModelAdmin):
	list_display = [
		const.ID_PROPERTY,
		const.POST_ID_PROPERTY,
		const.TITLE_PROPERTY,
		const.DESCRIPTION_PROPERTY,
		const.CATEGORY_PROPERTY
	]

admin.site.register(Post, PostAdmin)
