from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from lib import errorutility as errorUtil
from apps.api.permissions.isauthenticatedorgetrequest import \
	IsAuthenticatedOrGetRequest
from apps.post.serializers.postresponseserializer import PostResponseSerializer
from apps.post.serializers.postupdateserializer import PostUpdateSerializer
from apps.post.models import Post

class PostRetrieveUpdateDestroyView(APIView):
	permission_classes = [IsAuthenticatedOrGetRequest]

	def getPost(self, postId):
		try:
			return Post.objects.get(postId=postId)
		except Post.DoesNotExist:
			return None

	def get(self, request, postId, format=None):
		try:
			post = self.getPost(postId)
			if not post:
				return errorUtil.getPostDoesNotExistError()
			serializer = PostResponseSerializer(post)
			return Response(serializer.data, status=status.HTTP_200_OK)
		except:
			return errorUtil.getInternalServerError()

	def put(self, request, postId, format=None):
		try:
			post = self.getPost(postId)
			if not post:
				return errorUtil.getPostDoesNotExistError()
			serializer = PostUpdateSerializer(post, data=request.data)
			if serializer.is_valid():
				serializer.save()
				return Response(serializer.data, status=status.HTTP_200_OK)
			else:
				return Response(
					serializer.errors, status=status.HTTP_400_BAD_REQUEST
				)
		except:
			return errorUtil.getInternalServerError()

	def delete(self, request, postId, format=None):
		post = self.getPost(postId)
		if not post:
			return errorUtil.getPostDoesNotExistError()
		post.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)
