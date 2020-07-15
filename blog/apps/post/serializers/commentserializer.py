from rest_framework import serializers
from lib import constants as const
from apps.post.models import Comment

class CommentSerializer(serializers.ModelSerializer):
	id = serializers.UUIDField(source=const.COMMENT_ID_PROPERTY, read_only=True)

	class Meta:
		model = Comment
		fields = [
			const.ID_PROPERTY,
			const.DESCRIPTION_PROPERTY
		]
