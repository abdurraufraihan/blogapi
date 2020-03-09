from rest_framework.generics import ListCreateAPIView, \
	RetrieveUpdateDestroyAPIView
from apps.api.permissions.isauthenticatedorgetrequest import \
	IsAuthenticatedOrGetRequest
from apps.taxonomy.models import Category
from apps.taxonomy.serializer.categoryserializer import CategorySerializer

class CategoryListCreateView(ListCreateAPIView):
	permission_classes = [IsAuthenticatedOrGetRequest]

	queryset = Category.objects.all()
	serializer_class = CategorySerializer

class CategoryRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
	permission_classes = [IsAuthenticatedOrGetRequest]

	queryset = Category.objects.all()
	serializer_class = CategorySerializer
