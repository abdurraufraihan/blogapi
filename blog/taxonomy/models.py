from django.db import models

class Category(models.Model):
	name = models.CharField(max_length=30)

	def __str__(self):
		return self.name

class Tag(models.Model):
	name = models.CharField(max_length=30)

	def __str__(self):
		return self.name
