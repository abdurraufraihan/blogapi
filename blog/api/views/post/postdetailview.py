from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from lib import constants as const
from lib import errormessages as errorMessage
from post.serializers.postresponseserializer import PostResponseSerializer
from post.serializers.postupdateserializer import PostUpdateSerializer
from post.models import Post

class PostDetailView(APIView):
	def getPost(self, pk):
		try:
			return Post.objects.get(pk=pk)
		except Post.DoesNotExist:
			return None

	def get(self, request, pk, format=None):
		try:
			post = self.getPost(pk)
			if not post:
				return Response(
					{const.ERROR_PROPERTY : \
						errorMessage.POST_DOES_NOT_EXIST_ERROR},
					status=status.HTTP_404_NOT_FOUND
				)
			serializer = PostResponseSerializer(post)
			return Response(serializer.data, status=status.HTTP_200_OK)
		except:
			return Response(
				{const.ERROR_PROPERTY : errorMessage.INTERNAL_SERVER_ERROR},
				status=status.HTTP_404_NOT_FOUND
			)

	def put(self, request, pk, format=None):
		try:
			post = self.getPost(pk)
			if not post:
				return Response(
					{const.ERROR_PROPERTY : \
						errorMessage.POST_DOES_NOT_EXIST_ERROR},
					status=status.HTTP_404_NOT_FOUND
				)
			serializer = PostUpdateSerializer(post, data=request.data)
			if serializer.is_valid():
				serializer.save()
				return Response(serializer.data, status=status.HTTP_200_OK)
			else:
				return Response(
					serializer.errors, status=status.HTTP_400_BAD_REQUEST
				)
		except:
			return Response(
				{const.ERROR_PROPERTY : errorMessage.INTERNAL_SERVER_ERROR},
				status=status.HTTP_404_NOT_FOUND
			)
