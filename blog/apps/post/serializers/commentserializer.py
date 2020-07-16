from rest_framework import serializers
from lib import constants as const
from apps.post.models import Post, Comment

class CommentSerializer(serializers.ModelSerializer):
	id = serializers.UUIDField(source=const.COMMENT_ID_PROPERTY, read_only=True)

	class Meta:
		model = Comment
		fields = [
			const.ID_PROPERTY,
			const.DESCRIPTION_PROPERTY
		]

	def create(self, validatedData):
		post = Post.objects.get(postId=validatedData[const.POST_ID_PROPERTY])
		return Comment.objects.create(
			description=validatedData[const.DESCRIPTION_PROPERTY], post=post
		)
