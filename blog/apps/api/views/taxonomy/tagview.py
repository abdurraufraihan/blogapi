from rest_framework.generics import ListCreateAPIView, \
	RetrieveUpdateDestroyAPIView
from apps.api.permissions.isauthenticatedorgetrequest import \
	IsAuthenticatedOrGetRequest
from apps.taxonomy.models import Tag
from apps.taxonomy.serializer.tagserializer import TagSerializer
from lib import constants as const

class TagListCreateView(ListCreateAPIView):
	permission_classes = [IsAuthenticatedOrGetRequest]

	queryset = Tag.objects.all()
	serializer_class = TagSerializer

class TagRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
	lookup_field = const.TAG_ID_PROPERTY
	permission_classes = [IsAuthenticatedOrGetRequest]

	queryset = Tag.objects.all()
	serializer_class = TagSerializer
