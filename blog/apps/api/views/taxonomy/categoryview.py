from rest_framework.generics import ListCreateAPIView, \
	RetrieveUpdateDestroyAPIView
from apps.api.permissions.isauthenticatedorgetrequest import \
	IsAuthenticatedOrGetRequest
from apps.taxonomy.models import Category
from apps.taxonomy.serializer.categoryserializer import CategorySerializer
from lib import constants as const

class CategoryListCreateView(ListCreateAPIView):
	permission_classes = [IsAuthenticatedOrGetRequest]

	queryset = Category.objects.all()
	serializer_class = CategorySerializer

class CategoryRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
	lookup_field = const.CATEGORY_ID_PROPERTY
	permission_classes = [IsAuthenticatedOrGetRequest]

	queryset = Category.objects.all()
	serializer_class = CategorySerializer
