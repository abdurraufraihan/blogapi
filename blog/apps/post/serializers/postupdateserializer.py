from lib import constants as const
from apps.post.serializers.postsaveserializer import PostSaveSerializer

class PostUpdateSerializer(PostSaveSerializer):
	def __init__(self, *args, **kwargs):
		fields = None
		if const.DATA_PROPERTY in kwargs:
			fields = kwargs[const.DATA_PROPERTY].dict().keys()
		super().__init__(*args, **kwargs)
		if fields:
			allowedFields = set(fields)
			existingFields = set(self.fields)
			for fieldName in existingFields - allowedFields:
				self.fields.pop(fieldName)

	def update(self, post, validatedData):
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
