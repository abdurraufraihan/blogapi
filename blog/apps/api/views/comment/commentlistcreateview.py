from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from lib import errorutility as errorUtil
from apps.post.models import Comment
from apps.post.serializers.commentserializer import CommentSerializer

class CommentListCreateView(APIView):
	def get(self, request, postId, format=None):
		try:
			comments = Comment.objects.filter(post__postId=postId)
			serializer = CommentSerializer(comments, many=True)
			return Response(serializer.data, status=status.HTTP_200_OK)
		except:
			return errorUtil.getInternalServerError()
