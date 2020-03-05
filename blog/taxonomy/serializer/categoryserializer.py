from rest_framework import serializers
from lib import constants as const
from ..models import Category

class CategorySerializer(serializers.ModelSerializer):
	class Meta:
		model = Category
		fields = [const.ID_PROPERTY, const.NAME_PROPERTY]
