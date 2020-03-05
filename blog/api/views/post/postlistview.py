from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from lib import constants as const
from post.serializers.postresponseserializer import PostResponseSerializer
from post.models import Post

class PostListView(APIView):
	def get(self, request, format=None):
		try:
			queryset = Post.objects.all()
			serializer = PostResponseSerializer(queryset, many=True)
			return Response(serializer.data, status=status.HTTP_200_OK)
		except:
			return Response(
				{const.ERROR_PROPERTY : 'Internal server error'},
				status=status.HTTP_500_INTERNAL_SERVER_ERROR
			)
