from rest_framework import serializers
from lib import constants as const
from apps.post.models import Post

class PostSaveSerializer(serializers.ModelSerializer):
	def create(self, validatedData):
		tag = validatedData.pop(const.TAG_PROPERTY)
		post = Post.objects.create(**validatedData)
		if isinstance(tag, list):
			post.tag.set(tag)
		return post

	class Meta:
		model = Post
		fields = [
			const.TITLE_PROPERTY,
			const.DESCRIPTION_PROPERTY,
			const.CATEGORY_PROPERTY,
			const.TAG_PROPERTY,
			const.IMAGE_PROPERTY
		]
