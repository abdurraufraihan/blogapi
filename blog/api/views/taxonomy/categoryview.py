from rest_framework.generics import ListCreateAPIView, \
	RetrieveUpdateDestroyAPIView
from api.permissions.isauthenticatedorgetrequest import \
	IsAuthenticatedOrGetRequest
from taxonomy.models import Category
from taxonomy.serializer.categoryserializer import CategorySerializer

class CategoryListCreateView(ListCreateAPIView):
	permission_classes = [IsAuthenticatedOrGetRequest]

	queryset = Category.objects.all()
	serializer_class = CategorySerializer

class CategoryRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
	permission_classes = [IsAuthenticatedOrGetRequest]

	queryset = Category.objects.all()
	serializer_class = CategorySerializer
