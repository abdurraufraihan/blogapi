from lib import constants as const
from apps.post.serializers.postsaveserializer import PostSaveSerializer
from apps.post.models import Category, Tag

class PostUpdateSerializer(PostSaveSerializer):
	def __init__(self, *args, **kwargs):
		fields = None
		if const.DATA_PROPERTY in kwargs:
			fields = kwargs[const.DATA_PROPERTY].keys()
		super().__init__(*args, **kwargs)
		if fields:
			allowedFields = set(fields)
			existingFields = set(self.fields)
			for fieldName in existingFields - allowedFields:
				self.fields.pop(fieldName)

	def to_representation(self, post):
		if const.TAG_PROPERTY in self.fields:
			self.fields.pop(const.TAG_PROPERTY)
			responseData = super().to_representation(post)
			responseData[const.TAG_PROPERTY] = \
				[tag.name for tag in post.tag.all()]
			return responseData
		return super().to_representation(post)

	def update(self, post, validatedData):
		categoryId = None
		if const.CATEGORY_PROPERTY in validatedData:
			categoryId = validatedData[const.CATEGORY_PROPERTY]
			category = Category.objects.get(categoryId=categoryId)
			validatedData[const.CATEGORY_PROPERTY] = category
		tags = None
		if const.TAG_PROPERTY in validatedData:
			tags = validatedData.pop(const.TAG_PROPERTY)
			tags = [Tag.objects.get(tagId=tag) for tag in tags]
			validatedData[const.TAG_PROPERTY] = tags
		post.title = validatedData.get(const.TITLE_PROPERTY, post.title)
		post.description = \
			validatedData.get(const.DESCRIPTION_PROPERTY, post.description)
		post.category = \
			validatedData.get(const.CATEGORY_PROPERTY, post.category)
		tag = validatedData.get(const.TAG_PROPERTY, post.tag)
		if isinstance(tag, list):
			post.tag.set(tag)
		post.image = validatedData.get(const.IMAGE_PROPERTY, post.image)
		post.save()
		return post
