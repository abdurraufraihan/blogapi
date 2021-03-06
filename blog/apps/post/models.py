import uuid
from django.db import models
from django.conf import settings
from lib import constants as const
from lib import commonutility as commonUtil
from apps.taxonomy.models import Category, Tag

class Post(models.Model):
	author = models.ForeignKey(
		settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True
	)
	postId = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
	title = models.CharField(max_length=const.POST_TITLE_MAX_LENGTH)
	description = models.TextField()
	category = models.ForeignKey(
		Category, on_delete=models.SET_NULL, null=True, blank=True
	)
	tag = models.ManyToManyField(Tag)
	image = models.ImageField(upload_to=const.IMAGE_UPLOAD_PATH)

	def __str__(self):
		return self.title

class Comment(models.Model):
	commentId = \
		models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
	description = \
		models.CharField(max_length=const.COMMENT_DESCRIPTION_MAX_LENGTH)
	post = models.ForeignKey(
		Post, on_delete=models.CASCADE, related_name=const.COMMENTS_PROPERTY
	)

	def __str__(self):
		return commonUtil.getSummaryText(
			self.description, const.COMMENT_DESCRIPTION_SUMMARY_LENGTH
		)
