from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from lib import constants as const
from lib import errorutility as errorUtil
from lib import commonutility as commonUtil
from api.permissions.isauthenticatedorgetrequest import \
	IsAuthenticatedOrGetRequest
from post.serializers.postresponseserializer import PostResponseSerializer
from post.serializers.postsaveserializer import PostSaveSerializer
from post.models import Post

class PostListCreateView(APIView):
	permission_classes = [IsAuthenticatedOrGetRequest]

	def get(self, request, format=None):
		try:
			page = request.query_params.get(const.PAGINATION_QUERY_PARAM)
			startItem, endItem = \
				commonUtil.getPaginationRange(page, const.POST_PER_PAGE)
			queryset = Post.objects.all()[startItem : endItem]
			serializer = PostResponseSerializer(queryset, many=True)
			return Response(serializer.data, status=status.HTTP_200_OK)
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
		except:
			return errorUtil.getInternalServerError()
