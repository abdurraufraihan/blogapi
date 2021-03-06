from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from lib import errorutility as errorUtil, errormessages as errorMessage
from apps.api.permissions.isauthenticatedorgetrequest import \
	IsAuthenticatedOrGetRequest
from apps.post.serializers.postresponseserializer import PostResponseSerializer
from apps.post.serializers.postupdateserializer import PostUpdateSerializer
from apps.post.models import Post, Category, Tag

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
				return errorUtil.getDoesNotExistError(
					errorMessage.POST_DOES_NOT_EXIST_ERROR
				)
			serializer = PostResponseSerializer(post)
			return Response(serializer.data, status=status.HTTP_200_OK)
		except:
			return errorUtil.getInternalServerError()

	def put(self, request, postId, format=None):
		try:
			post = self.getPost(postId)
			if not post:
				return errorUtil.getDoesNotExistError(
					errorMessage.POST_DOES_NOT_EXIST_ERROR
				)
			serializer = PostUpdateSerializer(post, data=request.data)
			if serializer.is_valid():
				serializer.save()
				return Response(serializer.data, status=status.HTTP_200_OK)
			else:
				return Response(
					serializer.errors, status=status.HTTP_400_BAD_REQUEST
				)
		except Category.DoesNotExist:
			return errorUtil.getDoesNotExistError(
				errorMessage.CATEGORY_DOES_NOT_EXIST_ERROR
			)
		except Tag.DoesNotExist:
			return errorUtil.getDoesNotExistError(
				errorMessage.TAG_DOES_NOT_EXIST_ERROR
			)
		except:
			return errorUtil.getInternalServerError()

	def delete(self, request, postId, format=None):
		post = self.getPost(postId)
		if not post:
			return errorUtil.getPostDoesNotExistError(
				errorMessage.POST_DOES_NOT_EXIST_ERROR
			)
		post.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)
