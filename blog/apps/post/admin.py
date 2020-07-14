from django.contrib import admin
from lib import constants as const
from apps.post.models import Post, Comment

class PostAdmin(admin.ModelAdmin):
	list_display = [
		const.ID_PROPERTY,
		const.POST_ID_PROPERTY,
		const.TITLE_PROPERTY,
		const.DESCRIPTION_PROPERTY,
		const.CATEGORY_PROPERTY
	]

class CommentAdmin(admin.ModelAdmin):
	list_display = [
		const.ID_PROPERTY,
		const.COMMENT_ID_PROPERTY,
		const.DESCRIPTION_PROPERTY,
		const.POST_PROPERTY
	]

admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
