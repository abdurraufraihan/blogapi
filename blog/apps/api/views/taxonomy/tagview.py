from rest_framework.generics import ListCreateAPIView, \
	RetrieveUpdateDestroyAPIView
from apps.api.permissions.isauthenticatedorgetrequest import \
	IsAuthenticatedOrGetRequest
from apps.taxonomy.models import Tag
from apps.taxonomy.serializer.tagserializer import TagSerializer

class TagListCreateView(ListCreateAPIView):
	permission_classes = [IsAuthenticatedOrGetRequest]

	queryset = Tag.objects.all()
	serializer_class = TagSerializer

class TagRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
	permission_classes = [IsAuthenticatedOrGetRequest]

	queryset = Tag.objects.all()
	serializer_class = TagSerializer
