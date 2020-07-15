from rest_framework import serializers
from lib import constants as const
from apps.post.models import Comment

class CommentSerializer(serializers.ModelSerializer):
	class Meta:
		model = Comment
		fields = [
			const.COMMENT_ID_PROPERTY,
			const.DESCRIPTION_PROPERTY
		]
