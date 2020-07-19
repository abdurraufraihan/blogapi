from rest_framework import serializers
from lib import constants as const
from apps.taxonomy.models import Category

class CategorySerializer(serializers.ModelSerializer):
	id = \
		serializers.UUIDField(source=const.CATEGORY_ID_PROPERTY, read_only=True)

	class Meta:
		model = Category
		fields = [const.ID_PROPERTY, const.NAME_PROPERTY]
