from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from lib import errorutility as errorUtil
from lib import constants as const, errormessages as errorMessage
from apps.post.models import Post, Comment
from apps.post.serializers.commentserializer import CommentSerializer

class CommentListCreateView(APIView):
	def dispatch(self, request, postId, *args, **kwargs):
		isPostIdExist = Post.objects.filter(postId=postId).exists()
		if not isPostIdExist:
			return JsonResponse(
				{const.ERROR_PROPERTY:
					errorMessage.POST_ID_DOES_NOT_EXIST_ERROR},
				status=status.HTTP_404_NOT_FOUND
			)
		return super().dispatch(request, postId, *args, **kwargs)

	def get(self, request, postId, format=None):
		try:
			comments = Comment.objects.filter(post__postId=postId)
			serializer = CommentSerializer(comments, many=True)
			return Response(serializer.data, status=status.HTTP_200_OK)
		except:
			return errorUtil.getInternalServerError()
