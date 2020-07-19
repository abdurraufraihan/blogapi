from rest_framework import serializers
from lib import constants as const
from apps.post.models import Post, Category, Tag

class PostSaveSerializer(serializers.ModelSerializer):
	category = serializers.UUIDField(required=False)
	tag = serializers.ListField(child=serializers.UUIDField(), required=False)

	def create(self, validatedData):
		categoryId = None
		if const.CATEGORY_PROPERTY in validatedData:
			categoryId = validatedData[const.CATEGORY_PROPERTY]
			category = Category.objects.get(categoryId=categoryId)
			validatedData[const.CATEGORY_PROPERTY] = category
		tags = None
		if const.TAG_PROPERTY in validatedData:
			tags = validatedData.pop(const.TAG_PROPERTY)
			tags = [Tag.objects.get(tagId=tag) for tag in tags]
		post = Post.objects.create(**validatedData)
		if tags and isinstance(tags, list):
			post.tag.set(tags)
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
		extra_kwargs = {
			const.IMAGE_PROPERTY: {const.REQUIRED_PROPERTY: False}
		}
