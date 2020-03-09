from rest_framework import serializers
from apps.lib import constants as const
from apps.taxonomy.models import Category

class CategorySerializer(serializers.ModelSerializer):
	class Meta:
		model = Category
		fields = [const.ID_PROPERTY, const.NAME_PROPERTY]
