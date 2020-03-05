from django.db import models
from taxonomy.models import Category, Tag

class Post(models.Model):
	title = models.CharField(max_length=50)
	description = models.TextField()
	category = models.ForeignKey(
		Category, on_delete=models.SET_NULL, null=True, blank=True
	)
	tag = models.ManyToManyField(Tag)

	def __str__(self):
		return self.title
