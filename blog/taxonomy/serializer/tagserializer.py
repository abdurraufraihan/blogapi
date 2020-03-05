from rest_framework import serializers
from lib import constants as const
from ..models import Tag

class TagSerializer(serializers.ModelSerializer):
	class Meta:
		model = Tag
		fields = [const.ID_PROPERTY, const.NAME_PROPERTY]
