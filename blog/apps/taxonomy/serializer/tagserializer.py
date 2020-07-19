from rest_framework import serializers
from lib import constants as const
from apps.taxonomy.models import Tag

class TagSerializer(serializers.ModelSerializer):
	id = serializers.UUIDField(source=const.TAG_ID_PROPERTY, read_only=True)

	class Meta:
		model = Tag
		fields = [const.ID_PROPERTY, const.NAME_PROPERTY]
