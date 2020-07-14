import uuid
from django.db import models
from lib import constants as const

class Category(models.Model):
	categoryId = \
		models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
	name = models.CharField(max_length=const.CATEGORY_NAME_MAX_LENGTH)

	def __str__(self):
		return self.name

class Tag(models.Model):
	tagId = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
	name = models.CharField(max_length=const.TAG_NAME_MAX_LENGTH)

	def __str__(self):
		return self.name
