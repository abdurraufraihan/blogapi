from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from lib import constants as const
from lib import errorutility as errorUtil, errormessages as errorMessage
from lib import commonutility as commonUtil
from apps.api.permissions.isauthenticatedorgetrequest import \
	IsAuthenticatedOrGetRequest
from apps.post.serializers.postresponseserializer import PostResponseSerializer
from apps.post.serializers.postsaveserializer import PostSaveSerializer
from apps.post.models import Post, Category, Tag

class PostListCreateView(APIView):
	permission_classes = [IsAuthenticatedOrGetRequest]

	def get(self, request, format=None):
		try:
			page = request.query_params.get(const.PAGINATION_QUERY_PARAM)
			startItem, endItem = \
				commonUtil.getPaginationRange(page, const.POST_PER_PAGE)
			queryset = Post.objects.all().order_by(const.ORDER_BY_DECENDING_PK)\
				[startItem : endItem]
			serializer = PostResponseSerializer(queryset, many=True)
			postResponse = {
				const.TOTAL_POST_PROPERTY: Post.objects.count(),
				const.POSTS_PROPERTY: serializer.data
			}
			return Response(postResponse, status=status.HTTP_200_OK)
		except:
			return errorUtil.getInternalServerError()

	def post(self, request, format=None):
		try:
			serializer = PostSaveSerializer(data=request.data)
			if serializer.is_valid():
				post = serializer.save()
				serializer = PostResponseSerializer(post)
				return Response(serializer.data, status=status.HTTP_201_CREATED)
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
